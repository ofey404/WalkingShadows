from pydantic import BaseSettings


class Settings(BaseSettings):
    api_key: str
    temperature: float = 0.9

    class Config:
        env_prefix = "OPENAI_"
