#!/usr/bin/python3

import requests
from sys import argv


def gatherdata():
    """Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
    url = 'https://jsonplaceholder.typicode.com/'
    u_id = int(argv[1])
    EMPLOYEE_NAME = ""
    response_user = requests.get('{}users'.format(url))
    for i in response_user.json():
        if i.get("id") == u_id:
            EMPLOYEE_NAME = i.get("name")

    response_todos = requests.get('{}todos'.format(url))
    DONE_TASKS = [i.get("title") for i in response_todos.json()
                  if i.get("userId") == u_id and i.get("completed") is True]
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)

    TOTAL_NUMBER_OF_TASKS = 0
    response_todos = requests.get('{}todos'.format(url))
    for i in response_todos.json():
        if i.get("userId") == u_id:
            TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in DONE_TASKS:
        print("\t{}".format(i))


if __name__ == "__main__":
    gatherdata()
