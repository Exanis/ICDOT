from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired
from wtforms.fields.html5 import DateField

class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired(),
                                             Email(),
                                             EqualTo('email_confirm',message='Emails do not match')])
    email_confirm = StringField('Repeat Email',
                                validators=[DataRequired()])

    password = PasswordField('New Password', [InputRequired(),
                                              EqualTo('password_confirm', message='Passwords must match')])
    password_confirm  = PasswordField('Repeat Password')

    institute_name = StringField('Institute name', validators=[DataRequired()])

    department = StringField('Department or team name', validators=[DataRequired()])