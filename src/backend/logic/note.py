from schema import ServiceContext


def note(ctx: ServiceContext, message: str) -> str:
    return ctx.chain.run(message)
