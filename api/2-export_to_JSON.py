#!/usr/bin/python3
"""Python script that, using a REST API and export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    u = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    t = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    user = requests.get(u)
    todo = requests.get(t)
    data = []
    for i in todo.json():
        new = {
            "task": f"{i.get('title')}",
            "completed": i.get("completed"),
            "username": f"{user.json().get('username')}",
        }
        data.append(new)
    dicc = {f"{argv[1]}": data}
    with open(f"{argv[1]}.json", "w") as f:
        json.dump(dicc, f)
