"""python -m tools.kit.build detal bots.auto …  — собирает работы из tools/kit/<раздел>/<имя>.py в works/.
Без раздела — магазины (tools/kit/shops)."""
import importlib
import sys

from . import ai, app, bot, case, deck, free, mapp, shop, site

KITS = {"shops": shop, "bots": bot, "clients": shop, "slides": deck, "assist": ai, "apps": app, "design": case, "sites": site, "free": free, "mapps": mapp}

for name in sys.argv[1:]:
    part, _, mod_name = name.rpartition(".")
    part = part or "shops"
    mod = importlib.import_module(f"tools.kit.{"free_works" if part == "free" else part}.{mod_name}")
    d = KITS[part].build(mod.cfg())
    print("✓", d)
