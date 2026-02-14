#trend_fetch.py

from ai_trend_bot.mastodon_client import get_mastodon_client

def get_trending_topics(limit: int = 5) -> list[str]:
    """Return a list of top hashtags like ['#Python', '#AI']"""
    mastodon = get_mastodon_client()
    tags = mastodon.trending_tags(limit=limit)
    return [f"#{t['name']}" for t in tags]
