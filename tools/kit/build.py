"""python -m tools.kit.build detal bots.auto …  — собирает работы из tools/kit/<раздел>/<имя>.py в works/.
Без раздела — магазины (tools/kit/shops)."""
import importlib
import sys

from . import ai, app, bot, case, deck, shop

KITS = {"shops": shop, "bots": bot, "clients": shop, "slides": deck, "assist": ai, "apps": app, "design": case}

for name in sys.argv[1:]:
    part, _, mod_name = name.rpartition(".")
    part = part or "shops"
    mod = importlib.import_module(f"tools.kit.{part}.{mod_name}")
    d = KITS[part].build(mod.cfg())
    print("✓", d)
