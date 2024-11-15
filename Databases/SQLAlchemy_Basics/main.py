import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import select

from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True,primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    aricles = relationship('Article', secondary='article_author')

class Article(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    content = Column(String)
    authors= relationship('User', secondary='article_author')

class ArticleAuthor(Base):
    __tablename__ = 'article_author'
    article_id = Column(Integer, ForeignKey('article.article_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)

    user = relationship('User')
    article = relationship('Article')


#dialect+driver://username:password@host:port/database

engine=create_engine('sqlite:///db1.db', echo=False)

if __name__ == '__main__':
   
     #Using engine to query the database
    stmt=select(User)
    print("---------------Querying User Table----------------")
    print(stmt)

    with engine.connect() as conn:
        print("--------------------RESULT--------------------")
        result=conn.execute(stmt)
        for row in result:
            print(row)

    #Using session to query the database
    with Session(engine) as session:
        print("---------------Querying Articles Table----------------")
        articles=session.query(Article).filter(Article.article_id==1).all()
        print("------------------------RESULT------------------------")
        for article in articles:
            print("article:{}".format(article.title))
            for author in article.authors:
                print("author:{}".format(author.username))


    #Insert data in database using session
    print("-------------------ADDING DATA TO DATABASE-------------------")
    print("Give Artice title, content and author")
    t=input("Title:")
    c=input("Content:")
    a=input("Author ID:")
    with Session(engine,autoflush=False) as session:
        session.begin()
        try:
            article=Article(title=t,content=c)
            session.add(article)
            session.flush() #flush the session to get the primary key of the article (flush means to write the data to the database)
            print("------GETTING ARTICLE ID------")
            print("article ID={}".format(article.article_id))
            #Adding author to the article
            article_author=ArticleAuthor(article_id=article.article_id,user_id=a)
            session.add(article_author)
        except:
            print("-------------Error in adding data-------------")
            print("-----------Rolling back the session-----------")
            session.rollback()
            raise
        else:
            print("-----------Commiting the session-----------")
            session.commit()
            
