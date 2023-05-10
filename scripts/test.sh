#!/usr/bin/env bash
# set -x             # for debug
set -euo pipefail  # fail early
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "$PROJECT_ROOT"

if test -f .env; then
  source .env
fi

bazel test //src/backend/... \
           --test_env=OPENAI_API_KEY="${OPENAI_API_KEY}" \
           "$@"
