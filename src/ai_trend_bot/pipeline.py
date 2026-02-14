
import sys
from ai_trend_bot.mastodon_client import has_posted_today, post_to_mastodon
from ai_trend_bot.post_generator import generate_post
from ai_trend_bot.trend_fetch import get_trending_topics

def run_pipeline(dry_run: bool = False) -> dict:
    """
    Run the end-to-end bot pipeline.

    Returns a structured result for CLI/API callers.
    """
    if not dry_run and has_posted_today():
        return {
            "status": "skipped",
            "posted": False,
            "topic": None,
            "sarcastic_post": None,
            "message": "Already posted today; skipped publishing.",
        }

    topics = get_trending_topics(limit=5)
    topic = topics[0] if topics else "No trending topics"
    text = generate_post(topic)

    if dry_run:
        return {
            "status": "dry_run",
            "posted": False,
            "topic": topic,
            "sarcastic_post": text,
            "message": "Dry run completed. No post was sent to Mastodon.",
        }

    post_to_mastodon(text)
    return {
        "status": "posted",
        "posted": True,
        "topic": topic,
        "sarcastic_post": text,
        "message": "Posted successfully.",
    }


def main():
    result = run_pipeline(dry_run=False)
    if result["status"] == "skipped":
        print("Already posted today; exiting.")
        sys.exit(0)
    print("Posted successfully.")

if __name__ == "__main__":
    main()
