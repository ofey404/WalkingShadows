from typing import List, Optional, Type, Union

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings


class Settings(BaseSettings):
    url: str = "mongodb://localhost:27017"
    database_name: str = "test_database"

    class Config:
        env_prefix = "MONGODB_"


async def init(
    settings: Settings,
    document_models: Optional[List[Union[Type["DocType"], Type["View"], str]]] = None,
):
    client = AsyncIOMotorClient(settings.url)
    await init_beanie(
        database=client[settings.database_name], document_models=document_models
    )
