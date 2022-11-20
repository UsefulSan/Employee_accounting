"""empty message

Revision ID: 9b3f312a7f37
Revises: 26ea43681fd4
Create Date: 2022-11-20 16:27:53.817324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b3f312a7f37'
down_revision = '26ea43681fd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('phone', sa.String(length=20), nullable=True))
        batch_op.drop_column('Email')
        batch_op.drop_column('Phone')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Phone', sa.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('Email', sa.VARCHAR(length=100), nullable=True))
        batch_op.drop_column('phone')
        batch_op.drop_column('email')

    # ### end Alembic commands ###