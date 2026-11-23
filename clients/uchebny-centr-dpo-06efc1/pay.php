<?php
// Онлайн-оплата обучения через интернет-эквайринг Т-Банка (метод /v2/Init, платёжная форма банка).
// Заполните 4 строки ниже данными из личного кабинета Т-Бизнеса: Интернет-эквайринг → Магазины → Терминалы.
// Файл лежит на хостинге сайта; пароль терминала в браузер не попадает.
header('Content-Type: application/json; charset=utf-8');

$TERMINAL_KEY = '';            // TerminalKey (рабочий терминал, не DEMO)
$PASSWORD     = '';            // пароль терминала
$RECEIPT      = true;          // чеки 54-ФЗ: true, если подключены «Чеки Т-Бизнеса» или облачная касса
$TAXATION     = 'usn_income';  // система налогообложения ООО: osn, usn_income, usn_income_outcome
// Цены по программам — номер программы в каталоге на главной (0 — первая) => цена в рублях.
$PRICES = [
  // 0 => 25000,
];
$API = 'https://securepay.tinkoff.ru/v2/Init';

$enabled = $TERMINAL_KEY !== '' && $PASSWORD !== '' && count($PRICES) > 0;

if (($_GET['check'] ?? '') === '1') { echo json_encode(['enabled' => $enabled, 'prices' => $PRICES]); exit; }
if (!$enabled || $_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(400); echo '{"ok":false}'; exit; }

function f($k, $max = 200) { return trim(mb_substr(strip_tags((string)($_POST[$k] ?? '')), 0, $max)); }
$idx = (int)($_POST['prog'] ?? -1); $title = f('title', 300);
$name = f('name', 120); $email = f('email', 120); $phone = preg_replace('/[^\d+]/', '', f('phone', 30));
if (!isset($PRICES[$idx]) || mb_strlen($name) < 3 || !filter_var($email, FILTER_VALIDATE_EMAIL) || strlen(preg_replace('/\D/', '', $phone)) < 10 || ($_POST['agree'] ?? '') !== '1') {
  http_response_code(422); echo '{"ok":false,"error":"fields"}'; exit;
}

$amount = (int)round($PRICES[$idx] * 100);       // в копейках, цена берётся с сервера
$site = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off' ? 'https://' : 'http://') . $_SERVER['HTTP_HOST'] . rtrim(dirname($_SERVER['SCRIPT_NAME']), '/');
$desc = mb_substr('Обучение: ' . $title, 0, 140);
$req = [
  'TerminalKey' => $TERMINAL_KEY,
  'Amount'      => $amount,
  'OrderId'     => 'CL-' . date('ymdHis') . '-' . mt_rand(100, 999),
  'Description' => $desc,
  'SuccessURL'  => $site . '/?pay=ok#order',
  'FailURL'     => $site . '/?pay=fail#order',
  'DATA'        => ['Email' => $email, 'Phone' => $phone, 'Name' => $name],
];
if ($RECEIPT) {
  $req['Receipt'] = ['Email' => $email, 'Phone' => $phone, 'Taxation' => $TAXATION, 'Items' => [[
    'Name' => mb_substr($desc, 0, 128), 'Price' => $amount, 'Quantity' => 1, 'Amount' => $amount,
    'Tax' => 'none', 'PaymentMethod' => 'full_payment', 'PaymentObject' => 'service',
  ]]];
}
// Подпись: значения параметров верхнего уровня (без вложенных объектов) + Password, по алфавиту ключей, SHA-256
$t = ['Password' => $PASSWORD];
foreach ($req as $k => $v) { if (!is_array($v)) $t[$k] = is_bool($v) ? ($v ? 'true' : 'false') : (string)$v; }
ksort($t);
$req['Token'] = hash('sha256', implode('', $t));

$ch = curl_init($API);
curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 20,
  CURLOPT_HTTPHEADER => ['Content-Type: application/json'], CURLOPT_POSTFIELDS => json_encode($req, JSON_UNESCAPED_UNICODE)]);
$res = json_decode((string)curl_exec($ch), true); curl_close($ch);

if (!empty($res['Success']) && !empty($res['PaymentURL'])) { echo json_encode(['ok' => true, 'url' => $res['PaymentURL']]); exit; }
http_response_code(502);
echo json_encode(['ok' => false, 'error' => $res['Message'] ?? 'bank']);
