"""Главная ysdprojects.space — копия дизайна ysddev.com, но про работы: все 100 работ сразу.

Владелец 25.11.2026: «в проектах ysdprojects все 100 работ поставь и страницу полностью похожим на ysddev.com
сделай, только там про работы речь в основном».

Источник — index.html основного сайта (репозиторий ysddev/ysddev.github.io): берём его вёрстку, стили, скрипты
и список WORKS, убираем цены/отзывы/FAQ/заявку/о студии/ИИ-помощника, переписываем первый экран под портфолио,
показываем все работы с подписями. Ссылки «Цены», «Отзывы», «Оставить заявку» ведут на ysddev.com.

Запуск:
  python3 tools/build_home.py /путь/к/ysddev.github.io
→ home/index.html, home/works.json, картинки работ в home/img (их копирует mirror.yml в корень gh-pages).
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = ROOT / "home"
SITE = "https://ysddev.com"


def cut(s: str, start: str, end: str, include_end: bool = True) -> str:
    i = s.index(start)
    j = s.index(end, i) + (len(end) if include_end else 0)
    return s[:i] + s[j:]


def sub1(s: str, old: str, new: str) -> str:
    assert old in s, f"не нашёл: {old[:80]}"
    return s.replace(old, new, 1)


def works_from(src: str) -> list[dict]:
    i = src.index("var WORKS = [")
    j = src.index("];", i)
    js = "console.log(JSON.stringify(" + src[i + len("var WORKS = "):j + 1] + "))"
    out = subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def pl(n, one, few, many):
    return one if n % 10 == 1 and n % 100 != 11 else few if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else many


def build(src_dir: Path) -> None:
    s = (src_dir / "index.html").read_text(encoding="utf-8")
    works = works_from(s)
    n = len(works)
    cnt = Counter(w["c"] for w in works)

    # --- <head>
    s = re.sub(r"<title>.*?</title>", f"<title>{n} работ YSD DEV онлайн — сайты, магазины, боты, презентации</title>", s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">',
               f'<meta name="description" content="{n} живых проектов студии YSD DEV: сайты, интернет-магазины, Telegram-боты, '
               f'ИИ-ассистенты, веб-сервисы, презентации и дизайн. Каждый открывается и работает.">', s, count=1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://ysdprojects.space/">', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{n} работ YSD DEV онлайн">', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">',
               '<meta property="og:description" content="Не скриншоты, а работающие проекты: сайты, магазины, боты, презентации. Откройте любой.">', s, count=1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://ysdprojects.space/">', s, count=1)
    s = re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema.org","@type":"FAQPage".*?</script>', "", s, count=1, flags=re.S)
    s = s.replace('"url":"https://ysddev.com/","inLanguage"', '"url":"https://ysdprojects.space/","inLanguage"')

    # --- ссылки на разделы, которых здесь нет, — на основной сайт
    for a in ("prices", "reviews", "faq", "brief", "about"):
        s = s.replace(f'href="#{a}"', f'href="{SITE}/#{a}"')
    s = re.sub(r'href="/(?!/)([^"]*)"', lambda m: f'href="{SITE}/{m.group(1)}"'
               if not m.group(1).startswith(("fonts/", "favicon", "icon-", "apple-touch", "site.webmanifest")) else m.group(0), s)
    s = cut(s, '<div class="lang"', "</div>")  # без переключателя RU/EN: подписи работ только на русском

    # --- первый экран: про работы
    s = sub1(s, '<span data-i="status">Приём заявок открыт</span>', f"<span>{n} {pl(n, 'проект', 'проекта', 'проектов')} онлайн</span>")
    s = sub1(s, '<span class="stroke" data-i="h1b">под ключ.</span>', '<span class="stroke">онлайн.</span>')
    s = re.sub(r'<span class="h1s" data-i="h1a">.*?</span></h1>',
               f'<span class="h1s">{n} живых проектов студии YSD DEV — откройте любой и покликайте</span></h1>', s, count=1, flags=re.S)
    s = re.sub(r'<p class="lead" data-i="sub">.*?</p>',
               '<p class="lead">Не скриншоты, а работающие сайты, магазины, боты и презентации: посчитайте в калькуляторе, '
               'положите товар в корзину, пройдите сценарий бота. Так будет выглядеть и ваш проект.</p>', s, count=1, flags=re.S)
    s = re.sub(r'<div class="cta">.*?</div><div class="qs">',
               '<div class="cta"><a class="btn" href="#works"><span>Смотреть работы</span></a>'
               f'<a class="btn ghost" href="{SITE}/#brief">Заказать проект</a></div><div class="qs">', s, count=1, flags=re.S)
    qs = [("site", "Сайты"), ("shop", "Интернет-магазины"), ("bot", "Telegram-боты"), ("ai", "ИИ-ассистенты"),
          ("software", "Веб-сервисы"), ("deck", "Презентации"), ("design", "Дизайн")]
    s = re.sub(r'<div class="qs">.*?</div>',
               '<div class="qs"><span>Сразу к разделу:</span>' + "".join(f'<a href="#works" data-go="{k}">{t}</a>' for k, t in qs) + "</div>",
               s, count=1, flags=re.S)
    stats = [(n, pl(n, "работа онлайн", "работы онлайн", "работ онлайн")),
             (cnt["site"] + cnt["shop"], "сайтов и магазинов"),
             (cnt["bot"] + cnt["ai"], "ботов и ИИ-ассистентов"),
             (cnt["software"] + cnt["deck"] + cnt["design"], "сервисов, презентаций и дизайна")]
    s = re.sub(r'<div class="stats">.*?</div></div></section>',
               '<div class="stats">' + "".join(f"<div><b>{v}</b><small>{t}</small></div>" for v, t in stats) + "</div></div></section>",
               s, count=1, flags=re.S)

    # --- раздел работ: все сразу, с подписями
    s = sub1(s, '<h2 class="r" data-i="w-h">100 работ<br>в портфолио</h2>', f'<h2 class="r">{n} работ<br>в портфолио</h2>')
    s = re.sub(r'<p class="lead r" data-i="w-l">.*?</p>',
               '<p class="lead r">Нажмите на работу — откроется крупно с описанием. «Открыть проект» — живой сайт, бот или презентация '
               'в новой вкладке.</p>', s, count=1, flags=re.S)
    s = s.replace("var LIM = 12, wAll = false;", "var LIM = 12, wAll = true;")
    s = sub1(s, 'cur = b.dataset.k; wAll = false;', 'cur = b.dataset.k; wAll = true;')
    s = sub1(s, "'srcset=\"' + srcset(i, [400, 800, 1200, 1920]) + '\" src=\"' + pic(i, 400) + '\" onerror=\"YSD.fix(this)\"></div>' +",
             "'srcset=\"' + srcset(i, [400, 800, 1200, 1920]) + '\" src=\"' + pic(i, 400) + '\" onerror=\"YSD.fix(this)\"></div>' +\n"
             "'<figcaption class=\"cap\"><b>' + nm + '</b><span>' + (lang === \"en\" ? w.se : w.s) + '</span></figcaption>' +")
    s = sub1(s, "</style>", ".cap{display:grid;gap:4px;padding:14px 2px 6px;text-align:left}"
             ".cap b{font-size:16px;font-weight:600;line-height:1.3;color:#f3f3f6}"
             ".cap span{font-size:14px;line-height:1.45;color:rgba(243,243,246,.6)}"
             ".qs a[data-go]{cursor:pointer}</style>")

    # --- слова на первом экране и в бегущей строке — про виды работ
    s = re.sub(r'var ROT = \{ru:\[[^\]]*\]', 'var ROT = {ru:["Сайты", "Интернет-магазины", "Telegram-боты", "ИИ-ассистенты", '
               '"Mini App", "CRM и веб-сервисы", "Презентации", "Логотипы и дизайн"]', s, count=1)
    s = re.sub(r'var TICK = \{\s*ru: \[[^\]]*\]', 'var TICK = { ru: ["Калькуляторы","Корзина и оплата","Онлайн-запись",'
               '"Подбор по VIN","Telegram-боты","ИИ-ассистенты","CRM","Mini App","Презентации","Дизайн"]', s, count=1)

    # --- убрать разделы студии: цены, отзывы, вопросы, заявку, о студии и ИИ-помощника
    # не вырезаем, а прячем: скрипт основного сайта ищет форму заявки, цены и отзывы и падает без них
    i = s.index('<section id="prices"'); j = s.index("</main>", i)
    s = s[:i] + '<div hidden aria-hidden="true" class="studio-only">' + s[i:j] + "</div>" + s[j:]
    s = cut(s, '<button class="ai-launch"', "</button>")
    s = cut(s, '<section class="ai"', "</section>")

    # быстрые ссылки первого экрана включают фильтр
    s = sub1(s, "</body>", "<script>document.querySelectorAll('.qs a[data-go]').forEach(function(a){a.addEventListener('click',"
             "function(){var b=document.querySelector('#filters button[data-k=\"'+a.dataset.go+'\"]');if(b)b.click();})});</script></body>")

    (HOME / "index.html").write_text(s, encoding="utf-8")
    (HOME / "works.json").write_text(json.dumps([{k: w[k] for k in ("c", "t", "s", "g", "f", "u") if k in w} for w in works],
                                                ensure_ascii=False, indent=1), encoding="utf-8")
    # картинки работ и шрифт — с основного сайта
    (HOME / "img").mkdir(exist_ok=True)
    for w in works:
        for size in (400, 800, 1200, 1920):
            shutil.copy(src_dir / "img" / f"{w['f']}-{size}.webp", HOME / "img" / f"{w['f']}-{size}.webp")
    (HOME / "fonts").mkdir(exist_ok=True)
    shutil.copy(src_dir / "fonts" / "onest.woff2", HOME / "fonts" / "onest.woff2")
    for f in ("icon-96.png", "icon-192.png", "site.webmanifest"):
        if (src_dir / f).exists():
            shutil.copy(src_dir / f, HOME / f)
    print("работ:", n, dict(cnt))


if __name__ == "__main__":
    build(Path(sys.argv[1] if len(sys.argv) > 1 else "../ysddev.github.io"))
