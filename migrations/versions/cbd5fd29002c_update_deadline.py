"""update deadline

Revision ID: cbd5fd29002c
Revises: a398eeaf7d09
Create Date: 2025-01-15 10:28:59.444822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbd5fd29002c'
down_revision = 'a398eeaf7d09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.alter_column('deadline',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.alter_column('deadline',
               existing_type=sa.String(length=20),
               type_=sa.DATETIME(),
               existing_nullable=False)

    # ### end Alembic commands ###