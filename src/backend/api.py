import logic
from flask import current_app, jsonify
from schema import ServiceContext


def service_context() -> ServiceContext:
    with current_app.app_context():
        ctx: ServiceContext = current_app.ctx
        return ctx


def handle_note(req):
    try:
        return jsonify(
            logic.note(
                service_context(),
                logic.NoteRequest.parse_obj(req),
            ).dict()
        )
    except Exception as e:
        return jsonify({"message": str(e)}), 500
