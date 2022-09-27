#!/usr/bin/python3
import requests
"""Api Advance """


def top_ten(subreddit):
    """function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
            'User-Agent': "linux:Holberton:v1.0.0 (by /u/leslor)"
                }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json().get('data')
        for i in response.get('children'):
            print(i.get('data').get('title'))
    else:
        print("None")
        return
