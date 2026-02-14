import os
from pathlib import Path
from typing import Optional
from dotenv import dotenv_values, load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOTENV_PATH = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path=DOTENV_PATH)
_DOTENV_VALUES = dotenv_values(DOTENV_PATH)

def _first_non_empty(*keys: str) -> Optional[str]:
    for key in keys:
        value = os.getenv(key)
        if value and value.strip():
            return value.strip()
    for key in keys:
        value = _DOTENV_VALUES.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


OPENAI_API_KEY = _first_non_empty("OPENAI_API_KEY")
MASTODON_TOKEN = _first_non_empty("MASTODON_TOKEN", "MASTODON_ACCESS_TOKEN")
MASTODON_API_BASE_URL = _first_non_empty("MASTODON_API_BASE_URL", "MASTODON_BASE_URL")

POST_PROMPT = (
    "Topic: {topic}\n"
    "Write a single post about this topic in a creative or sarcastic tone. "
    "Keep it under 280 characters and in English."
)
