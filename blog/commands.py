import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('init-db')
def init_db():
    # import models for creating tables

    db.create_all()


@click.command('create-init-user')
def create_init_user():
    from blog.user.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='name@example.com', name='Vladimir', password=generate_password_hash('test123'), is_staff=False)
        )
        db.session.commit()