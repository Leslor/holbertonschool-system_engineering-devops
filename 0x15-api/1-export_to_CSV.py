#!/usr/bin/python3
"""Python script to export data in the CSV format."""
import csv
import requests
from sys import argv


def writecsv():
    """Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
    url = 'https://jsonplaceholder.typicode.com/'

    USER_ID = int(argv[1])

    response_user = requests.get('{}users'.format(url))
    USERNAME = [i.get("name") for i in response_user.json()
                if i.get("id") == USER_ID][0]

    response_todos = requests.get('{}todos'.format(url))
    TASKS = [(i.get("title"), i.get("completed"))
             for i in response_todos.json()
             if i.get("userId") == USER_ID]
    data = [[USER_ID, USERNAME, i[0], i[1]] for i in TASKS]

    file_name = '{}.csv'.format(USER_ID)
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
    writecsv()
