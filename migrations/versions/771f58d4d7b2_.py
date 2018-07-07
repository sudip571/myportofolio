"""empty message

Revision ID: 771f58d4d7b2
Revises: 
Create Date: 2018-07-07 10:21:20.672604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '771f58d4d7b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('mobileno', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('about_me', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_abouts_email'), 'abouts', ['email'], unique=True)
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=50), nullable=True),
    sa.Column('company_address', sa.String(length=50), nullable=True),
    sa.Column('start_date', sa.String(length=50), nullable=True),
    sa.Column('end_date', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_subject', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('email_body', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=True)
    op.create_table('portofolios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_title', sa.String(length=120), nullable=True),
    sa.Column('project_description', sa.String(length=1000), nullable=True),
    sa.Column('project_image_path', sa.String(length=200), nullable=True),
    sa.Column('technology_used', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skillcategories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('mobile_no', sa.String(length=50), nullable=True),
    sa.Column('about_me', sa.String(length=800), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_name', sa.String(length=100), nullable=True),
    sa.Column('skillcategory_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skillcategory_id'], ['skillcategories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skills')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('skillcategories')
    op.drop_table('portofolios')
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.drop_table('contacts')
    op.drop_table('companies')
    op.drop_index(op.f('ix_abouts_email'), table_name='abouts')
    op.drop_table('abouts')
    # ### end Alembic commands ###