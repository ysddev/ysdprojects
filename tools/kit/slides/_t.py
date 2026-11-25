"""Тема презентации: четыре вида слайдов (светлый, тёмный, акцентный, мягкий) из коротких наборов (фон, текст, приглушённый, плашка)."""


def theme(page: str, pink: str, ac: str, aci: str, fh: str, fb: str, light, dark, accent, soft, **extra) -> dict:
    t = {"page": page, "pink": pink, "ac": ac, "aci": aci, "fh": fh, "fb": fb, "hw": "700", "ht": "-.03em", "r": "calc(var(--u)*1.2)"}
    for key, (bg, ink, mut, card) in (("l", light), ("d", dark), ("a", accent), ("s", soft)):
        line = "rgba(255,255,255,.2)" if _dark(bg) else "rgba(0,0,0,.14)"
        t.update({f"{key}-bg": bg, f"{key}-ink": ink, f"{key}-mut": mut, f"{key}-line": line, f"{key}-card": card})
    t.update(extra)
    return t


def _dark(hexc: str) -> bool:
    h = hexc.lstrip("#")
    if len(h) != 6:
        return False
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return (r * 299 + g * 587 + b * 114) / 1000 < 128


# 25.11: подписи над заголовками — обычным регистром, без разрядки: читаются как текст, а не как шаблон
CALM = (".kick{text-transform:none;letter-spacing:0;font-size:calc(var(--u)*1.35);font-weight:600}"
        ".t-cover .badge,.step small,.cts small,.plan small,.tbl th{text-transform:none;letter-spacing:0}"
        ".step small,.cts small,.plan small{font-size:calc(var(--u)*1.25)}.tbl th{font-size:calc(var(--u)*1.2)}"
        "@media screen and (max-width:760px),screen and (orientation:portrait) and (max-width:1100px){"
        ".kick{font-size:14px}.step small,.cts small,.plan small,.tbl th{font-size:14px}.t-cover .badge{font-size:14px}"
        ".t-cover .meta{font-size:14px}.t-cover .meta b{font-size:16px}.num,.brandm{font-size:14px}.donut figcaption span{font-size:14px}.cout p{font-size:14px}.bar b,.bar em,.legend{font-size:14px}.bars{gap:4px}}")
# телефон и узкий экран (лента слайдов): «M + правила + }»
M = "@media screen and (max-width:760px),screen and (orientation:portrait) and (max-width:1100px){"
