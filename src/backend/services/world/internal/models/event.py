from beanie import Document


class Event(Document):
    event_id: int
    description: str
