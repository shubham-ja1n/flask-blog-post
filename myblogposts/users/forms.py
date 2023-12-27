from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed

from myblogposts.models import User

class LoginForm(FlaskForm):
    email = StringField("Enter Email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    email = StringField("Enter Email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter Password", validators=[DataRequired(), EqualTo('pass_confirm')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Register")
    
    def check_email(self, field):
        email = User.query.filter_by(email=field.data).first()
        if email:
            raise ValidationError("Your email has been already registered.")
    
    def check_username(self, field):
        username = User.query.filter_by(username=field.data).first()
        if username:
            raise ValidationError("Your username has been already registered.")
    
class UpdateForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    email = StringField("Enter Email", validators=[DataRequired(), Email()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    
    def check_email(self, field):
        email = User.query.filter_by(email=field.data).first()
        if email:
            raise ValidationError("Your email has been already registered.")
    
    def check_username(self, field):
        username = User.query.filter_by(username=field.data).first()
        if username:
            raise ValidationError("Your username has been already registered.")
    