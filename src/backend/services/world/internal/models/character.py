from typing import Any, Dict, List

from beanie import Document


class Character(Document):
    akasha_id: str

    memory: List[Dict[str, Any]]
    property: Dict[str, Any]
    event: List[Dict[str, Any]]
