from typing import Optional

from pydantic_yaml import YamlModel


class Config(YamlModel):
    port: int = 5000
    debug: bool = True


class Secret(YamlModel):
    openai_api_key: str
