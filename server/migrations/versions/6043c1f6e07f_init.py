"""init

Revision ID: 6043c1f6e07f
Revises: 
Create Date: 2020-05-31 16:59:18.049261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6043c1f6e07f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tms', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('ip', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_server_ip'), 'server', ['ip'], unique=True)
    op.create_index(op.f('ix_server_name'), 'server', ['name'], unique=True)
    op.create_index(op.f('ix_server_tms'), 'server', ['tms'], unique=False)
    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tms', sa.DateTime(), nullable=True),
    sa.Column('id_server', sa.Integer(), nullable=True),
    sa.Column('agent', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_server'], ['server.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_report_tms'), 'report', ['tms'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_report_tms'), table_name='report')
    op.drop_table('report')
    op.drop_index(op.f('ix_server_tms'), table_name='server')
    op.drop_index(op.f('ix_server_name'), table_name='server')
    op.drop_index(op.f('ix_server_ip'), table_name='server')
    op.drop_table('server')
    # ### end Alembic commands ###
