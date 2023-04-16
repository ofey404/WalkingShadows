from __init__ import main
import argparse
from pathlib import Path

BACKEND_DIR = Path(__file__).parent
DEFAULT_CONFIG_DIR = BACKEND_DIR / "config"


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
        default=DEFAULT_CONFIG_DIR,
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    print(args)
    main()
