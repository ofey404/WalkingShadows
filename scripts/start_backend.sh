#!/usr/bin/env bash
# set -x             # for debug
set -euo pipefail  # fail early
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "$PROJECT_ROOT"

echo "## $(date +%c) Starting backend... ##" | tee -a "$PROJECT_ROOT"/backend.log
until bazel run //src/backend:backend_bin 2>&1 | tee -a "$PROJECT_ROOT"/backend.log
do
    echo "## Server would restart after 10 seconds... ##"  | tee -a "$PROJECT_ROOT"/backend.log
    sleep 10
done
