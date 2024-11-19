from flask_restful import Resource
from flask_restful import fields,marshal_with
from flask_restful import reqparse

from application.database import db
from application.models import User, Article, ArticleAuthors
from application.validation import NotFoundError, BusinessValidationError

user_output_fields={
    "user_id":fields.Integer,
    "username":fields.String,
    "email":fields.String
}
article_output_fields = {
                    "article_id": fields.Integer,
                    "title": fields.String,
                    "content": fields.String
                }
article_author_output_fields = {
                    "article_id": fields.Integer,
                    "author_id": fields.Integer
                }


create_user_parser=reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')



class userAPI(Resource):
    @marshal_with(user_output_fields)
    def get(self, username):
        user=db.session.query(User).filter(User.username==username).first()
        if user:
            return user,200
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(user_output_fields)
    def post(self):
        args=create_user_parser.parse_args()
        username=args.get("username",None)
        email=args.get("email",None)

        if username is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="username is required")
        if email is None:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="email is required")
        elif "@" not in email:
            raise BusinessValidationError(status_code=400,error_code="BE1003",error_message="email is invalid")

        user=db.session.query(User).filter((User.username==username)|(User.email==email)).first()

        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1004",error_message="Duplicate User")
        
        new_user=User(username=username,email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user,201

    def put(self, username):
        pass
    def delete(self, username):
        pass



class AllTableViewAPI(Resource):
    def get(self, table):
        table_mapping = {
            'User': User,
            'user': User,
            'Article': Article,
            'article': Article,
            'ArticleAuthors': ArticleAuthors,
            'articleauthors': ArticleAuthors
        }
        table_class = table_mapping.get(table)
        if not table_class:
            return {"Error": "Invalid table name"}, 400

        table_data = db.session.query(table_class).all()
        if table_data:
            if table_class == User:
                return marshal_with(user_output_fields)(lambda: (table_data, 200))()
            elif table_class == Article:
                return marshal_with(article_output_fields)(lambda: (table_data, 200))()
            elif table_class == ArticleAuthors:
                return marshal_with(article_author_output_fields)(lambda: (table_data, 200))()
            else:
                return {"Error": "Invalid table class"}, 400    
        else:
            raise NotFoundError(status_code=404)