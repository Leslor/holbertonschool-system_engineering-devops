#!/usr/bin/python3
"""Api Advance"""
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and
    returns the number of subscribers (not active
    users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'User-Agent': "linux:Holberton:v1.0.0 (by /u/leslor)"
                }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json().get('data').get('subscribers'))
    return 0
