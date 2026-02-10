#run_bot.sh

#!/usr/bin/env bash
# scripts/run_bot.sh

# 1) Make sure we use the venv’s Python
VENV_PYTHON="$(pwd)/.venv/bin/python"

# 2) Add `src/` so that `import ai_trend_bot` works
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# 3) Run your pipeline
$VENV_PYTHON -m ai_trend_bot.pipeline

