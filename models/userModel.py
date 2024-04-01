import uuid
from sqlalchemy.dialects.postgresql import UUID
from common.database import db
from common.marshmallow import add_schema

@add_schema
class Usuario(db.Model):
    __tablename__ = 'usuario'
    __table_args__ = {"schema": "dados"}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = db.Column(db.String, nullable=False)
    sobrenome = db.Column(db.String)
    cpf = db.Column(db.String(14), unique=True)
    sexo = db.Column(db.CHAR(1), db.CheckConstraint('sexo IN (\'F\', \'M\')'))


