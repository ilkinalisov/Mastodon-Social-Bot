from openai import OpenAI
import os
from dotenv import load_dotenv # <-- New Import!
from ai_trend_bot.config import POST_PROMPT # <-- New Import!
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # A type check that resolves circular import warning/error
    from ai_trend_bot.config import POST_PROMPT

# Load .env file *only if* it hasn't been loaded by the pipeline
# This makes the module testable and runnable outside the main pipeline
load_dotenv() 

# Instantiate a client
_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def generate_post(topic: str) -> str: # <-- Changed signature to accept 'topic'
    # Use the template from config.py
    prompt = POST_PROMPT.format(topic=topic)
    
    resp = _client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content