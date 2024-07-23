"""recreate session table

Revision ID: 27c6a89db4d8
Revises: 6d8dd15127db
Create Date: 2024-06-01 11:45:02.739111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '27c6a89db4d8'
<<<<<<< HEAD
down_revision: Union[str, None] = '6d8dd15127db'
=======
down_revision: Union[str, None] = '6a4b319fae29'
>>>>>>> 6ccfcf3 (getting started with automated testing)
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'session',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('last_login', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('user_agent', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('ip', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('jwt_token', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('attemps', sa.INTEGER(), nullable=True),
        sa.Column('person_id', sa.INTEGER(), sa.ForeignKey('person.id'), nullable=False),
        sa.PrimaryKeyConstraint('id', name='session_pkey')
    )


def downgrade() -> None:
    op.drop_table('session')
