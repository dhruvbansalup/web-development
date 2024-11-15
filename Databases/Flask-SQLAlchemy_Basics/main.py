import os
current_dir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__) #creating the Flask app
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(current_dir,"testdb.db") #setting the database URI


db=SQLAlchemy(app) #creating the database object
# db.init_app(app) #initializing the database object
app.app_context().push() #This is required to create the database
with app.app_context():
    db.create_all()

class User(db.Model): #creating the User table
    __tablename__="user"
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String,unique=True)
    email=db.Column(db.String,unique=True)

class Article(db.Model): #creating the Article table
    __tablename__="article"
    article_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String)
    content=db.Column(db.String)

    author_id=db.relationship('User',secondary="article_author")

class ArticleAuthors(db.Model): #creating the ArticleAuthors table
    __tablename__="article_author"
    article_id=db.Column(db.Integer,db.ForeignKey('article.article_id'),primary_key=True)
    author_id=db.Column(db.Integer,db.ForeignKey('user.user_id'),primary_key=True)

    user = db.relationship('User')
    article = db.relationship('Article')



@app.route("/",methods=["GET","POST"])
def articles():
    articles=Article.query.all()
    # articles=db.session.query(Article).all()

    return render_template("articles.html",articles=articles)


if __name__=="__main__":
    
    #Run the app
    app.run(
        host="0.0.0.0",
        debug=True,
        port=8080
    )
