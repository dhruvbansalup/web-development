from app import api
from application.database import db
from application.models import User
from flask_restful import fields, reqparse, Resource, marshal_with,abort
from flask_login import login_required

users_field = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
}

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username', type=str, required=True, help='Username cannot be blank')
create_user_parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
create_user_parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

class UserResource(Resource):
    @marshal_with(users_field)
    @login_required
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                abort(404, message="User not found")
            return user
        else:
            users = User.query.all()
            return users
        
    def post(self):
        args = create_user_parser.parse_args()
        if not args['password']:
            abort(400, message="Password cannot be empty")
        
        new_user = User(username=args['username'], email=args['email'], password=args['password'], is_active=True)
        existing_user = User.query.filter_by(email=args['email']).first()
        if existing_user:
            abort(400, message="User with this email already exists")
        
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201


api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')