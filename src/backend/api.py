import connexion
import logic
from flask import current_app, jsonify
from schema import ServiceContext


def service_context() -> ServiceContext:
    with current_app.app_context():
        ctx: ServiceContext = current_app.ctx
        return ctx


def handle_note(req):
    ctx = service_context()
    message = req.get("message")
    answer = logic.note(ctx, message)

    return jsonify({"message": answer})
