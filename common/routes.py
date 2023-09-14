from flask import Flask 
from controlers.site import home
from controlers.usersControler import (
                                       get_user, 
                                       get_user_all, 
                                       post_user, 
                                       patch_user, 
                                       put_user,
                                       delete_user
                                       )



def register_routes(app: Flask):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/users', 'users_all', get_user_all, methods=['GET'])
    app.add_url_rule('/users/<uuid:id>', 'users_id', get_user, methods=['GET'])
    app.add_url_rule('/users', 'users_post', post_user, methods=['POST'])
    app.add_url_rule('/users/<uuid:id>', 'users_patch', patch_user, methods=['PATCH'])
    app.add_url_rule('/users/<uuid:id>', 'users_put', put_user, methods=['PUT'])
    app.add_url_rule('/users/<uuid:id>', 'users_delete', delete_user, methods=['DELETE'])


