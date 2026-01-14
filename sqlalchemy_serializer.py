"""Minimal drop-in replacement for sqlalchemy_serializer.SerializerMixin

This small helper provides a `SerializerMixin` with a `to_dict()` method
that inspects the SQLAlchemy model's table columns and returns a dict.
It's intentionally minimal to satisfy the tests without adding a dependency.
"""
from typing import Any, Dict


class SerializerMixin:
    def to_dict(self) -> Dict[str, Any]:
        table = getattr(self, "__table__", None)
        if table is None:
            # Fallback: try to use __dict__ filtering private attrs
            return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

        data: Dict[str, Any] = {}
        for col in table.columns:
            data[col.name] = getattr(self, col.name)
        return data
