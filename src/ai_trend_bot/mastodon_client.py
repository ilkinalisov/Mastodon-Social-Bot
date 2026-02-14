# src/ai_trend_bot/mastodon_client.py
import datetime
from typing import Optional
from mastodon import Mastodon
from ai_trend_bot.config import MASTODON_TOKEN, MASTODON_API_BASE_URL

_mastodon: Optional[Mastodon] = None


def get_mastodon_client() -> Mastodon:
    global _mastodon
    if _mastodon is None:
        if not MASTODON_API_BASE_URL:
            raise RuntimeError(
                "API base URL is required. Set MASTODON_BASE_URL (or MASTODON_API_BASE_URL)."
            )
        if not MASTODON_TOKEN:
            raise RuntimeError(
                "Mastodon access token is required. Set MASTODON_ACCESS_TOKEN (or MASTODON_TOKEN)."
            )
        _mastodon = Mastodon(
            access_token=MASTODON_TOKEN,
            api_base_url=MASTODON_API_BASE_URL,
        )
    return _mastodon


def has_posted_today() -> bool:
    mastodon = get_mastodon_client()
    # use account_verify_credentials() to get your user id
    acct = mastodon.account_verify_credentials()
    statuses = mastodon.account_statuses(acct["id"], limit=1)
    if not statuses:
        return False
    last_date = statuses[0]["created_at"].date()
    return last_date == datetime.date.today()


def post_to_mastodon(text: str):
    """
    Publish a toot/status, truncated at 500 chars.
    """
    mastodon = get_mastodon_client()
    if len(text) > 500:
        text = text[:497] + "…"  
    mastodon.toot(text)
