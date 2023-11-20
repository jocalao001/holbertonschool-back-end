#!/usr/bin/python3
"""Python script that, using a REST API and export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    u = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    t = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    user = requests.get(u)
    todo = requests.get(t)
    data = []
    for i in todo.json():
        new = [
            f"{user.json().get('id')}",
            f"{user.json().get('username')}",
            f"{i.get('completed')}",
            f"{i.get('title')}",
        ]
        data.append(new)
    with open(f"{argv[1]}.csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
