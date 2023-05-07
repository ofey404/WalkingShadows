#!/usr/bin/env bash
# set -x             # for debug
set -euo pipefail  # fail early
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

SERVICE_ROOT="${SCRIPT_DIR}/.."

cd "$SERVICE_ROOT"

bazel run //src/backend/services/world:world_bin
