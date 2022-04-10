#!/usr/bin/env python3
"""
Simple Notion Helper
"""
import requests
from config import Config

config = Config()

database_id = config.task_database_id
secret = config.secret


query_url = f"https://api.notion.com/v1/databases/{database_id}/query"


headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Authorization": f"Bearer {secret}"
}

payload = {
    "page_size": 100,
    #"filter": {
    #    "and" : [
    #        {
    #            "property" : "Done",
    #            "checkbox" : {
    #                "equals" : True,
    #            }
    #        },
    #        {
    #            "property" : "Next Due",
    #            "rich_text" : {
    #                "is_not_empty" : True,
    #            }
    #        },
    #        {
    #            "property" : "Next Due",
    #            "rich_text" : {
    #                "does_not_equal" : "Error in Recur Interval: Non-Whole or Negative Number"
    #            }
    #        }
    #    ]
    #}
}



response = requests.request("POST", query_url, json=payload, headers=headers)




out = response.json()
for task in out['results']:
    update_payload = {
    }
    print("Id " + task['id'])
    print("Archived " + str(task['archived']))
    print("Done " + str(task['properties']['Done']['checkbox']))
    print("Due " + str(task['properties']['Due']['date']))
    print("Next Due " + str(task['properties']['Next Due']))
    for content in task['properties']['Task']['title']:
        if content['type'] == 'text':
            print(content['text']['content'])
    print(task['properties']['Sub-Tasks'])
    print("###########")
