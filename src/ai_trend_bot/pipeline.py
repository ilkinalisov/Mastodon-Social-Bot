
# ... (imports)
# src/ai_trend_bot/pipeline.py
import sys
from ai_trend_bot.mastodon_client import has_posted_today, post_to_mastodon
from ai_trend_bot.post_generator import generate_post
from ai_trend_bot.trend_fetch import get_trending_topics

def main():
    if has_posted_today():
        print("❌ Already posted today; exiting.")
        sys.exit(0)

    topics = get_trending_topics(limit=5)
    topic = topics[0] if topics else "No trending topics"
    
    # This now passes the *topic* to the refactored function
    text  = generate_post(topic)          
    
    post_to_mastodon(text)
# ... (rest of the file)
    print("✅ Posted successfully.")

if __name__ == "__main__":
    main()
