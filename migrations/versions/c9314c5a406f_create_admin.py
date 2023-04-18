"""create admin

Revision ID: c9314c5a406f
Revises: 9ad9d007c52c
Create Date: 2023-04-18 23:40:23.876401

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.user.models import User

# revision identifiers, used by Alembic.
revision = 'c9314c5a406f'
down_revision = '9ad9d007c52c'
branch_labels = None
depends_on = None


def upgrade():
    db.session.add(
        User(email='admin@admin.com', name='admin', password=generate_password_hash('admin'), is_staff=True)
    )
    db.session.commit()


def downgrade():
    db.session.delete(
        User(email='admin@admin.com', name='admin', password=generate_password_hash('admin'), is_staff=True)
    )
    db.session.commit()
