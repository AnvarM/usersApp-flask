from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField,PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddUser(FlaskForm):
    username = StringField('User name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteUser(FlaskForm):
    email = StringField('User email', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    new_email = StringField('New email', validators=[DataRequired()])
    submit = SubmitField('Submit')
