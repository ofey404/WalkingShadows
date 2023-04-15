import connexion
from flask_cors import CORS


app = connexion.App(__name__, specification_dir="./")
app.add_api("api.yml")

CORS(app.app)


def main():
    """main start the python web server"""
    app.run(debug=True)
