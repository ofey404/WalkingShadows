from flask import jsonify


def note(note):
    message = note.get("message")
    return jsonify({"message": f"message received: {message}"})
