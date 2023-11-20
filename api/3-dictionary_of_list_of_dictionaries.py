#!/usr/bin/python3
"""using a REST API and export all data in the JSON format"""
import json
import requests


if __name__ == "__main__":
    all_users = f"https://jsonplaceholder.typicode.com/users/"
    user = requests.get(all_users)
    dicc = {}
    for u in user.json():
        t = f"https://jsonplaceholder.typicode.com/users/{u.get('id')}/todos"
        todo = requests.get(t)
        data = []
        for i in todo.json():
            new = {
                "username": f"{u.get('username')}",
                "task": f"{i.get('title')}",
                "completed": i.get("completed"),
            }
            data.append(new)
        dicc[f"{u.get('id')}"] = data

    with open("todo_all_employees.json", "w") as f:
        json.dump(dicc, f)
