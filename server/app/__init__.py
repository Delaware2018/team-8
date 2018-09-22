from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
import bcrypt
from flask_bcrypt import Bcrypt




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

    @app.route('/groups/create/', methods=['POST', 'GET'])
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
        user_emails = request.args['user_ids'].strip().split(",")
        selected_group = Group.query.filter_by(id=id).first()
        ret_list = []
        for user_email in user_emails:
            my_user = User.query.filter_by(id=user_email).first()
            if my_user:
                if ('donated' not in request.args):
                    donated = 0.00
                elif (len(ret_list) == 0 and 'donated' in request.args):
                    donated = float(request.args['donated'])
                new_group_user = GroupUser(group_id = id)
                new_group_user.user_id = my_user.id
                new_group_user.donated = donated
                new_group_user.save()
                selected_group.donated += donated
                selected_group.save()
                response = ({
                    'id' : new_group_user.id,
                    'group_id' : new_group_user.group_id,
                    'donated' : new_group_user.donated,
                    'user_id' : new_group_user.user_id
                })
                ret_list.append(response)
        return jsonify(ret_list)

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
        if 'firstname' in request.args:
            f_name = request.args['firstname']
        if 'lastname' in request.args:
            l_name = request.args['lastname']
        if 'email' in request.args:
            email = request.args['email']
        if 'password' in request.args:
            password = request.args['password']
            hashed = Bcrypt().generate_password_hash(password).decode()
        if 'line1' in request.args:
            line_1 = request.args['line1']
        if 'line2' in request.args:
            line_2 = request.args['line2']
        if 'city' in request.args:
            city = request.args['city']
        if 'state' in request.args:
            state = request.args['state']
        if 'zipcode' in request.args:
            zipcode = request.args['zipcode']
        if 'country' in request.args:
            country = request.args['country']

        user = User(email = email, password = hashed)
        user.save()

        response = jsonify({
            'id': user.id,
            'email' : user.email,
            'password' : user.password,
            'firstname': user.f_name,
            'lastname': user.l_name,
            'line1': user.line_1,
            'line2': user.line_2,
            'city': user.city,
            'state': user.state,
            'zipcode': user.zipcode,
            'country': user.country,
        })
        return response

    @app.route('/login/', methods=['POST'])
    def login():
        email = request.args['email']
        password = request.args['password']
        my_user = User.query.filter_by(email=email).first()
        if (my_user.password_is_valid(password)):
            response = jsonify({
                'id': my_user.id,
                'email' : my_user.email,
                'password' : my_user.password,
                'firstname': my_user.f_name,
                'lastname': my_user.l_name,
                'line1': my_user.line_1,
                'line2': my_user.line_2,
                'city': my_user.city,
                'state': my_user.state,
                'zipcode': my_user.zipcode,
                'country': my_user.country,
                'status_code' : 201
            })
            return response

        else:
            response = {'status_code' : 500}

        return response


    @app.route('/', methods=['GET'])
    def get_users():
        all_users = User.query.all()
        ret_list = []
        for user in all_users:
            user_groups = GroupUser.query.filter_by(user_id = user.id)
            json_elm = ({
                'id': user.id,
                'email' : user.email,
                'firstname': user.f_name,
                'lastname': user.l_name,
                'donated' : user.personal_donations,
                'groups': []
            })
            for group in user_groups:
                selected_group = Group.query.filter_by(id=group.group_id).first()
                temp_elm = {
                    'id' :selected_group.id,
                    'name' : selected_group.name,
                    'total_members' : len(GroupUser.query.filter_by(group_id = group.id).all()),
                    'donated' : selected_group.donated
                }
                json_elm['groups'].append(temp_elm)
            ret_list.append(json_elm)
        return jsonify(ret_list)


    return app
