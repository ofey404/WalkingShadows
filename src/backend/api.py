from flask import jsonify, render_template


def note(note):
    message = note.get("message")
    return jsonify({"message": f"message received: {message}"})
