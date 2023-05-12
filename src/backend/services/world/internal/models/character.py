from typing import Any, Dict, List

import langchain.schema as schema
from services.world.internal.models.event import Event


class Character(Event):
    name: str

    fact: List[Dict[str, schema.Document]] = []
    memory: List[Dict[str, schema.Document]] = []
    property: Dict[str, Any] = {}
