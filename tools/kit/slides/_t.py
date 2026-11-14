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
