#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID"""
import json
import requests
from sys import argv


def writecsv():
    """Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
    url = 'https://jsonplaceholder.typicode.com/'

    USER_ID = int(argv[1])

    response_user = requests.get('{}users'.format(url))
    USERNAME = [i.get("username") for i in response_user.json()
                if i.get("id") == USER_ID][0]

    response_todos = requests.get('{}todos'.format(url))
    TASKS = [(i.get("title"), i.get("completed"))
             for i in response_todos.json()
             if i.get("userId") == USER_ID]
    data = {argv[1]: [{"task": i[0], "completed": i[1],
            "username": USERNAME} for i in TASKS]}

    file_name = '{}.json'.format(USER_ID)
    with open(file_name, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    writecsv()
