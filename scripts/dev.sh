#!/usr/bin/env bash
# set -x             # for debug
set -euo pipefail  # fail early
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "$PROJECT_ROOT"

pushd src/frontend > /dev/null
    echo "## $(date +%c) Starting frontend... ##" | tee -a "$PROJECT_ROOT"/frontend.log
    yarn run dev 2>&1 | tee -a "$PROJECT_ROOT"/frontend.log &
popd > /dev/null

echo "## $(date +%c) Starting backend... ##" | tee -a "$PROJECT_ROOT"/backend.log
until bazel run //src/backend:backend_bin 2>&1 | tee -a "$PROJECT_ROOT"/backend.log
do
    echo "## Server would restart after 10 seconds... ##"  | tee -a "$PROJECT_ROOT"/backend.log
    sleep 10
done &

# On exit, kill the whole process group.
# https://stackoverflow.com/questions/360201/how-do-i-kill-background-processes-jobs-when-my-shell-script-exits
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

sleep infinity

