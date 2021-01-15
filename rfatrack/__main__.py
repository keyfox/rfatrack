#!/usr/bin/env python3

import requests

from . import rfatweets
from .config import (
    RFATRACK_SPREADSHEET_ENDPOINT,
    RFATRACK_PROGRESS_FILE_PATH,
    RFATRACK_ACCOUNT_SCREEN_NAME,
)
from .twitter import iterate_tweets
from .progress import load_progress, save_progress


def post_to_spreadsheet(endpoint, payload):
    with requests.post(endpoint, json=payload, allow_redirects=True) as res:
        return res.json()


def track_rfatweets(screen_name, since_id):
    tweets = []
    max_id = None
    for t in iterate_tweets(screen_name, since_id=since_id):

        max_id = max(max_id or 0, t.id)

        if not rfatweets.is_rfatweet(t):
            continue

        tweets.append(t)
    return max_id, reversed(tweets)


def main():

    progress = load_progress(
        RFATRACK_PROGRESS_FILE_PATH, lambda: {"newest_fetched": None}
    )
    max_id, tweets = track_rfatweets(
        RFATRACK_ACCOUNT_SCREEN_NAME, since_id=progress["newest_fetched"]
    )
    if max_id is not None:
        for record in map(rfatweets.to_logrecord, tweets):
            post_to_spreadsheet(RFATRACK_SPREADSHEET_ENDPOINT, record)
        progress["newest_fetched"] = max_id
    save_progress(progress, RFATRACK_PROGRESS_FILE_PATH)


if __name__ == "__main__":
    main()
