<?php
// Заявки с сайта «ВСЁ ЗА ВАС» → почта. Работает на хостинге с PHP (Reg.ru).
header('Content-Type: application/json; charset=utf-8');
$TO = 'peteryaroshetskiy@yandex.ru';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo '{"success":false}'; exit; }
$d = json_decode(file_get_contents('php://input'), true);
if (!is_array($d)) $d = $_POST;
if (!empty($d['website'])) { echo '{"success":true}'; exit; }   // ловушка для ботов

function f($d, $k, $max = 500) { return trim(mb_substr(strip_tags((string)($d[$k] ?? '')), 0, $max)); }
$name = f($d, 'name', 100);
$phone = f($d, 'phone', 30);
if ($name === '' || strlen(preg_replace('/\D/', '', $phone)) < 11) { http_response_code(422); echo '{"success":false}'; exit; }

$rows = [
  'Имя' => $name, 'Телефон' => $phone, 'Тип недвижимости' => f($d, 'type', 60),
  'Адрес' => f($d, 'address') ?: '—', 'Комментарий' => f($d, 'comment', 2000) ?: '—',
  'Дата' => (new DateTime('now', new DateTimeZone('Europe/Moscow')))->format('d.m.Y H:i'),
];
$body = "Новая заявка с сайта «ВСЁ ЗА ВАС»\n\n";
foreach ($rows as $k => $v) $body .= "$k: $v\n";

$host = preg_replace('/^www\./', '', $_SERVER['HTTP_HOST'] ?? 'vse-za-vas.ru');
$subject = '=?UTF-8?B?' . base64_encode('Новая заявка с сайта «ВСЁ ЗА ВАС»') . '?=';
$headers = "From: =?UTF-8?B?" . base64_encode('ВСЁ ЗА ВАС') . "?= <noreply@$host>\r\n"
         . "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n";
$ok = mail($TO, $subject, $body, $headers, "-fnoreply@$host");
echo json_encode(['success' => $ok]);
