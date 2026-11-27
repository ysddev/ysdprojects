<?php
// Заявки с сайта Учебного центра ДПО → письмо на почту центра.
// Работает на хостинге с PHP (на хостинге клиента в РФ). На статичном демо не используется.
header('Content-Type: application/json; charset=utf-8');

$site_data = is_file(__DIR__ . '/data/site.php') ? (include __DIR__ . '/data/site.php') : [];
$TO   = $site_data['contacts']['email'] ?? 'center.consultlab@mail.ru'; // меняется в админке → «Контакты»
$FROM = 'noreply@' . preg_replace('/^www\./', '', $_SERVER['HTTP_HOST'] ?? 'localhost');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }
if (!empty($_POST['hp'])) { echo '{"ok":true}'; exit; } // ловушка для ботов

function f($k, $max = 500) { return trim(mb_substr(strip_tags((string)($_POST[$k] ?? '')), 0, $max)); }
$name = f('name', 120); $phone = f('phone', 40); $prog = f('prog', 300); $who = f('who', 60); $msg = f('msg', 2000);

if (mb_strlen($name) < 2 || strlen(preg_replace('/\D/', '', $phone)) < 10 || ($_POST['agree'] ?? '') !== '1') {
  http_response_code(422); echo '{"ok":false,"error":"fields"}'; exit;
}

// не чаще одной заявки в 20 секунд с одного адреса
$lock = sys_get_temp_dir() . '/cl_lead_' . md5($_SERVER['REMOTE_ADDR'] ?? '');
if (is_file($lock) && time() - filemtime($lock) < 20) { http_response_code(429); echo '{"ok":false}'; exit; }
@touch($lock);

$body = "Заявка с сайта\n\n"
      . "Кто учится: $who\nПрограмма: $prog\nИмя: $name\nТелефон: $phone\n"
      . ($msg !== '' ? "Комментарий: $msg\n" : '')
      . "\nСогласие на обработку персональных данных: дано (" . date('d.m.Y H:i') . ")\n";
$subject = '=?UTF-8?B?' . base64_encode('Заявка на обучение: ' . $name) . '?=';
$headers = "From: Сайт Учебного центра <$FROM>\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit";

$ok = @mail($TO, $subject, $body, $headers, '-f' . $FROM);
echo json_encode(['ok' => (bool)$ok]);
