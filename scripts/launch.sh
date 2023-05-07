#!/usr/bin/env bash
# set -x             # for debug
set -euo pipefail  # fail early
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "$PROJECT_ROOT"

./scripts/build_image.sh

pushd src/deploy/local > /dev/null
  docker-compose up -d
popd > /dev/null
