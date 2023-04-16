import inspect

from langchain import LLMChain, PromptTemplate
from langchain.llms import BaseLLM, OpenAI
from pydantic import BaseModel
from schema.config import Config, Secret
from schema.singleton import Singleton


class ServiceContext(BaseModel, Singleton):
    config: Config
    secret: Secret
    llm: BaseLLM
    chain: LLMChain


def new_service_context(
    config: Config,
    secret: Secret,
) -> ServiceContext:
    llm = OpenAI(
        openai_api_key=secret.openai_api_key,
        verbose=config.debug,
    )
    return _new_service_context_with_llm(
        config=config,
        secret=secret,
        llm=llm,
    )


def _new_service_context_with_llm(
    config: Config,
    secret: Secret,
    llm: BaseLLM,
) -> ServiceContext:
    """Create a new service context"""
    note_prompt = PromptTemplate(
        input_variables=["message"],
        template=inspect.cleandoc(
            """
            You're a philosopher in a cave, sitting beside a campfire.
            You're thinking about the meaning of life, as the fire crackles.
            Your friend comes up to you and give you a note, "{message}".
            
            What 5 high level insights can you infer from this note?
            (example format: insight (because of reason))
        """
        ),
    )
    return ServiceContext(
        config=config,
        secret=secret,
        llm=llm,
        chain=LLMChain(
            llm=llm,
            prompt=note_prompt,
            verbose=config.debug,
        ),
    )
