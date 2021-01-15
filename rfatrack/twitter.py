import tweepy

from .config import (
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
)


def iterate_tweets(screen_name, since_id):
    # Create Twitter API
    auth = tweepy.OAuthHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
    )
    auth.set_access_token(
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET,
    )
    api = tweepy.API(auth)

    return tweepy.Cursor(
        api.user_timeline,
        screen_name=screen_name,  # RFATRACK_ACCOUNT_SCREEN_NAME,
        since_id=since_id,
    ).items()
