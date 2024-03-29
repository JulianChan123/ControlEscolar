"""empty message

Revision ID: 68e1ebf4458e
Revises: 
Create Date: 2024-01-24 21:35:20.472831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68e1ebf4458e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombres', sa.String(length=50), nullable=True),
    sa.Column('apellidos', sa.String(length=50), nullable=True),
    sa.Column('matricula', sa.String(length=8), nullable=True),
    sa.Column('promedio', sa.Double(), nullable=True),
    sa.Column('fotoPerfilUrl', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profesor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombres', sa.String(length=50), nullable=True),
    sa.Column('apellidos', sa.String(length=50), nullable=True),
    sa.Column('numeroEmpleado', sa.Integer(), nullable=True),
    sa.Column('horasClase', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profesor')
    op.drop_table('alumno')
    # ### end Alembic commands ###
