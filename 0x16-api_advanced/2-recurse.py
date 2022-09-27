#!/usr/bin/python3
"""Api Advance"""
import requests


def recurse(subreddit, hot_list=[], size_hot_list=0):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent': "linux:Holberton:v1.0.0 (by /u/leslor)"
                }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json().get('data')
        size_children = len(response.get('children'))
        if size_hot_list == size_children:
            return hot_list
        else:
            hot_list.append(response.get('children')[size_hot_list].get(
                'data').get('title'))
            return recurse(subreddit, hot_list, size_hot_list+1)
    else:
        return None
