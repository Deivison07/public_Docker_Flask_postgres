import json

from flask import request
from models.userModel import Usuario
from common.database import db

def get_user_all():
    schema = Usuario.Schema()
    rows = Usuario.query.all()
    return schema.dump(rows, many=True)

def get_user(id):
    schema = Usuario.Schema()
    user = Usuario.query.filter_by(id=id)
    if user:
        return schema.dump(user, many=True)
    return '', 404

def post_user():
    data = json.loads(request.data)
    try:
        new_user = Usuario(**data)
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return {
            'error': str(e)
        }, 402
    return '', 200

def put_user(id):
    #<-- implement code -->
    return patch_user(id)


def patch_user(id):
    user = Usuario.query.get(id)
    if user:
        for atributo, valor in json.loads(request.data).items():
            setattr(user, atributo, valor)
        db.session.commit()
        return '',200
    return '',404
        
def delete_user(id):
    user = Usuario.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return '', 200
    return '',404

