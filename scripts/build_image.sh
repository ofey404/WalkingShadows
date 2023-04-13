#!/usr/bin/env bash
# set -x             # for debug
set -euo pipefail  # fail early
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "$PROJECT_ROOT"

bazel run -c dbg //src:src_image -- --norun

echo "## Tag image as walkingshadows:latest ##"
docker tag bazel/src:src_image walkingshadows:latest
