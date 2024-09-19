"""Create Subscription table

Revision ID: 657c8a0aeaf0
Revises: 
Create Date: 2024-09-19 17:06:38.354231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '657c8a0aeaf0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('subscribed_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscription')
    # ### end Alembic commands ###
