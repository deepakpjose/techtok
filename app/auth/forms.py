from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()], render_kw={'class':'form-control', 'placeholder':'abc@example.com'})
    password = PasswordField('Password', validators=[Required()], render_kw={'class':'form-control', 'placeholder':'Password'})
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In', render_kw={'style':'background-color:#007bff', 'class':'form-control'})
