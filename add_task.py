#!/usr/bin/env python3
"""
Simple Notion Helper to add Tasks
to Thomas Franks Notion Task Tools
"""
# pylint: disable=invalid-name
import sys


import requests
from config import Config

config = Config()

database_id = config.database_id
secret = config.secret


query_url = f"https://api.notion.com/v1/databases/{database_id}/query"


# Use of Sys Argv to keep the requirements simple

task_data = []

for param in sys.argv:
    if param == "-i":
        print("Enter/Paste Task. Ctrl-D to process")
        while True:
            try:
                line = input()
            except EOFError:
                break
            line = line.strip()
            if line.startswith('-'):
                task_data.append(line)

    if param == "-t":
        task_data.append(sys.argv[-1])
    if param == "-f":
        # pylint: disable = consider-using-with
        task_data = [x.strip() for x in open(sys.argv[-1], encoding='utf-8').readlines() \
                                                            if x.strip().startswith('-')]

if not task_data:
    print("No Taskdata Found")
    print("-i Paste Data to Program")
    print("-t Add as last Parameter (use quotes)")
    print("-f Specify Filename")
    sys.exit(1)


headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Authorization": f"Bearer {secret}"
}

query_url = "https://api.notion.com/v1/pages"

for task in task_data:
    # Format Task Name
    task_name = task.strip()
    if task_name.startswith('-'):
        # Hack needed cause of the 3 types of possible inputs
        task_name = task_name[1:]

    payload = {
        "parent" : {
            "type" : "database_id",
            "database_id": database_id,
        },
        "properties" : {
            "Task" : {
                "type": "title",
                "title": [
                  {"type": "text", "text": {"content": task_name }},
                ]
            },
            'Kanban Status': {
                'type': 'select',
                'select': {'color': 'red', 'name': 'To Do'},
            },
            'Priority': {
                'select': {'color': 'green', 'name': '🧀 Medium'},
            },
        }
    }
    response = requests.request("POST", query_url, json=payload, headers=headers)
    if config.debug:
        print(response.json())
