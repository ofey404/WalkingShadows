from http.client import HTTPException
from typing import Any, Dict, Union

from pydantic import BaseModel


class HttpExceptionModel(BaseModel):
    detail: str


def add_exception_to_openapi(*exceptions: HTTPException) -> Dict[int, Dict[str, Any]]:
    return {
        e.status_code: {
            "description": e.detail,
            "model": HttpExceptionModel,
        }
        for e in exceptions
    }
