"""Общее для ботов: палитры чата Telegram (светлая и тёмная) и сборка темы."""

TG_LIGHT = {"tgbg": "#dfe7ec", "tghead": "#ffffff", "tghi": "#10161c", "tgin": "#ffffff", "tgink": "#10161c",
            "tgoink": "#10161c", "tgbtn": "rgba(255,255,255,.82)", "tgbtnink": "#10161c", "tgfield": "#f0f2f5"}
TG_DARK = {"tgbg": "#0e1621", "tghead": "#17212b", "tghi": "#ffffff", "tgin": "#182533", "tgink": "#e9eef4",
           "tgoink": "#ffffff", "tgbtn": "rgba(255,255,255,.1)", "tgbtnink": "#ffffff", "tgfield": "#242f3d"}


def theme(dark_chat: bool = False, **v) -> dict:
    """v — цвета и шрифты страницы; чат берёт палитру Telegram, исходящие сообщения — в цвет бренда."""
    t = dict(TG_DARK if dark_chat else TG_LIGHT)
    t.setdefault("tgout", v.pop("tgout", "#2b5278" if dark_chat else "#e3f6d4"))
    t["tgpat"] = v.pop("tgpat", f"linear-gradient(180deg,{t['tgbg']},{t['tgbg']})")
    base = {"rb": "14px", "rc": "22px", "rs": "30px", "hw": "700", "ht": "-.02em", "pbg": "#ffffff", "pink": "#161a20"}
    base.update(t)
    base.update(v)
    return base


FAQ_COMMON = [
    ("Сколько делается такой бот?", "Сценарий согласуем в первый день. Рабочая версия с записью и уведомлениями готова за 3–5 дней, "
                                   "с оплатой и интеграциями — за 7–10 дней."),
    ("Что нужно от нас?", "Список услуг и цен, график работы и доступ к тому, с чем бот должен обмениваться: таблица, CRM или "
                          "учётная система. Тексты сообщений напишем сами и согласуем с вами."),
    ("Можно менять тексты и цены без программиста?", "Да. Услуги, цены, расписание и тексты ответов меняются в админке или "
                                                    "в таблице, бот подхватывает изменения сразу."),
]


def qr_svg(seed: str, n: int = 25) -> str:
    """Рисунок QR-кода для билета или пропуска в чате (иллюстрация: три метки по углам и модули по зерну)."""
    import hashlib
    bits = "".join(f"{b:08b}" for b in hashlib.sha256(seed.encode()).digest() * 4)
    cells, k = [], 0

    def finder(x, y):
        return (0 <= x < 7 and 0 <= y < 7) or (n - 7 <= x < n and 0 <= y < 7) or (0 <= x < 7 and n - 7 <= y < n)

    def finder_on(x, y):
        for ox, oy in ((0, 0), (n - 7, 0), (0, n - 7)):
            if ox <= x < ox + 7 and oy <= y < oy + 7:
                dx, dy = x - ox, y - oy
                return dx in (0, 6) or dy in (0, 6) or (2 <= dx <= 4 and 2 <= dy <= 4)
        return False
    for y in range(n):
        for x in range(n):
            if finder(x, y):
                on = finder_on(x, y)
            elif (x == 7 and y < 8) or (y == 7 and x < 8) or (x == n - 8 and y < 8) or (y == 7 and x >= n - 8) or \
                    (x == 7 and y >= n - 8) or (y == n - 8 and x < 8):
                on = False
            else:
                on = bits[k % len(bits)] == "1"
                k += 1
            if on:
                cells.append(f"M{x} {y}h1v1h-1z")
    return f"<svg viewBox='0 0 {n} {n}' shape-rendering='crispEdges' aria-hidden='true'><path fill='#111' d='{''.join(cells)}'/></svg>"
