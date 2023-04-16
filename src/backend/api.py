import connexion
from schema import ServiceContext
from flask import current_app
from flask import jsonify
import logic


def service_context() -> ServiceContext:
    with current_app.app_context():
        ctx: ServiceContext = current_app.ctx
        return ctx


def handle_note(req):
    ctx = service_context()
    message = req.get("message")
    answer = logic.note(ctx, message)

    return jsonify({"message": answer})
