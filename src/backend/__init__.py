import connexion
from flask_cors import CORS
from logging.config import dictConfig
from pathlib import Path

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

_BACKEND_DIR = Path(__file__).parent
_API_YAML = _BACKEND_DIR / "api.yml"

APP = connexion.App(__name__, specification_dir="./")
APP.add_api(_API_YAML)

CORS(APP.app)

SERVICE_CONTEXT = None

with APP.app.app_context():
    print("Initializing app...")


def main():
    """main start the python web server"""
    APP.run(debug=True)
