from schema.singleton import Singleton
from pydantic import BaseModel
from schema.config import Config, Secret


class ServiceContext(BaseModel, Singleton):
    config: Config
    secret: Secret
