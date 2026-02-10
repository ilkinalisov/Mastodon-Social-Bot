#config.py

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Mastodon
MASTODON_TOKEN      = os.getenv("MASTODON_TOKEN")
MASTODON_API_BASE_URL = os.getenv("MASTODON_API_BASE_URL")

# Prompt template
POST_PROMPT = (
    "Topic: {topic}\n"
    "Write a single post about this topic in a creative or sarcastic tone. "
    "Keep it under 280 characters and in English."
)
