from fastapi import Header
from types import SimpleNamespace


def get_current_user(x_role: str | None = Header(default="viewer")):
    """
    Mock authentication dependency
    """

    if x_role == "admin":
        return SimpleNamespace(id=1, role="admin")

    if x_role == "analyst":
        return SimpleNamespace(id=2, role="analyst")

    return SimpleNamespace(id=3, role="viewer")