import json
from pathlib import Path
from typing import Any, List, Optional

from fastapi import Depends
from langchain import OpenAI
from langchain.callbacks.manager import Callbacks
from langchain.schema import LLMResult
from services.world.settings import Settings, get_settings


def get_llm(
    settings: Settings = Depends(get_settings),
) -> OpenAI:
    return OpenAI(temperature=settings.openai.temperature)


class MockOpenAI(OpenAI):
    from_file: Path = None
    to_file: Path = None
    records: List[LLMResult] = []

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.from_file is not None:
            with open(self.from_file, "r") as f:
                records_json = json.load(f)
            self.records = [LLMResult.parse_obj(r) for r in records_json]

    def __del__(self):
        if self.to_file is not None:
            json_str = json.dumps(
                [r.dict() for r in self.records],
                ensure_ascii=False,
            )
            with open(self.to_file, "w") as f:
                f.write(json_str)

    def generate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        callbacks: Callbacks = None,
    ) -> LLMResult:
        """Run the LLM on the given prompts."""
        print("MockOpenAI._generate")
        if self.from_file is not None:
            result = self.records.pop(0)
            return result
        result = super().generate(prompts, stop, callbacks)
        if self.to_file is not None:
            self.records.append(result)
        return result

    async def agenerate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        callbacks: Callbacks = None,
    ) -> LLMResult:
        """Run the LLM on the given prompts."""
        if self.from_file is not None:
            result = self.records.pop(0)
            return result
        result = await super().agenerate(prompts, stop, callbacks)
        if self.to_file is not None:
            self.records.append(result)
        return result
