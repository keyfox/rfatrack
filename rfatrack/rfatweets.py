import requests
from datetime import timezone
import rfaparse

TARGET_HASHTAGS = {"リングフィットアドベンチャー", "RingFitAdventure", "NintendoSwitch"}


def is_rfatweet(tweet):
    # Check if the tweet has certain hashtags
    hashtags = {t["text"] for t in tweet.entities["hashtags"]}
    if hashtags != TARGET_HASHTAGS:
        return False

    # Check if a single image (supposed to be a screenshot of RFA) is attached
    if len(tweet.entities.get("media", [])) != 1:
        return False

    return True


def parse_rfatweet(tweet):
    media = tweet.entities["media"]
    image_url = media[0]["media_url_https"]

    with requests.get(image_url, stream=True) as f:
        # Download an image and parse it
        return rfaparse.parse_summary_screen(f.raw)


def to_logrecord(tweet):
    assert is_rfatweet(tweet)
    created_at = tweet.created_at.replace(tzinfo=timezone.utc)
    timestamp = created_at.timestamp()

    parsed = parse_rfatweet(tweet)

    return {
        **parsed.asdict(),
        "tweet_id": str(tweet.id),
        "timestamp": timestamp,
    }
