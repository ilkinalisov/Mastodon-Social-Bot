#test_trend_fetch.py

import pytest
from ai_trend_bot.trend_fetch import get_trending_topics

def test_get_trending_topics(monkeypatch):
    dummy = [{'name':'Python'}, {'name':'AI'}]
    class DummyMastodon:
        def trending_tags(self, limit):
            return dummy

    monkeypatch.setattr('ai_trend_bot.trend_fetch.get_mastodon_client', lambda: DummyMastodon())
    tags = get_trending_topics(limit=2)
    assert tags == ['#Python', '#AI']
