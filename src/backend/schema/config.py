from typing import Optional

from pydantic_yaml import YamlModel
from schema.singleton import Singleton


class Config(YamlModel, Singleton):
    port: int = 5000
    debug: bool = True


class Secret(YamlModel, Singleton):
    openai_api_key: str
