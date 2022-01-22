def mapNotionResultToBook(result):
    # you can print result here and check the format of the answer.
    book_id = result["id"]
    properties = result["properties"]
    author = properties["Author"]["rich_text"][0]["text"]["content"]
    name = properties["Name"]["title"][0]["text"]["content"]
    completed = properties["Completed"]["checkbox"]

    return {"author": author, "name": name, "completed": completed, "book_id": book_id}


# For each book called by the API ("json_response_books"), reformat it to only return the title, author(s), and publisher. Return default data if any info is missing ("~XXX not available~") ...
def reformat_search(response):
    for item in response:
        try:
            title = item["volumeInfo"]["title"]
        except KeyError:
            title = "~Title not available]~"
        try:
            author = " & ".join(item["volumeInfo"]["authors"])
        except KeyError:
            author = "~Author not available~"
        try:
            publisher = item["volumeInfo"]["publisher"]
        except KeyError:
            publisher = "~Publisher not available~"
