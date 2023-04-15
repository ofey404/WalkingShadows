from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/note", methods=["GET"])
def note():
    return jsonify({"message": "this is my message"})


"""Start the python web server"""


def main():
    app.run()
