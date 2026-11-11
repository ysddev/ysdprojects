#!/usr/bin/env python3
"""Демо для клиентов → на адрес портфолио (ysdprojects.space/clients/<slug>/).

Бот собирает демо у себя на сервере (demo.ysdprojects.space/<slug>/), но у части клиентов в России этот сервер не
открывается, а портфолио на GitHub Pages открывается. Поэтому сборка сайта сама забирает демо с сервера бота и кладёт
их рядом с портфолио: список — demo.ysdprojects.space/_demos.json (ведёт бот) плюс clients/_demos.txt (вручную).
Папки сайтов, которые лежат в репозитории (clients/<имя>/), не трогаем.

    python3 tools/pull_demos.py <папка сайта>
"""
import json
import os
import re
import sys
import urllib.request

BASE = "https://demo.ysdprojects.space"
SLUG = re.compile(r"[a-z0-9][a-z0-9-]{2,79}")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "ysd-pages-pull/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def main(out: str) -> int:
    slugs = []
    try:
        slugs += json.loads(get(BASE + "/_demos.json")).get("slugs", [])
    except Exception as exc:  # бот ещё не обновлён или недоступен — работаем по ручному списку
        print("список бота не получен:", exc)
    manual = os.path.join(ROOT, "clients", "_demos.txt")
    if os.path.exists(manual):
        slugs += [ln.strip() for ln in open(manual, encoding="utf-8") if ln.strip() and not ln.startswith("#")]
    changed = 0
    for slug in dict.fromkeys(slugs):
        if not SLUG.fullmatch(slug) or os.path.isdir(os.path.join(ROOT, "clients", slug)):
            continue  # чужое имя или сайт, который ведём руками
        try:
            html = get(f"{BASE}/{slug}/")
        except Exception as exc:
            print(slug, "не скачался:", exc)
            continue
        if b"<html" not in html[:2000].lower() and b"<!doctype" not in html[:200].lower():
            continue
        folder = os.path.join(out, "clients", slug)
        os.makedirs(os.path.join(folder, "img"), exist_ok=True)
        page = os.path.join(folder, "index.html")
        if not os.path.exists(page) or open(page, "rb").read() != html:
            open(page, "wb").write(html)
            changed += 1
        for name in sorted(set(re.findall(rb"img/([a-z0-9_-]{1,40}\.(?:jpg|png|webp))", html))):
            dst = os.path.join(folder, "img", name.decode())
            if os.path.exists(dst):
                continue
            try:
                open(dst, "wb").write(get(f"{BASE}/{slug}/img/{name.decode()}", 60))
                changed += 1
            except Exception as exc:
                print(slug, name.decode(), "не скачалась:", exc)
    print("изменений:", changed)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "site"))
