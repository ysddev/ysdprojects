"""python -m tools.kit.build detal mebel …  — собирает работы из tools/kit/shops/<имя>.py в works/."""
import importlib
import sys

from . import shop

for name in sys.argv[1:]:
    mod = importlib.import_module(f"tools.kit.shops.{name}")
    d = shop.build(mod.cfg())
    print("✓", d)
