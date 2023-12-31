"""new Model

Revision ID: 7fe089462a34
Revises: 
Create Date: 2023-10-28 19:09:34.083008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fe089462a34'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('gambar', sa.Text(), nullable=True),
    sa.Column('stok', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
