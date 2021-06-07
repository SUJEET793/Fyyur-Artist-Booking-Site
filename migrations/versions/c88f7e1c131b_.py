"""empty message

Revision ID: c88f7e1c131b
Revises: 7b68a2158ddb
Create Date: 2021-05-31 16:46:09.777203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c88f7e1c131b'
down_revision = '7b68a2158ddb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('address', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'address')
    # ### end Alembic commands ###
