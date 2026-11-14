"""Общее для ИИ-ассистентов: сборка темы."""


def theme(**v) -> dict:
    base = {"rb": "14px", "rc": "22px", "rs": "30px", "hw": "700", "ht": "-.02em"}
    base.update(v)
    return base
