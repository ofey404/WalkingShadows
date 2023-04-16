from typing import List

from langchain.llms.fake import FakeListLLM
from schema import Config, Secret, ServiceContext
from schema.service_context import _new_service_context_with_llm


def fake_service_context(llm_responses: List[str]) -> ServiceContext:
    return _new_service_context_with_llm(
        config=Config(
            port=5000,
            debug=True,
        ),
        secret=Secret(
            openai_api_key="",
        ),
        llm=FakeListLLM(
            responses=llm_responses,
        ),
    )
