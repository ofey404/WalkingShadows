from typing import Any, Dict, List

from services.world.internal.models.event import Event


class Character(Event):
    name: str

    fact: List[Dict[str, Any]] = []
    memory: List[Dict[str, Any]] = []
    property: Dict[str, Any] = {}
