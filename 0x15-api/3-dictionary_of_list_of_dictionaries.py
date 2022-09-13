#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID"""
import json
import requests
from sys import argv


def writecsv():
    """Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
    url = 'https://jsonplaceholder.typicode.com/'
    response_user = requests.get('{}users'.format(url))
    response_todos = requests.get('{}todos'.format(url))

    USERNAME = [(i.get("username"), i.get("id")) for
                i in response_user.json()]
    TASKS = [(i.get("title"), i.get("completed"), i.get(
             "userId")) for i in response_todos.json()]

    data = {}
    for i in USERNAME:
        data[i[1]] = [{"username": i[0], "task": j[0],
                      "completed": j[1]} for j in TASKS if i[1] == j[2]]

    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    writecsv()
