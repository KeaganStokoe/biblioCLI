import json
import os
import urllib.parse

import click
import requests
from dotenv import load_dotenv
from helper_functions import mapNotionResultToBook

load_dotenv()

token = os.environ["NOTION_KEY"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]
NOTION_URL = "https://api.notion.com/v1/databases/"


def addBookToDatabase(name, author, completed=False):
    url = f"https://api.notion.com/v1/pages"

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {"title": [{"text": {"content": name}}]},
            "Author": {"rich_text": [{"text": {"content": author}}]},
            "Goodreads link": {
                "url": urllib.parse.quote(
                    f"https://www.goodreads.com/search?utf8&query={name}",
                    safe=";/?:@&=+$,",
                )
            },
            "Completed": {"checkbox": completed},
        },
    }

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
        },
        data=json.dumps(payload),
    )

    if response.status_code == 200:
        click.echo(f'Successfully added "{name}" by "{author}" to the database.')
    else:
        click.echo(f'Failed to add "{name}" by "{author}" to the database.')
        click.echo(f"Here's the error message: {response.json()}")


def getBooks():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {token}", "Notion-Version": "2021-08-16"},
    )

    result_dict = r.json()
    book_list_result = result_dict["results"]

    for book in book_list_result:
        click.echo(mapNotionResultToBook(book))
