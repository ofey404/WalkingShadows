from typing import Optional
from schema.singleton import Singleton
from pydantic_yaml import YamlModel


class Config(YamlModel, Singleton):
    port: int = 5000
    debug: bool = True


class Secret(YamlModel, Singleton):
    openai_api_key: str
