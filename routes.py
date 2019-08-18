from flask import Flask, render_template, redirect, url_for, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from models import User
from forms import LoginForm, AddUser, DeleteUser, UpdateUser
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
import pymysql

connection = pymysql.connect(host='localhost', user='testuser', password='testpassword', db='testdb', charset='utf8mb4')
cursor = connection.cursor()
msg_restricted = "You need to have admin rights to perform this action"
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('users.html', users = users)

@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember = True)
        return redirect(url_for('users'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add_user')
@login_required
def add_user():
    if (current_user.role == 1):
        form = AddUser()
        return  render_template('add_user.html', form=form)
    else:
        return msg_restricted

@app.route('/delete_user')
@login_required
def delete_user_form():
    if (current_user.role == 1):
        form = DeleteUser()
        return  render_template('delete_user.html', form=form)
    else:
        return msg_restricted

@app.route('/update_user')
@login_required
def update_user_form():
    if (current_user.role == 1):
        form = UpdateUser()
        return  render_template('update_user.html', form=form)
    else:
        return msg_restricted

@app.route('/add_user', methods=['POST'])
@login_required
def post_user():
    if(current_user.role == 1):
        form = AddUser()
        user = User(request.form['username'], request.form['email'], request.form['password'], 2)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))
    else:
        return msg_restricted

@app.route('/delete_user', methods=['POST'])
@login_required
def delete_user():
    if(current_user.role == 1):
        form = DeleteUser()
        user = User.query.filter_by(email = request.form['email']).first()
        id = user.id
        sql = "DELETE FROM users where id = {}".format(id)
        cursor.execute(sql)
        connection.commit()
        return redirect(url_for('users'))
    else:
        return msg_restricted


@app.route('/update_user', methods=['POST'])
@login_required
def update_user():
    if(current_user.role == 1):
        form = UpdateUser()
        user = User.query.filter_by(email = request.form['email']).first()
        email = user.email
        new_email = request.form['new_email']
        sql = "UPDATE users set email = '{}' where email = '{}'".format(new_email, email)
        cursor.execute(sql)
        connection.commit()
        return redirect(url_for('users'))
    else:
        return msg_restricted