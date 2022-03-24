"""Create activities table

Revision ID: 6e0f50729083
Revises: 
Create Date: 2022-03-23 23:08:57.227180

"""
from alembic import op
from sqlalchemy import Integer, String, Column, SmallInteger, DECIMAL


# revision identifiers, used by Alembic.
revision = '6e0f50729083'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'activities',
        Column('id', Integer, primary_key=True),
        Column('name', String(100), nullable=False),
        Column('kind', String(50), nullable=False),
        Column('participants', SmallInteger, nullable=False),
        Column('price', DECIMAL(2), nullable=False)
    )


def downgrade():
    op.drop_table('activities')
