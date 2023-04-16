from langchain.llms import BaseLLM
from pydantic import BaseModel
from schema.config import Config, Secret
from schema.singleton import Singleton


class ServiceContext(BaseModel, Singleton):
    config: Config
    secret: Secret
    llm: BaseLLM


def new_service_context(
    config: Config,
    secret: Secret,
) -> "ServiceContext":
    """Create a new service context"""
    return ServiceContext(
        config=config,
        secret=secret,
        llm=OpenAI(openai_api_key=secret.openai_api_key),
    )
