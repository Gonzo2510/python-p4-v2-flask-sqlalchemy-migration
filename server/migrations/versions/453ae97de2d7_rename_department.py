"""rename department

Revision ID: 453ae97de2d7
Revises: f1c66e7c5bf3
Create Date: 2024-02-25 20:37:47.505191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '453ae97de2d7'
down_revision = 'f1c66e7c5bf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###