#!/usr/bin/env bash
# set -x             # for debug
set -euo pipefail  # fail early
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "$PROJECT_ROOT"

bazel run -c dbg //src/backend/services/world:image -- --norun

echo "## Tag image as walkingshadows-world:latest ##"
docker tag bazel/src/backend/services/world:image ws-world:latest
