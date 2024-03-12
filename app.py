from flask import Flask, jsonify
import os
from pathlib import Path
import frontmatter
from frontmatter.default_handlers import YAMLHandler
from slugify import slugify
from json import dumps


app = Flask(__name__)

article_path = "content/article"

def get_articles():
    articles = []
    for file_path in Path(article_path).rglob("*.md"):
        with open(file_path, "r", encoding="utf-8") as file:
            article = frontmatter.load(file, handler=YAMLHandler())
            articles.append({
                "title": article.get("title"),
                "content": article.content,
                "summary": article.get("summary", default=""),
                "slug": "/%s/%s" % ("article",slugify(article.get("title")))
            })

    return articles

@app.route("/api/articles", methods=["GET"])
def api_articles():
    articles = get_articles()
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
