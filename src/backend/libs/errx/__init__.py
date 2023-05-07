from typing import Any, Dict, Union

from pydantic import BaseModel


class HttpExceptionModel(BaseModel):
    detail: str


def add_to_openapi_doc(code_pair: Dict[int, str]) -> Dict[int, Dict[str, Any]]:
    return {
        code: {
            "description": detail,
            "model": HttpExceptionModel,
        }
        for code, detail in code_pair.items()
    }
