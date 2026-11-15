"""Свободная страница работы: вся разметка в конфиге (экспериментальные сайты, которые не ложатся в общий каркас).
Здесь только шрифты (копируются в папку работы), фото (images.txt) и запись index.html."""
from __future__ import annotations

from .common import favicon, fonts, out, save, write_images


def build(c: dict) -> str:
    d = out(c["slug"])
    write_images(d, c.get("images", {}))
    font_css = fonts(d, c["fonts"])
    page = c["html"].replace("/*FONTS*/", font_css).replace("{FAVICON}", favicon(*c["fav"]))
    save(d, page)
    return d
