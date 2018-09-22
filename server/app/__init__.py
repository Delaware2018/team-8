from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
import bcrypt


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

    @app.route('/groups/<int:id>', methods=['GET'])
    def get_group(id, **kwargs):
        result = Group.query.filter_by(id=id).first()
        response = {
            'id' : result.id,
            'name' : result.name,
            'donated' : result.donated
        }
        return response



    @app.route('/user/register/', methods=['POST'])
    def register():
        f_name = request.args['firstname']
        l_name = request.args['lastname']
        password = request.args[b'password']
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        line_1 = request.args['line1']
        line_2 = request.args['line2']
        city = request.args['city']
        zipcode = request.args['zipcode']
        country = request.args['country']

        user = User(id=id)
        user.save()

        response = jsonify({
            'id': user.id,
            'firstname': user.f_name,
            'lastname': user.l_name,
            'password': user.hashed,
            'line1': user.line_1,
            'line2': user.line_2,
            'city': user.city,
            'zipcode': user.zipcode,
            'country': user.country,

        })
        response.status_code = 201
        return response

    @app.route('/', methods=['GET'])
    def main():
        return "Hello World"

    return app
