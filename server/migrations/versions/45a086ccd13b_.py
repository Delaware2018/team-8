"""empty message

Revision ID: 45a086ccd13b
Revises: 0c72e7294d6e
Create Date: 2018-09-22 02:39:16.618429

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '45a086ccd13b'
down_revision = '0c72e7294d6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('f_name', sa.String(length=100), nullable=True),
    sa.Column('l_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('line_1', sa.String(length=100), nullable=True),
    sa.Column('line_2', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('zipcode', sa.Integer(), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.Column('phone_number', sa.String(length=10), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.Column('personal_donations', sa.Integer(), nullable=True),
    sa.Column('income', sa.Integer(), nullable=True),
    sa.Column('bio', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('Users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Users_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('f_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('l_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('line_1', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('line_2', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('zipcode', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('country', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('date_joined', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('personal_donations', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('income', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bio', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Users_pkey'),
    sa.UniqueConstraint('email', name='Users_email_key')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
