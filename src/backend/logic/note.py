from schema import ServiceContext


def note(ctx: ServiceContext, message: str) -> str:
    return f"message received: {message}, port: {ctx.config.port}"
