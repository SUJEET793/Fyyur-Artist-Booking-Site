"""empty message

Revision ID: 7b68a2158ddb
Revises: 606595e27819
Create Date: 2021-05-31 16:41:36.907201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b68a2158ddb'
down_revision = '606595e27819'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('phone', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('image_link', sa.String(length=500), nullable=True))
    op.add_column('Artist', sa.Column('facebook_link', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('address', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('phone', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('image_link', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('facebook_link', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'facebook_link')
    op.drop_column('Venue', 'image_link')
    op.drop_column('Venue', 'phone')
    op.drop_column('Venue', 'address')
    op.drop_column('Artist', 'facebook_link')
    op.drop_column('Artist', 'image_link')
    op.drop_column('Artist', 'genres')
    op.drop_column('Artist', 'phone')
    # ### end Alembic commands ###
