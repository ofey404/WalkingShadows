import connexion
from flask_cors import CORS
from schema import Config, Secret, ServiceContext
from flask import current_app
from logging.config import dictConfig
from pathlib import Path

_BACKEND_DIR = Path(__file__).parent
_API_YAML = _BACKEND_DIR / "api.yml"


def create_app(
    conf: Config,
    secret: Secret,
) -> connexion.FlaskApp:
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

    app = connexion.App(__name__, specification_dir="./")
    app.add_api(_API_YAML)

    CORS(app.app)

    with app.app.app_context():
        current_app.ctx = ServiceContext(config=conf, secret=secret)

    return app
