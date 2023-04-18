from pydantic import BaseModel
from schema import ServiceContext


class NoteRequest(BaseModel):
    message: str


class NoteResponse(BaseModel):
    message: str


def note(ctx: ServiceContext, req: NoteRequest) -> NoteResponse:
    return NoteResponse(message=ctx.chain.run(req.message))
