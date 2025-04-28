from flask import current_app as app
from flask import render_template, request, redirect, url_for, flash
from application.database import db
from application.models import User
from flask_login import LoginManager, login_user,login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "Please log in to access this page."
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
@login_required
def index():
   
    return f'Welcome {current_user.username}! <a href="/logout">Logout</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
