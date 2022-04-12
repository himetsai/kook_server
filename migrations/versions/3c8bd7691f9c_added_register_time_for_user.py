"""added register time for User

Revision ID: 3c8bd7691f9c
Revises: f9b21095f4bd
Create Date: 2022-04-05 14:18:36.361677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c8bd7691f9c'
down_revision = 'f9b21095f4bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registered_on', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'registered_on')
    # ### end Alembic commands ###
