from schema.singleton import Singleton
from pydantic import BaseModel


class ServiceContext(BaseModel, metaclass=Singleton):
    openai_api_key: str

    def openai_api_key(self):
        return self.openai_api_key
