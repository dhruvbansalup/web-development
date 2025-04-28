from flask import current_app as app
from application.database import db
from flask_migrate import Migrate
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    def verify_password(self, password):
        return self.password == password
    
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)
migrate.init_app(app, db)
