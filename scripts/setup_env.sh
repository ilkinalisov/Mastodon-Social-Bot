#setup_env.sh

#!/usr/bin/env bash

# 1. Create & activate venv
python3 -m venv .venv
source .venv/bin/activate

# 2. Install deps
pip install --upgrade pip
pip install -r requirements.txt

# 3. Copy .env
if [ ! -f .env ]; then
  cp .env.example .env
  echo "\nEdit .env with your API keys before running the bot."
fi
