from pydantic import BaseModel
from schema.config import Config, Secret
from schema.singleton import Singleton


class ServiceContext(BaseModel, Singleton):
    config: Config
    secret: Secret
