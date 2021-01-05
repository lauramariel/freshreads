from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def list_books():
    url="https://www.googleapis.com/books/v1/volumes?q=Liane%20Moriarty"
    content_type="application/json"
    headers={ "Content-type": f"{content_type}" }

    resp = requests.get(url, headers=headers)
    if resp.ok:
        titles = []
        results = json.loads(resp.text)

        for result in results.get("items"):
            titles.append(result.get("volumeInfo").get("title"))


    return render_template("index.html", titles=titles)