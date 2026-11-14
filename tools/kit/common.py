"""Общее для генераторов работ портфолио: шрифты (локально, как в остальных работах), фото (images.txt — их
скачивает workflow mirror с Unsplash в webp), запись папки работы."""
from __future__ import annotations

import glob
import html
import json
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORKS = os.path.join(ROOT, "works")

_FONT_INDEX: dict[str, str] = {}


def _index_fonts() -> None:
    if _FONT_INDEX:
        return
    for f in glob.glob(os.path.join(WORKS, "**", "fonts", "*.woff2"), recursive=True):
        if "/shops/" not in f:
            _FONT_INDEX.setdefault(os.path.basename(f), f)
    for f in glob.glob(os.path.join(WORKS, "**", "fonts", "*.woff2"), recursive=True):
        _FONT_INDEX.setdefault(os.path.basename(f), f)


CYR = "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116"
LAT = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,"
       "U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD")


def fonts(out_dir: str, specs: list[tuple[str, str, list[int], str]]) -> str:
    """specs: (css family, file prefix, weights, style). Копирует woff2 в out_dir/fonts, возвращает @font-face."""
    _index_fonts()
    os.makedirs(os.path.join(out_dir, "fonts"), exist_ok=True)
    css = []
    for fam, pref, weights, style in specs:
        for w in weights:
            for sub, rng in (("cyrillic", CYR), ("latin", LAT)):
                name = f"{pref}-{sub}-{w}-{style}.woff2"
                src = _FONT_INDEX.get(name)
                if not src:  # новый шрифт: KIT_FONTS=<папка node_modules/@fontsource> (npm i @fontsource/<имя>)
                    cand = os.path.join(os.environ.get("KIT_FONTS", ""), pref, "files", name)
                    src = cand if os.path.isfile(cand) else None
                if not src:
                    raise FileNotFoundError(name)
                dst = os.path.join(out_dir, "fonts", name)
                if os.path.abspath(src) != os.path.abspath(dst):
                    shutil.copyfile(src, dst)
                css.append(f'@font-face{{font-family:"{fam}";font-style:{style};font-weight:{w};font-display:swap;'
                           f'src:url(fonts/{name}) format("woff2");unicode-range:{rng}}}')
    return "\n".join(css)


def write_images(out_dir: str, images: dict[str, tuple[str, int, int, str]]) -> None:
    """images: имя → (unsplash id, ширина, высота пропорции, ширины через запятую)."""
    lines = ["# имя unsplash-id ширина высота ширины — workflow mirror скачает в img/<имя>-<w>.webp"]
    for name, spec in images.items():
        if len(spec) > 4:
            continue  # фото по прямой ссылке (сайт клиента) — скачивать не нужно
        pid, a, b, widths = spec
        lines.append(f"{name} {pid} {a} {b} {widths}")
    with open(os.path.join(out_dir, "images.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def img(name: str, images: dict, sizes: str = "100vw", alt: str = "", cls: str = "", eager: bool = False) -> str:
    spec = images[name]
    if len(spec) > 4:  # фото по прямой ссылке
        return (f'<img src="{html.escape(spec[4])}" alt="{html.escape(alt)}" width="{spec[1] * 100}" height="{spec[2] * 100}"'
                f'{" class=" + chr(34) + cls + chr(34) if cls else ""}{"" if eager else " loading=" + chr(34) + "lazy" + chr(34)} decoding="async">')
    _, a, b, widths = spec
    ws = [int(w) for w in widths.split(",")]
    srcset = ", ".join(f"img/{name}-{w}.webp {w}w" for w in ws)
    mid = ws[min(1, len(ws) - 1)]
    return (f'<img src="img/{name}-{mid}.webp" srcset="{srcset}" sizes="{sizes}" alt="{html.escape(alt)}" '
            f'width="{a * 100}" height="{b * 100}"{" class=" + chr(34) + cls + chr(34) if cls else ""}'
            f'{"" if eager else " loading=" + chr(34) + "lazy" + chr(34)} decoding="async">')


def e(s: str) -> str:
    return html.escape(s or "", quote=True)


def jdump(x) -> str:
    return json.dumps(x, ensure_ascii=False).replace("</", "<\\/")


def out(slug: str) -> str:
    # «clients/<имя>» — первая версия для клиента (ysdprojects.space/clients/<имя>/), остальное — работы портфолио
    d = os.path.join(ROOT if slug.startswith("clients/") else WORKS, *slug.split("/"))
    os.makedirs(d, exist_ok=True)
    return d


def save(d: str, page: str) -> None:
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)


def favicon(letter: str, bg: str, fg: str) -> str:
    from urllib.parse import quote
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='{bg}'/>"
           f"<text x='32' y='44' font-family='Arial,sans-serif' font-weight='700' font-size='34' text-anchor='middle' "
           f"fill='{fg}'>{letter}</text></svg>")
    return "data:image/svg+xml," + quote(svg)
