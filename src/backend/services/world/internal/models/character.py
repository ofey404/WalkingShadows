from typing import Any, Dict, List

from beanie import Document


class Character(Document):
    event_id: int
    name: str

    fact: List[Dict[str, Any]] = []
    memory: List[Dict[str, Any]] = []
    property: Dict[str, Any] = {}
