<?php
/**
 * Админка сайта Учебного центра ДПО (ООО «КОНСАЛТЛАБ»).
 * Программы и цены, разделы «Сведений», документы, контакты, онлайн-оплата Т-Банка, пароль.
 * Данные — в ../data/*.php (сервер их исполняет, а не отдаёт). Страницы — обычные HTML, админка правит их по меткам.
 */
declare(strict_types=1);
mb_internal_encoding('UTF-8');
header('X-Frame-Options: DENY');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: same-origin');
header('Cache-Control: no-store');

const ROOT = __DIR__ . '/..';
const DATA = ROOT . '/data';
const FILES_DIR = ROOT . '/docs/files';
const PAGES = ['index.html', 'sveden.html', 'oferta.html', 'politika.html', 'soglasie.html'];
const DIRS = ['smk' => 'Системы менеджмента качества', 'mgmt' => 'Управление', 'tech' => 'Техника и оборудование', '' => 'Без направления'];
const TYPES = ['pk' => 'Повышение квалификации', 'pp' => 'Профессиональная переподготовка'];
const SV_TITLES = [
  'osnovnye' => 'Основные сведения', 'struktura' => 'Структура и органы управления', 'dokumenty' => 'Документы',
  'obrazovanie' => 'Образование', 'rukovodstvo' => 'Руководство. Педагогический состав', 'mto' => 'Материально-техническое обеспечение',
  'platnye' => 'Платные образовательные услуги', 'fhd' => 'Финансово-хозяйственная деятельность', 'vakantnye' => 'Вакантные места для приёма (перевода)',
  'dostupnaya-sreda' => 'Доступная среда', 'stipendii' => 'Стипендии и иные виды материальной поддержки', 'standarty' => 'Образовательные стандарты и требования',
  'mezhdunarodnoe' => 'Международное сотрудничество', 'rekvizity' => 'Реквизиты',
];
const UPLOAD_EXT = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'jpg', 'jpeg', 'png'];
const UPLOAD_MAX = 15 * 1024 * 1024;

session_name('cl_admin');
session_set_cookie_params(['httponly' => true, 'samesite' => 'Strict', 'secure' => !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off', 'path' => dirname($_SERVER['SCRIPT_NAME'])]);
session_start();

/* ---------- хранилище ---------- */
function load(string $n, $def) { $f = DATA . "/$n.php"; if (!is_file($f)) return $def; $v = include $f; return is_array($v) ? $v : $def; }
function store(string $n, array $v): void {
  if (!is_dir(DATA)) mkdir(DATA, 0750, true);
  $f = DATA . "/$n.php"; $tmp = $f . '.tmp';
  file_put_contents($tmp, "<?php\n// создано админкой " . date('d.m.Y H:i') . "\nreturn " . var_export($v, true) . ";\n", LOCK_EX);
  rename($tmp, $f);
  if (function_exists('opcache_invalidate')) @opcache_invalidate($f, true);
}
function page_path(string $p): string { return ROOT . '/' . $p; }
function backup(string $p): void {
  $dir = DATA . '/backup'; if (!is_dir($dir)) mkdir($dir, 0750, true);
  // копия начинается с exit-заглушки PHP: через браузер её не открыть, даже если .htaccess не работает
  file_put_contents($dir . '/' . basename($p, '.html') . '-' . date('Ymd-His') . '-' . substr(bin2hex(random_bytes(2)), 0, 4) . '.php', "<?php exit; ?>\n" . file_get_contents(page_path($p)));
  $all = glob($dir . '/' . basename($p, '.html') . '-*.php') ?: []; sort($all);
  foreach (array_slice($all, 0, max(0, count($all) - 30)) as $old) @unlink($old);
}
function put_page(string $p, string $html): void {
  backup($p);
  $tmp = page_path($p) . '.tmp'; file_put_contents($tmp, $html, LOCK_EX); rename($tmp, page_path($p));
}
function between(string $s, string $a, string $b): ?array {
  $i = strpos($s, $a); if ($i === false) return null; $i += strlen($a);
  $j = strpos($s, $b, $i); if ($j === false) return null;
  return [$i, $j];
}
function replace_between(string $s, string $a, string $b, string $new): string {
  $r = between($s, $a, $b); if (!$r) throw new RuntimeException('Не найдена метка ' . $a);
  return substr($s, 0, $r[0]) . $new . substr($s, $r[1]);
}
function h(?string $s): string { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }

/* ---------- очистка HTML из редактора ---------- */
function clean_html(string $html): string {
  $allowed = [
    'p' => [], 'br' => [], 'b' => [], 'strong' => [], 'i' => [], 'em' => [], 'u' => [], 'ul' => [], 'ol' => [], 'li' => [],
    'h3' => [], 'h4' => [], 'small' => [], 'span' => [], 'div' => [], 'dl' => [], 'dt' => [], 'dd' => [],
    'table' => [], 'thead' => [], 'tbody' => [], 'tr' => [], 'th' => [], 'td' => [],
    'a' => ['href', 'target', 'rel'],
    'svg' => ['viewbox', 'fill', 'stroke', 'stroke-width', 'aria-hidden'], 'path' => ['d'], 'circle' => ['cx', 'cy', 'r'],
  ];
  $classes = ['sv-t', 'sv-docs', 'sv-doc', 'sv-p', 'sv-list', 'sv-h3', 'sv-tbl', 'sv-prog', 'sv-progs'];
  $doc = new DOMDocument('1.0', 'UTF-8');
  libxml_use_internal_errors(true);
  $doc->loadHTML('<?xml encoding="UTF-8"><div id="__root">' . $html . '</div>', LIBXML_HTML_NOIMPLIED | LIBXML_HTML_NODEFDTD);
  libxml_clear_errors();
  $root = $doc->getElementById('__root');
  if (!$root) return '';
  $walk = function (DOMNode $n) use (&$walk, $allowed, $classes) {
    for ($c = $n->firstChild; $c; $c = $next) {
      $next = $c->nextSibling;
      if ($c instanceof DOMComment || $c instanceof DOMProcessingInstruction) { $n->removeChild($c); continue; }
      if (!($c instanceof DOMElement)) continue;
      $tag = strtolower($c->tagName);
      if (in_array($tag, ['script', 'style', 'iframe', 'object', 'embed', 'form', 'input', 'button', 'textarea', 'select', 'meta', 'link', 'img'], true)) { $n->removeChild($c); continue; }
      if (!isset($allowed[$tag])) { // неизвестный тег — оставить содержимое
        $first = $c->firstChild;
        while ($c->firstChild) $n->insertBefore($c->firstChild, $c);
        $n->removeChild($c); if ($first) $next = $first; continue; // вынутое содержимое тоже проверяем
      }
      foreach (iterator_to_array($c->attributes) as $att) {
        $an = strtolower($att->name);
        if ($an === 'class') {
          $keep = array_values(array_intersect(preg_split('/\s+/', trim($att->value)), $classes));
          if ($keep) $c->setAttribute('class', implode(' ', $keep)); else $c->removeAttribute('class');
          continue;
        }
        if ($an === 'style') { // только простые отступы и размеры, без url() и выражений
          if (!preg_match('/^(\s*(margin|padding)(-top|-bottom)?\s*:\s*[0-9.]+(px|em|rem)?\s*;?)+$/i', $att->value)) $c->removeAttribute('style');
          continue;
        }
        if (!in_array($an, $allowed[$tag], true)) { $c->removeAttribute($att->name); continue; }
        if ($an === 'href') {
          $v = trim($att->value);
          if (!preg_match('~^(https?://|mailto:|tel:|docs/|#|[a-z0-9_-]+\.html)~i', $v)) $c->removeAttribute('href');
        }
      }
      if ($tag === 'a' && $c->getAttribute('target') === '_blank') $c->setAttribute('rel', 'noopener');
      $walk($c);
    }
  };
  $walk($root);
  $out = '';
  foreach ($root->childNodes as $ch) $out .= $doc->saveHTML($ch);
  return trim($out);
}

/* ---------- программы → страницы ---------- */
function progs_default(): array {
  return [
    ['t' => 'Бизнес-процессы, организационное проектирование, механизмы и системы управления', 'type' => 'pk', 'dir' => 'mgmt', 'price' => 0, 'doc' => 'https://disk.yandex.ru/i/po5XBzhk7AcFHQ'],
    ['t' => 'Внутренний аудитор систем менеджмента качества (ISO 9001:2015 / ГОСТ Р ИСО 9001-2015)', 'type' => 'pk', 'dir' => 'smk', 'price' => 0, 'doc' => ''],
    ['t' => 'Разработка и внедрение систем менеджмента качества', 'type' => 'pk', 'dir' => 'smk', 'price' => 0, 'doc' => ''],
    ['t' => 'Внутренний аудит системы менеджмента органов по сертификации продукции в соответствии с ГОСТ Р ИСО 19011-2021 (подготовка внутренних аудиторов)', 'type' => 'pk', 'dir' => 'smk', 'price' => 0, 'doc' => ''],
    ['t' => 'Подготовка экспертов по сертификации и специалистов по разработке систем менеджмента качества организаций в соответствии с ГОСТ Р ИСО 9001-2015 (ISO 9001:2015)', 'type' => 'pk', 'dir' => 'smk', 'price' => 0, 'doc' => ''],
    ['t' => 'Технологические машины и оборудование', 'type' => 'pp', 'dir' => 'tech', 'price' => 0, 'doc' => ''],
  ];
}
function render_progs(array $progs): void {
  $js = [];
  foreach ($progs as $p) { $o = ['t' => $p['t'], 'type' => $p['type'], 'dir' => $p['dir']]; if ($p['price'] > 0) $o['price'] = $p['price']; $js[] = $o; }
  $json = json_encode($js, JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP | JSON_PRETTY_PRINT);
  $idx = file_get_contents(page_path('index.html'));
  $idx = replace_between($idx, '/*admin:P*/', '/*/admin:P*/', 'var P = ' . $json . ';');
  put_page('index.html', $idx);

  $html = '<div class="sv-progs">';
  foreach ($progs as $p) {
    $html .= '<div class="sv-prog"><h4>«' . h($p['t']) . '»</h4><p><span>Вид образования:</span> дополнительное профессиональное образование</p>'
      . '<p><span>Подвид дополнительного образования:</span> ' . ($p['type'] === 'pp' ? 'программа профессиональной переподготовки' : 'программа повышения квалификации') . '</p>'
      . ($p['price'] > 0 ? '<p><span>Стоимость:</span> ' . number_format((float)$p['price'], 0, ',', ' ') . ' ₽</p>' : '')
      . ($p['doc'] !== '' ? '<p><a href="' . h($p['doc']) . '" target="_blank" rel="noopener">Открыть программу</a></p>' : '') . '</div>';
  }
  $html .= '</div>';
  $sv = file_get_contents(page_path('sveden.html'));
  put_page('sveden.html', replace_between($sv, '<!--admin:progs-->', '<!--/admin:progs-->', $html));
}

/* ---------- контакты ---------- */
function digits(string $s): string { $d = preg_replace('/\D/', '', $s); if (strlen($d) === 11 && $d[0] === '8') $d = '7' . substr($d, 1); return $d; }
function apply_contacts(array $old, array $new): int {
  $n = 0;
  foreach (PAGES as $p) {
    $s = file_get_contents(page_path($p)); $o = $s;
    if ($old['phone'] !== $new['phone']) {
      $s = str_replace('tel:+' . digits($old['phone']), 'tel:+' . digits($new['phone']), $s);
      $s = str_replace(h($old['phone']), h($new['phone']), $s);
      $s = str_replace($old['phone'], $new['phone'], $s);
    }
    if ($old['email'] !== $new['email']) $s = str_replace($old['email'], $new['email'], $s);
    if ($s !== $o) { put_page($p, $s); $n++; }
  }
  return $n;
}

/* ---------- файлы ---------- */
function translit(string $s): string {
  $map = ['а'=>'a','б'=>'b','в'=>'v','г'=>'g','д'=>'d','е'=>'e','ё'=>'e','ж'=>'zh','з'=>'z','и'=>'i','й'=>'y','к'=>'k','л'=>'l','м'=>'m','н'=>'n','о'=>'o','п'=>'p','р'=>'r','с'=>'s','т'=>'t','у'=>'u','ф'=>'f','х'=>'h','ц'=>'c','ч'=>'ch','ш'=>'sh','щ'=>'sch','ъ'=>'','ы'=>'y','ь'=>'','э'=>'e','ю'=>'yu','я'=>'ya'];
  $s = strtr(mb_strtolower($s), $map);
  $s = preg_replace('/[^a-z0-9]+/', '-', $s);
  return trim(substr($s, 0, 60), '-') ?: 'file';
}
function files_list(): array {
  if (!is_dir(FILES_DIR)) return [];
  $out = [];
  foreach (glob(FILES_DIR . '/*') ?: [] as $f) if (is_file($f) && in_array(strtolower(pathinfo($f, PATHINFO_EXTENSION)), UPLOAD_EXT, true)) $out[] = ['name' => basename($f), 'size' => filesize($f), 'time' => filemtime($f)];
  usort($out, fn($a, $b) => $b['time'] <=> $a['time']);
  return $out;
}
function upload_one(array $f): array {
  if (($f['error'] ?? 1) !== UPLOAD_ERR_OK) throw new RuntimeException('Файл не загрузился');
  if ($f['size'] > UPLOAD_MAX) throw new RuntimeException('Файл больше 15 МБ');
  $ext = strtolower(pathinfo($f['name'], PATHINFO_EXTENSION));
  if (!in_array($ext, UPLOAD_EXT, true)) throw new RuntimeException('Можно загружать: ' . implode(', ', UPLOAD_EXT));
  $head = (string)file_get_contents($f['tmp_name'], false, null, 0, 8);
  $ok = ($ext === 'pdf' && str_starts_with($head, '%PDF')) || (in_array($ext, ['docx', 'xlsx'], true) && str_starts_with($head, "PK"))
     || (in_array($ext, ['doc', 'xls'], true) && str_starts_with($head, "\xD0\xCF\x11\xE0")) || (in_array($ext, ['jpg', 'jpeg'], true) && str_starts_with($head, "\xFF\xD8"))
     || ($ext === 'png' && str_starts_with($head, "\x89PNG"));
  if (!$ok) throw new RuntimeException('Содержимое файла не похоже на ' . strtoupper($ext));
  if (!is_dir(FILES_DIR)) mkdir(FILES_DIR, 0755, true);
  $base = translit(pathinfo($f['name'], PATHINFO_FILENAME)); $name = "$base.$ext"; $i = 2;
  while (is_file(FILES_DIR . "/$name")) $name = $base . '-' . $i++ . ".$ext";
  move_uploaded_file($f['tmp_name'], FILES_DIR . "/$name");
  @chmod(FILES_DIR . "/$name", 0644);
  return ['name' => $name, 'url' => 'docs/files/' . $name];
}

/* ---------- доступ ---------- */
$auth = load('auth', []);
$csrf = $_SESSION['csrf'] ??= bin2hex(random_bytes(16));
$msg = ''; $err = '';
$post = $_SERVER['REQUEST_METHOD'] === 'POST';
if ($post && !hash_equals($csrf, (string)($_POST['csrf'] ?? ''))) { http_response_code(403); exit('Страница устарела, обновите её.'); }
$act = (string)($_POST['act'] ?? '');

if ($post && $act === 'setup' && empty($auth['hash'])) {
  $p1 = (string)($_POST['p1'] ?? ''); $p2 = (string)($_POST['p2'] ?? '');
  if (mb_strlen($p1) < 8) $err = 'Пароль — не короче 8 символов.';
  elseif ($p1 !== $p2) $err = 'Пароли не совпадают.';
  else { $auth = ['hash' => password_hash($p1, PASSWORD_DEFAULT), 'fails' => 0, 'until' => 0]; store('auth', $auth); session_regenerate_id(true); $_SESSION['ok'] = 1; $msg = 'Пароль сохранён. Запомните его — восстановить можно только через хостинг.'; }
}
if ($post && $act === 'login' && !empty($auth['hash'])) {
  if (($auth['until'] ?? 0) > time()) $err = 'Слишком много попыток. Подождите ' . ceil(($auth['until'] - time()) / 60) . ' мин.';
  elseif (password_verify((string)($_POST['p'] ?? ''), $auth['hash'])) { $auth['fails'] = 0; store('auth', $auth); session_regenerate_id(true); $_SESSION['ok'] = 1; }
  else { $auth['fails'] = ($auth['fails'] ?? 0) + 1; if ($auth['fails'] >= 5) { $auth['until'] = time() + 900; $auth['fails'] = 0; } store('auth', $auth); sleep(1); $err = 'Неверный пароль.'; }
}
if ($post && $act === 'logout') { $_SESSION = []; session_destroy(); header('Location: ./'); exit; }
$in = !empty($_SESSION['ok']) && !empty($auth['hash']);

/* ---------- действия ---------- */
$site = load('site', []);
$site += ['progs' => progs_default(), 'contacts' => ['phone' => '8 991 855-85-05', 'email' => 'center.consultlab@mail.ru']];
$pay = load('pay', ['terminalKey' => '', 'password' => '', 'receipt' => true, 'taxation' => 'usn_income']);
$tab = preg_replace('/[^a-z]/', '', (string)($_GET['tab'] ?? 'progs')) ?: 'progs';

if ($in && $post) {
  try {
    if ($act === 'progs') {
      $rows = $_POST['p'] ?? []; $progs = [];
      foreach ($rows as $r) {
        $t = trim(strip_tags((string)($r['t'] ?? ''))); if ($t === '') continue;
        $type = array_key_exists($r['type'] ?? '', TYPES) ? $r['type'] : 'pk';
        $dir = array_key_exists($r['dir'] ?? '', DIRS) ? $r['dir'] : '';
        $price = (int)round((float)str_replace([' ', ','], ['', '.'], (string)($r['price'] ?? '0')));
        $doc = trim((string)($r['doc'] ?? ''));
        if ($doc !== '' && !preg_match('~^(https?://|docs/)~', $doc)) $doc = '';
        $progs[] = ['t' => mb_substr($t, 0, 300), 'type' => $type, 'dir' => $dir, 'price' => max(0, $price), 'doc' => $doc, 'o' => (int)($r['o'] ?? 0)];
      }
      usort($progs, fn($a, $b) => $a['o'] <=> $b['o']);
      foreach ($progs as &$p) unset($p['o']); unset($p);
      if (!$progs) throw new RuntimeException('Нужна хотя бы одна программа.');
      render_progs($progs); $site['progs'] = $progs; store('site', $site);
      $msg = 'Программы сохранены, сайт обновлён.';
    }
    if ($act === 'sv') {
      $id = (string)($_POST['id'] ?? ''); if (!isset(SV_TITLES[$id])) throw new RuntimeException('Нет такого раздела.');
      $html = clean_html((string)($_POST['html'] ?? ''));
      $sv = file_get_contents(page_path('sveden.html'));
      put_page('sveden.html', replace_between($sv, "<!--admin:sv:$id-->", "<!--/admin:sv:$id-->", $html));
      $msg = 'Раздел «' . SV_TITLES[$id] . '» сохранён.'; $tab = 'sv';
    }
    if ($act === 'upload') {
      $r = upload_one($_FILES['f'] ?? []);
      if (!empty($_POST['ajax'])) { header('Content-Type: application/json; charset=utf-8'); echo json_encode(['ok' => true] + $r, JSON_UNESCAPED_UNICODE); exit; }
      $msg = 'Файл загружен: ' . $r['url']; $tab = 'files';
    }
    if ($act === 'delfile') {
      $n = basename((string)($_POST['name'] ?? '')); $f = FILES_DIR . '/' . $n;
      if ($n === '' || !is_file($f)) throw new RuntimeException('Файл не найден.');
      $used = []; foreach (PAGES as $pg) if (str_contains(file_get_contents(page_path($pg)), 'docs/files/' . $n)) $used[] = $pg;
      if ($used && empty($_POST['force'])) throw new RuntimeException('Файл используется на страницах: ' . implode(', ', $used) . '. Сначала уберите ссылку из раздела.');
      unlink($f); $msg = 'Файл удалён.'; $tab = 'files';
    }
    if ($act === 'contacts') {
      $new = ['phone' => trim(strip_tags((string)$_POST['phone'])), 'email' => trim((string)$_POST['email'])];
      if (strlen(digits($new['phone'])) !== 11) throw new RuntimeException('Телефон: 11 цифр, например 8 991 855-85-05.');
      if (!filter_var($new['email'], FILTER_VALIDATE_EMAIL)) throw new RuntimeException('Проверьте почту.');
      $n = apply_contacts($site['contacts'], $new); $site['contacts'] = $new; store('site', $site);
      $msg = 'Контакты сохранены, обновлено страниц: ' . $n . '. Заявки с сайта приходят на ' . $new['email'] . '.'; $tab = 'contacts';
    }
    if ($act === 'pay') {
      $pay['terminalKey'] = trim((string)$_POST['terminalKey']);
      if (($_POST['password'] ?? '') !== '') $pay['password'] = trim((string)$_POST['password']);
      $pay['receipt'] = !empty($_POST['receipt']);
      $pay['taxation'] = in_array($_POST['taxation'] ?? '', ['osn', 'usn_income', 'usn_income_outcome', 'esn', 'patent'], true) ? $_POST['taxation'] : 'usn_income';
      store('pay', $pay); $msg = 'Настройки оплаты сохранены.'; $tab = 'pay';
    }
    if ($act === 'pass') {
      if (!password_verify((string)$_POST['old'], $auth['hash'])) throw new RuntimeException('Старый пароль неверный.');
      if (mb_strlen((string)$_POST['p1']) < 8 || $_POST['p1'] !== $_POST['p2']) throw new RuntimeException('Новый пароль — не короче 8 символов, оба поля одинаковые.');
      $auth['hash'] = password_hash((string)$_POST['p1'], PASSWORD_DEFAULT); store('auth', $auth); $msg = 'Пароль изменён.'; $tab = 'pass';
    }
  } catch (Throwable $e) {
    if (!empty($_POST['ajax'])) { header('Content-Type: application/json; charset=utf-8'); http_response_code(422); echo json_encode(['ok' => false, 'error' => $e->getMessage()], JSON_UNESCAPED_UNICODE); exit; }
    $err = $e->getMessage();
  }
}

/* ---------- вывод ---------- */
$svId = isset(SV_TITLES[$_GET['id'] ?? '']) ? $_GET['id'] : 'osnovnye';
$svHtml = '';
if ($in && $tab === 'sv') { $sv = file_get_contents(page_path('sveden.html')); $r = between($sv, "<!--admin:sv:$svId-->", "<!--/admin:sv:$svId-->"); $svHtml = $r ? substr($sv, $r[0], $r[1] - $r[0]) : ''; }
$tabs = ['progs' => 'Программы и цены', 'sv' => 'Сведения', 'files' => 'Документы', 'contacts' => 'Контакты', 'pay' => 'Онлайн-оплата', 'pass' => 'Пароль'];
?><!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Админка · Учебный центр ДПО</title>
<style>
:root{--acc:#5A2D91;--ink:#1B1724;--ink2:#5d566b;--bg:#F5F3F9;--line:#DCD3EC;--ok:#1E7B4B;--err:#B3261E}
*{box-sizing:border-box}body{margin:0;font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--ink)}
a{color:var(--acc)}header{background:#fff;border-bottom:1px solid var(--line)}
.w{max-width:1100px;margin:0 auto;padding:0 20px}.hd{display:flex;align-items:center;gap:16px;min-height:64px;flex-wrap:wrap}
.hd b{font-size:18px}.hd .sp{flex:1}
nav.tb{display:flex;gap:6px;flex-wrap:wrap;padding:14px 0}nav.tb a{padding:9px 14px;border-radius:999px;text-decoration:none;background:#fff;border:2px solid var(--line);color:var(--ink);font-weight:500;font-size:15px}
nav.tb a.on{background:var(--acc);border-color:var(--acc);color:#fff}
.card{background:#fff;border:2px solid var(--line);border-radius:18px;padding:22px;margin:0 0 18px}
h1{font-size:24px;margin:0 0 6px}h2{font-size:20px;margin:0 0 12px}.muted{color:var(--ink2);font-size:14px}
label{display:block;font-weight:600;font-size:14px;margin:0 0 6px}
input[type=text],input[type=password],input[type=email],input[type=number],select,textarea{width:100%;font:inherit;padding:10px 12px;border:2px solid var(--line);border-radius:10px;background:#fff}
input:focus,select:focus,textarea:focus,.ed:focus{outline:none;border-color:var(--acc)}
.btn{display:inline-flex;align-items:center;gap:8px;font:inherit;font-weight:600;border:0;border-radius:999px;padding:11px 20px;background:var(--acc);color:#fff;cursor:pointer;text-decoration:none}
.btn.g{background:#EDE6F7;color:var(--acc)}.btn.s{padding:7px 12px;font-size:14px}.btn.r{background:#FBE9E7;color:var(--err)}
.note{padding:12px 16px;border-radius:12px;margin:0 0 16px}.note.ok{background:#E6F4EC;color:var(--ok)}.note.er{background:#FBE9E7;color:var(--err)}
.prog{display:grid;grid-template-columns:34px minmax(0,1fr);gap:12px;border:2px solid var(--line);border-radius:14px;padding:14px;margin:0 0 12px;background:#fff}
.prog .n{display:flex;flex-direction:column;gap:6px;align-items:center}.prog .n button{width:30px;height:30px;border-radius:8px;border:1px solid var(--line);background:#fff;cursor:pointer}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin-top:10px}
@media(max-width:760px){.grid{grid-template-columns:1fr 1fr}}
.tool{display:flex;gap:6px;flex-wrap:wrap;padding:8px;border:2px solid var(--line);border-bottom:0;border-radius:12px 12px 0 0;background:#FAF8FD;position:sticky;top:0;z-index:2}
.tool button{font:inherit;font-size:14px;padding:6px 10px;border-radius:8px;border:1px solid var(--line);background:#fff;cursor:pointer}
.ed{min-height:320px;border:2px solid var(--line);border-radius:0 0 12px 12px;padding:18px;background:#fff;overflow:auto}
.ed dl>div{display:grid;grid-template-columns:1fr 1.2fr;gap:6px 18px;padding:10px 0;border-bottom:1px solid #eee}.ed dt{color:var(--ink2)}.ed dd{margin:0}
.ed .sv-doc{display:flex;gap:10px;align-items:center;border:2px solid var(--line);border-radius:10px;padding:10px 12px;margin:6px 0;text-decoration:none;color:var(--ink)}.ed .sv-doc svg{width:18px;height:18px;flex:none}
.ed .sv-doc small{display:block;color:var(--ink2)}
.ed table{border-collapse:collapse;width:100%}.ed th,.ed td{border:1px solid #e3dcef;padding:8px;text-align:left}
table.fl{width:100%;border-collapse:collapse}table.fl td{padding:10px 8px;border-bottom:1px solid var(--line);vertical-align:middle}
.row{display:flex;gap:12px;flex-wrap:wrap;align-items:end}.row>div{flex:1 1 220px}
.login{max-width:420px;margin:12vh auto}textarea.tt{resize:vertical;min-height:52px}
</style></head><body>
<?php if (!$in): ?>
<div class="w login"><div class="card">
  <h1>Админка сайта</h1><p class="muted">Учебный центр ДПО · ООО «КОНСАЛТЛАБ»</p>
  <?php if ($err): ?><div class="note er"><?= h($err) ?></div><?php endif; ?>
  <?php if (empty($auth['hash'])): ?>
  <form method="post"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="setup">
    <p>Первый вход: придумайте пароль. Он будет только у вас.</p>
    <p><label for="p1">Новый пароль (от 8 символов)</label><input id="p1" type="password" name="p1" autocomplete="new-password" required minlength="8"></p>
    <p><label for="p2">Ещё раз</label><input id="p2" type="password" name="p2" autocomplete="new-password" required minlength="8"></p>
    <button class="btn">Сохранить и войти</button></form>
  <?php else: ?>
  <form method="post"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="login">
    <p><label for="p">Пароль</label><input id="p" type="password" name="p" autocomplete="current-password" required autofocus></p>
    <button class="btn">Войти</button></form>
  <?php endif; ?>
</div></div>
<?php else: ?>
<header><div class="w hd"><b>Админка · Учебный центр ДПО</b><span class="sp"></span>
  <a href="../" target="_blank">Открыть сайт</a>
  <form method="post" style="margin:0"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="logout"><button class="btn g s">Выйти</button></form>
</div></header>
<main class="w">
<nav class="tb"><?php foreach ($tabs as $k => $v): ?><a href="?tab=<?= $k ?>" class="<?= $tab === $k ? 'on' : '' ?>"><?= h($v) ?></a><?php endforeach; ?></nav>
<?php if ($msg): ?><div class="note ok"><?= h($msg) ?></div><?php endif; ?>
<?php if ($err): ?><div class="note er"><?= h($err) ?></div><?php endif; ?>

<?php if ($tab === 'progs'): ?>
<form method="post" class="card" id="pf"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="progs">
  <h2>Программы и цены</h2>
  <p class="muted">Меняются сразу в каталоге на главной, в форме заявки, в «Сведениях» → «Образование» и в онлайн-оплате. Если цена пустая или 0, оплата этой программы онлайн недоступна, а на сайте написано «стоимость указана в прайсе центра».</p>
  <div id="plist">
  <?php foreach ($site['progs'] as $i => $p): ?>
    <div class="prog"><div class="n"><b><?= $i + 1 ?></b><button type="button" class="up" title="Выше">↑</button><button type="button" class="dn" title="Ниже">↓</button></div>
      <div><input type="hidden" class="o" name="p[<?= $i ?>][o]" value="<?= $i ?>">
        <label>Название</label><textarea name="p[<?= $i ?>][t]" rows="2" maxlength="300" class="tt"><?= h($p['t']) ?></textarea>
        <div class="grid">
          <div><label>Вид</label><select name="p[<?= $i ?>][type]"><?php foreach (TYPES as $k => $v): ?><option value="<?= $k ?>" <?= $p['type'] === $k ? 'selected' : '' ?>><?= h($v) ?></option><?php endforeach; ?></select></div>
          <div><label>Направление</label><select name="p[<?= $i ?>][dir]"><?php foreach (DIRS as $k => $v): ?><option value="<?= $k ?>" <?= $p['dir'] === $k ? 'selected' : '' ?>><?= h($v) ?></option><?php endforeach; ?></select></div>
          <div><label>Цена, ₽</label><input type="text" inputmode="numeric" name="p[<?= $i ?>][price]" value="<?= $p['price'] ? (int)$p['price'] : '' ?>" placeholder="например 25000"></div>
          <div><label>Ссылка на программу (PDF)</label><input type="text" name="p[<?= $i ?>][doc]" value="<?= h($p['doc']) ?>" placeholder="docs/files/... или https://"></div>
        </div>
        <p style="margin:10px 0 0"><button type="button" class="btn r s del">Удалить программу</button></p>
      </div></div>
  <?php endforeach; ?>
  </div>
  <p><button type="button" class="btn g" id="addp">+ Добавить программу</button></p>
  <button class="btn">Сохранить программы</button>
</form>
<template id="ptpl"><div class="prog"><div class="n"><b>+</b><button type="button" class="up">↑</button><button type="button" class="dn">↓</button></div><div><input type="hidden" class="o" name="p[__][o]" value="999">
  <label>Название</label><textarea name="p[__][t]" rows="2" maxlength="300" class="tt"></textarea>
  <div class="grid"><div><label>Вид</label><select name="p[__][type]"><?php foreach (TYPES as $k => $v): ?><option value="<?= $k ?>"><?= h($v) ?></option><?php endforeach; ?></select></div>
  <div><label>Направление</label><select name="p[__][dir]"><?php foreach (DIRS as $k => $v): ?><option value="<?= $k ?>"><?= h($v) ?></option><?php endforeach; ?></select></div>
  <div><label>Цена, ₽</label><input type="text" inputmode="numeric" name="p[__][price]" placeholder="например 25000"></div>
  <div><label>Ссылка на программу (PDF)</label><input type="text" name="p[__][doc]" placeholder="docs/files/... или https://"></div></div>
  <p style="margin:10px 0 0"><button type="button" class="btn r s del">Удалить программу</button></p></div></div></template>
<script>
(function(){var L=document.getElementById('plist'),n=1000;
 function renum(){[].forEach.call(L.children,function(c,i){c.querySelector('.o').value=i;c.querySelector('.n b').textContent=i+1})}
 L.addEventListener('click',function(e){var c=e.target.closest('.prog');if(!c)return;
  if(e.target.classList.contains('up')&&c.previousElementSibling)L.insertBefore(c,c.previousElementSibling);
  if(e.target.classList.contains('dn')&&c.nextElementSibling)L.insertBefore(c.nextElementSibling,c);
  if(e.target.classList.contains('del')&&confirm('Удалить программу с сайта?'))c.remove();renum()});
 document.getElementById('addp').addEventListener('click',function(){var t=document.getElementById('ptpl').innerHTML.replace(/__/g,'n'+(n++));L.insertAdjacentHTML('beforeend',t);renum();L.lastElementChild.querySelector('textarea').focus()});
})();
</script>

<?php elseif ($tab === 'sv'): ?>
<div class="card">
  <h2>Сведения об образовательной организации</h2>
  <form method="get" class="row" style="margin-bottom:14px"><input type="hidden" name="tab" value="sv">
    <div><label for="sid">Раздел</label><select id="sid" name="id" onchange="this.form.submit()"><?php foreach (SV_TITLES as $k => $v): ?><option value="<?= $k ?>" <?= $svId === $k ? 'selected' : '' ?>><?= h($v) ?></option><?php endforeach; ?></select></div>
    <div style="flex:0 0 auto"><a class="btn g" href="../sveden.html#<?= h($svId) ?>" target="_blank">Посмотреть на сайте</a></div>
  </form>
  <?php if ($svId === 'obrazovanie'): ?><p class="muted">Список образовательных программ в этом разделе меняется на вкладке «Программы и цены».</p><?php endif; ?>
  <form method="post" id="svf"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="sv"><input type="hidden" name="id" value="<?= h($svId) ?>"><input type="hidden" name="html" id="svh">
    <div class="tool">
      <button type="button" data-c="bold"><b>Ж</b></button><button type="button" data-c="italic"><i>К</i></button>
      <button type="button" data-c="insertUnorderedList">• Список</button><button type="button" data-c="insertOrderedList">1. Список</button>
      <button type="button" data-c="formatBlock" data-v="p">Абзац</button><button type="button" data-c="formatBlock" data-v="h3">Подзаголовок</button>
      <button type="button" id="lnk">Ссылка</button><button type="button" id="ul">+ Документ</button><button type="button" data-c="removeFormat">Убрать оформление</button>
      <input type="file" id="uf" accept=".pdf,.doc,.docx,.xls,.xlsx,.jpg,.jpeg,.png" hidden>
    </div>
    <div class="ed" id="ed" contenteditable="true"><?= $svHtml ?></div>
    <p class="muted">Строки таблиц (слева название, справа значение) правятся прямо в тексте. «+ Документ» загружает файл и добавляет его в раздел ссылкой.</p>
    <button class="btn">Сохранить раздел</button>
  </form>
</div>
<script>
(function(){var ed=document.getElementById('ed'),csrf=<?= json_encode($csrf) ?>;
 document.querySelectorAll('.tool [data-c]').forEach(function(b){b.addEventListener('click',function(){ed.focus();document.execCommand(b.dataset.c,false,b.dataset.v?'<'+b.dataset.v+'>':null)})});
 document.getElementById('lnk').addEventListener('click',function(){var u=prompt('Адрес ссылки (https://…)');if(u){ed.focus();document.execCommand('createLink',false,u)}});
 var uf=document.getElementById('uf');document.getElementById('ul').addEventListener('click',function(){uf.click()});
 uf.addEventListener('change',function(){var f=uf.files[0];if(!f)return;var title=prompt('Название документа на сайте',f.name.replace(/\.[^.]+$/,''));if(title===null)return;
  var fd=new FormData();fd.append('csrf',csrf);fd.append('act','upload');fd.append('ajax','1');fd.append('f',f);
  fetch('./',{method:'POST',body:fd,credentials:'same-origin'}).then(function(r){return r.json()}).then(function(j){if(!j.ok)throw new Error(j.error);
   var box=ed.querySelector('.sv-docs');if(!box){box=document.createElement('div');box.className='sv-docs';ed.appendChild(box)}
   var a=document.createElement('a');a.className='sv-doc';a.href=j.url;a.target='_blank';a.rel='noopener';
   a.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"></path><path d="M14 3v5h5M9 13h6M9 17h6"></path></svg><span><b></b></span><svg viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 9h11M10 4l5 5-5 5"></path></svg>';
   a.querySelector('b').textContent=title||j.name;box.appendChild(a);uf.value='';
  }).catch(function(e){alert('Не загрузилось: '+e.message)})});
 ed.addEventListener('click',function(e){var a=e.target.closest('a.sv-doc');if(a){e.preventDefault();if(confirm('Убрать документ «'+a.textContent.trim()+'» из раздела? Сам файл останется на вкладке «Документы».'))a.remove()}});
 document.getElementById('svf').addEventListener('submit',function(){document.getElementById('svh').value=ed.innerHTML});
})();
</script>

<?php elseif ($tab === 'files'): ?>
<div class="card"><h2>Документы</h2>
  <form method="post" enctype="multipart/form-data" class="row"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="upload">
    <div><label for="f">Загрузить файл (PDF, Word, Excel, JPG, PNG — до 15 МБ)</label><input id="f" type="file" name="f" required accept=".pdf,.doc,.docx,.xls,.xlsx,.jpg,.jpeg,.png"></div>
    <div style="flex:0 0 auto"><button class="btn">Загрузить</button></div></form>
  <p class="muted">Чтобы документ появился в «Сведениях», откройте нужный раздел и нажмите «+ Документ» или вставьте ссылку на файл.</p>
  <table class="fl"><?php foreach (files_list() as $f): ?><tr>
    <td><a href="../docs/files/<?= h($f['name']) ?>" target="_blank"><?= h($f['name']) ?></a><div class="muted"><?= round($f['size'] / 1024) ?> КБ · <?= date('d.m.Y H:i', $f['time']) ?> · ссылка: docs/files/<?= h($f['name']) ?></div></td>
    <td style="text-align:right"><form method="post" onsubmit="return confirm('Удалить файл навсегда?')"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="delfile"><input type="hidden" name="name" value="<?= h($f['name']) ?>"><button class="btn r s">Удалить</button></form></td>
  </tr><?php endforeach; ?></table>
  <?php if (!files_list()): ?><p class="muted">Пока нет загруженных файлов.</p><?php endif; ?>
</div>

<?php elseif ($tab === 'contacts'): ?>
<form method="post" class="card"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="contacts">
  <h2>Контакты</h2><p class="muted">Меняются на всех страницах сайта: в шапке, подвале, «Сведениях» и документах. На эту почту приходят заявки с сайта.</p>
  <div class="row"><div><label for="ph">Телефон</label><input id="ph" type="text" name="phone" value="<?= h($site['contacts']['phone']) ?>"></div>
  <div><label for="em">Электронная почта</label><input id="em" type="email" name="email" value="<?= h($site['contacts']['email']) ?>"></div></div>
  <p class="muted">Адрес и реквизиты ООО указаны в юридических документах — их меняем вместе с документами, напишите нам.</p>
  <button class="btn">Сохранить контакты</button></form>

<?php elseif ($tab === 'pay'): ?>
<form method="post" class="card" autocomplete="off"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="pay">
  <h2>Онлайн-оплата Т-Банка</h2>
  <p class="muted">Данные терминала — в личном кабинете Т-Бизнеса: Интернет-эквайринг → Магазины → Терминалы. Пароль терминала хранится только здесь, на вашем хостинге. Кнопки «Оплатить» на сайте включаются, когда заполнены ключ, пароль и цена программы.</p>
  <div class="row"><div><label for="tk">TerminalKey (ключ терминала)</label><input id="tk" type="text" name="terminalKey" value="<?= h($pay['terminalKey']) ?>"></div>
  <div><label for="tp">Пароль терминала</label><input id="tp" type="password" name="password" placeholder="<?= $pay['password'] ? 'сохранён — оставьте пустым, чтобы не менять' : 'не задан' ?>" autocomplete="new-password"></div></div>
  <div class="row" style="margin-top:12px"><div><label for="tx">Система налогообложения ООО (для чека)</label><select id="tx" name="taxation">
    <?php foreach (['osn' => 'Общая (ОСН)', 'usn_income' => 'УСН «доходы»', 'usn_income_outcome' => 'УСН «доходы минус расходы»', 'esn' => 'ЕСХН', 'patent' => 'Патент'] as $k => $v): ?><option value="<?= $k ?>" <?= $pay['taxation'] === $k ? 'selected' : '' ?>><?= h($v) ?></option><?php endforeach; ?></select></div>
  <div><label><input type="checkbox" name="receipt" value="1" <?= $pay['receipt'] ? 'checked' : '' ?>> Отправлять чеки (подключены «Чеки Т-Бизнеса» или облачная касса)</label></div></div>
  <p style="margin-top:16px"><button class="btn">Сохранить</button></p>
  <p class="muted">Статус: <?= ($pay['terminalKey'] && $pay['password']) ? 'терминал настроен' : 'терминал не настроен — онлайн-оплата выключена' ?>.</p></form>

<?php elseif ($tab === 'pass'): ?>
<form method="post" class="card" style="max-width:520px"><input type="hidden" name="csrf" value="<?= h($csrf) ?>"><input type="hidden" name="act" value="pass">
  <h2>Смена пароля</h2>
  <p><label>Текущий пароль</label><input type="password" name="old" autocomplete="current-password" required></p>
  <p><label>Новый пароль (от 8 символов)</label><input type="password" name="p1" autocomplete="new-password" required minlength="8"></p>
  <p><label>Ещё раз</label><input type="password" name="p2" autocomplete="new-password" required minlength="8"></p>
  <button class="btn">Сменить пароль</button></form>
<?php endif; ?>
<p class="muted" style="margin:24px 0">Перед каждым сохранением админка делает копию страницы. Если что-то пошло не так, напишите нам — восстановим.</p>
</main>
<?php endif; ?>
</body></html>
