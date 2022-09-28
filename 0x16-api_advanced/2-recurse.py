#!/usr/bin/python3
"""
Make recursive petitions to the Reddit API
"""

from requests import get


header = {
    'User-Agent': 'Linux:api_advanced:v0.0.0 (by /u/ElEnriquez)'
}


def recurse(subreddit, hot_list=[], after='nothing'):
    """
    Prints the titles of the hot posts listed for a given subreddit.
    recursively
    """

    base_url = 'https://www.reddit.com/r/{}/hot.json?after={}#'.format(
        subreddit, after)
    response = get(base_url, headers=header, allow_redirects=False)

    if (after is None):
        return

    if (response.status_code != 200):
        return (None)

    data = response.json().get('data')
    elements = data.get('children')
    iterate_children(elements, hot_list, 0)
    recurse(subreddit, hot_list, data.get('after'))

    return (hot_list)


def iterate_children(childrens, hotlist, counter=0):
    """
    Iterate over the childrens on the API
    """
    if (len(childrens) == counter):
        return

    hotlist.append(childrens[counter].get('data').get('title'))

    iterate_children(childrens, hotlist, counter + 1)
