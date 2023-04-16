from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

article = Blueprint("article", __name__, url_prefix="/articles", static_folder="../static")

ARTICLES = {

    1: {"title": "title 1",
        "text": "text 1",
        "author": {
            "email": "name@email.com",
            "pk": 1,
        }
        },
    2: {"title": "title 2",
        "text": "text 2",
        "author": {
            "email": "name@email.com",
            "pk": 2,
        }
        },
    3: {"title": "title 3",
        "text": "text 3",
        "author": {
            "email": "name@example.com",
            "pk": 1,
        }
        },
}


@article.route("/")
@login_required
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route("/<int:pk>")
@login_required
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        raise NotFound(f"Article #{pk} doesn't exist!")

    return render_template('articles/details.html', article_name=article_name)
