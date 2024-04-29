"""Serialize DataClass objects to native python data structures"""

from .data_class import DataClass


def serialize(obj: any, target_cls=dict) -> float | dict | list[dict]:
    """Serialize DataClass objects to native python data structures"""
    if isinstance(obj, list):
        return [serialize(sub, target_cls) for sub in obj]

    if isinstance(obj, DataClass):
        obj = obj.__dict__
        result = target_cls()
        for key in obj:
            result[key] = serialize(obj[key], target_cls)
        return result
    return obj
