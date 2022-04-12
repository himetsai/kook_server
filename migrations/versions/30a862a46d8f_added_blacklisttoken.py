"""added BlacklistToken

Revision ID: 30a862a46d8f
Revises: 3c8bd7691f9c
Create Date: 2022-04-10 17:29:14.151480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30a862a46d8f'
down_revision = '3c8bd7691f9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###