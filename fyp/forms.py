from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from fyp.models import User
from flask_login import current_user
class InsertForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    profession=SelectField('Profession', choices = [('teacher', 'Teacher'),('student', 'Student')])
    submit=SubmitField('Add Up')
    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Choose a different one')
    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Choose a different one')
class UpdateAccountForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    profession=SelectField('Profession', choices = [('techeacer', 'Teacher'),('student', 'Student')])
    submit=SubmitField('Update')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Choose a different one')
    def validate_email(self, email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Choose a different one')


class LoginForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')
