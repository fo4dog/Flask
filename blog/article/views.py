from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint("article", __name__, url_prefix="/articles", static_folder="../static")

ARTICLES = {

    1: {"title": "title 1",
        "text": "text 1",
        "author": {
            "name": "Alice",
            "pk": 1,
        }
        },
    2: {"title": "title 2",
        "text": "text 2",
        "author": {
            "name": "Jon",
            "pk": 2,
        }
        },
    3: {"title": "title 3",
        "text": "text 3",
        "author": {
            "name": "Alice",
            "pk": 1,
        }
        },
}


@article.route("/")
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route("/<int:pk>")
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        raise NotFound(f"Article #{pk} doesn't exist!")

    return render_template('articles/details.html', article_name=article_name)
