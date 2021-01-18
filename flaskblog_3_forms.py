from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username            = StringField("Username",
                            validators=[DataRequired(), Length(min=2, max=20)])
    email               = StringField("Email",
                            validators=[DataRequired(), Email()])
    password            = PasswordField("Password",
                            validators=[DataRequired()])
    confirm_password    = PasswordField("Confirm Password",
                            validators=[DataRequired(), EqualTo('password')])
    submit              = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email               = StringField("Email",
                            validators=[DataRequired(), Email()])
    password            = PasswordField("Password",
                            validators=[DataRequired()])
    remember            = BooleanField("Remember")  # Jodi cookies hishebe egulo save korte chai
    submit              = SubmitField("Login")
