import argparse
from schema import Config, Secret
from __init__ import create_app, _BACKEND_DIR

_DEFAULT_CONFIG_DIR = _BACKEND_DIR / "config"


def parse_args():
    parser = argparse.ArgumentParser(
        description="""Start Walking Shadows Backend

    Example: python3 -m backend/__main__.py --config-dir backend/config/
    """,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-c",
        "--config-dir",
        help="Directory holding configuration files",
        default=_DEFAULT_CONFIG_DIR,
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()

    conf = Config.parse_file(args.config_dir / "config.yaml")
    secret = Secret.parse_file(args.config_dir / "secret.yaml")
    app = create_app(conf, secret)

    app.run(
        port=conf.port,
        debug=conf.debug,
    )
