from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError
import email_validator
from model import User


class FormRegistration(FlaskForm):
    username = StringField('Usermame', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=20)])
    vegan = BooleanField('Vegan', validators=[DataRequired()])
    lactose = BooleanField('Lactose intolerant', validators=[DataRequired()])
    gluten = BooleanField('Gluten intolerant', validators=[DataRequired()])
    submit = SubmitField('Register')


