#!/usr/bin/env bash
# set -x             # for debug
set -euo pipefail  # fail early
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "$PROJECT_ROOT"

pushd src/frontend > /dev/null
    echo "## $(date +%c) Starting frontend... ##" | tee -a "$PROJECT_ROOT"/frontend.log
    yarn run dev 2>&1 | tee -a "$PROJECT_ROOT"/frontend.log
popd > /dev/null

