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

update_user_parser=reqparse.RequestParser()
update_user_parser.add_argument('email')


class userAPI(Resource):
    @marshal_with(user_output_fields)
    def get(self, username):
        user=db.session.query(User).filter(User.username==username).first()
        if user:
            #return valid json
            return user,200
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(user_output_fields)
    def post(self):
        #Use parser to get data
        args=create_user_parser.parse_args()
        username=args.get("username",None)
        email=args.get("email",None)
        
        # Validate imput data
        if username is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="username is required")
        if email is None:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="email is required")
        elif "@" not in email:
            raise BusinessValidationError(status_code=400,error_code="BE1003",error_message="email is invalid")

        #Check if user already exists
        user=db.session.query(User).filter((User.username==username)|(User.email==email)).first()

        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1004",error_message="Duplicate User")
        
        #add new user to database
        new_user=User(username=username,email=email)
        db.session.add(new_user)
        db.session.commit()

        return new_user,201
    
    def delete(self, username):
        #Check if user exists
        user=db.session.query(User).filter(User.username==username).first()
        
        if user is None:
            raise NotFoundError(status_code=404)
        
        #Check if there are articles for this user, if yes then throw error
        article=Article.query.filter(Article.authors.any(username=username)).first()
        
        if article:
            raise BusinessValidationError(status_code=400,error_code="BE1005",error_message="Can't Delete User as there are articles written by this user")
        
        #if no Dependency, then delete
        db.session.delete(user)
        db.session.commit()

        return "Successfully Deleted",200

    @marshal_with(user_output_fields)
    def put(self, username):
        # Use parser to get data
        args = update_user_parser.parse_args()
        new_email = args.get("email", None)

        # Validate input data
        if new_email is None:
            raise BusinessValidationError(status_code=400, error_code="BE1002", error_message="email is required")
        elif "@" not in new_email:
            raise BusinessValidationError(status_code=400, error_code="BE1003", error_message="email is invalid")

        # Check if same email already exists
        existing_email = db.session.query(User).filter(User.email == new_email).first()
        if existing_email:
            raise BusinessValidationError(status_code=400, error_code="BE1006", error_message="Duplicate Email ID")

        # Check if user exists
        user = db.session.query(User).filter(User.username == username).first()
        if user is None:
            raise NotFoundError(status_code=404)

        # Update user details
        user.email = new_email
        db.session.commit()

        return user, 200


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