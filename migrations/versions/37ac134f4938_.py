"""empty message

Revision ID: 37ac134f4938
Revises: 7b3f1d6450ff
Create Date: 2020-06-18 10:58:42.966041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37ac134f4938'
down_revision = '7b3f1d6450ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'admins', 'users', ['user_id'], ['id'])
    op.add_column('branches', sa.Column('region_id', sa.Integer(), nullable=True))
    op.drop_constraint('branches_region_fkey', 'branches', type_='foreignkey')
    op.create_foreign_key(None, 'branches', 'regions', ['region_id'], ['id'])
    op.drop_column('branches', 'region')
    op.add_column('managers', sa.Column('branch_id', sa.Integer(), nullable=True))
    op.add_column('managers', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'managers', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'managers', 'branches', ['branch_id'], ['id'])
    op.add_column('regions', sa.Column('admin_id', sa.Integer(), nullable=True))
    op.drop_constraint('regions_admin_fkey', 'regions', type_='foreignkey')
    op.create_foreign_key(None, 'regions', 'admins', ['admin_id'], ['id'])
    op.drop_column('regions', 'admin')
    op.add_column('tellers', sa.Column('manager_id', sa.Integer(), nullable=True))
    op.add_column('tellers', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tellers', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'tellers', 'managers', ['manager_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tellers', type_='foreignkey')
    op.drop_constraint(None, 'tellers', type_='foreignkey')
    op.drop_column('tellers', 'user_id')
    op.drop_column('tellers', 'manager_id')
    op.add_column('regions', sa.Column('admin', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'regions', type_='foreignkey')
    op.create_foreign_key('regions_admin_fkey', 'regions', 'admins', ['admin'], ['id'])
    op.drop_column('regions', 'admin_id')
    op.drop_constraint(None, 'managers', type_='foreignkey')
    op.drop_constraint(None, 'managers', type_='foreignkey')
    op.drop_column('managers', 'user_id')
    op.drop_column('managers', 'branch_id')
    op.add_column('branches', sa.Column('region', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'branches', type_='foreignkey')
    op.create_foreign_key('branches_region_fkey', 'branches', 'regions', ['region'], ['id'])
    op.drop_column('branches', 'region_id')
    op.drop_constraint(None, 'admins', type_='foreignkey')
    op.drop_column('admins', 'user_id')
    # ### end Alembic commands ###
