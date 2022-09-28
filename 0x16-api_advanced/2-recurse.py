#!/usr/bin/python3
"""Api Advance"""
import requests


def recurse(subreddit, hot_list=[], after='None'):
    """Recurse Function """
    url = "https://www.reddit.com/r/{}/hot.json?after={}#".format(
            subreddit, after)
    headers = {
            'User-Agent': "linux:Holberton:v1.0.0 (by /u/leslor)"
                }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if (after is None):
        return
    if response.status_code == 200:
        response = response.json().get('data')
        add(response, hot_list, size_hot_list=0)
        recurse(subreddit, hot_list, after)
    return None


def add(response, hot_list, size_hot_list=0):
    size_children = len(response.get('children'))
    if size_hot_list == size_children:
        return hot_list
    else:
        hot_list.append(response.get('children')[size_hot_list].get(
            'data').get('title'))
        return add(response, hot_list, size_hot_list + 1)
