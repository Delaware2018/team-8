from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from flask_restful import Resource, reqparse


from instance.config import app_config

db = SQLAlchemy()


def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from app.models import Group
    from app.models import User
    from app.models import GroupUser

    @app.route('/groups/', methods=['POST', 'GET'])
    def groups():
        if request.method == "POST":
            name = request.args['name']
            donated = float(request.args['donated'])
            if name:
                group = Group(name = name)
                group.donated = donated
                group.save()
                response = jsonify({
                    'id': group.id,
                    'name': group.name,
                    'donated': group.donated
                })
                response.status_code = 201
            return response
        else:
            groups = Group.get_all()
            ret_list = []
            for group in groups:
                json_elm = {
                    'id' : group.id,
                    'name' : group.name,
                    'donated' : group.donated
            }
                ret_list.append(json_elm)
            response = jsonify(ret_list)
            response.status_code = 200
            return response

    @app.route('/groups/<int:id>/add/', methods=['POST'])
    def add_user_to_group(id, **kwargs):
        user_id = request.args['user_id']
        donated = float(request.args['donated'])
        new_group_user = GroupUser(group_id = id)
        new_group_user.user_id = user_id
        new_group_user.donated = donated
        new_group_user.save()
        response = ({
            'id' : new_group_user.id,
            'group_id' : new_group_user.group_id,
            'donated' : new_group_user.donated,
            'user_id' : new_group_user.user_id
        })
        return response

    @app.route('/groups/<int:id>', methods=['GET'])
    def get_group(id, **kwargs):
        result = Group.query.filter_by(id=id).first()
        response = jsonify({
            'id' : result.id,
            'name' : result.name,
            'donated' : result.donated
        })
        return response

    @app.route('/register/', methods=['POST'])
    def register():
        response = request.method
        return response

    @app.route('/', methods=['GET'])
    def main():
        return "Hello World"

    return app
