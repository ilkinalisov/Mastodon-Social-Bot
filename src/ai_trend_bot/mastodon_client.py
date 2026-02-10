# src/ai_trend_bot/mastodon_client.py
import datetime
from mastodon import Mastodon
from ai_trend_bot.config import MASTODON_TOKEN, MASTODON_API_BASE_URL

# instantiate once with env-loaded creds
mastodon = Mastodon(
    access_token=MASTODON_TOKEN,
    api_base_url=MASTODON_API_BASE_URL
)


def has_posted_today() -> bool:
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
    if len(text) > 500:
        text = text[:497] + "…"  
    mastodon.toot(text)

