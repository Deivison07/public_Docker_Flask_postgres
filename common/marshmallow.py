from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

def add_schema(cls):
    class Schema(SQLAlchemyAutoSchema):
        class Meta:
            model = cls
    cls.Schema = Schema
    return cls