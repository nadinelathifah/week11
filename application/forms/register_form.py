from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import ValidationError, InputRequired


def fill_form_check(form, field):
    if len(field.data) <= 0:
        raise ValidationError('Field must be filled')

class RegisterForm(FlaskForm):
    first_name = StringField('Firstname', validators=[InputRequired(), fill_form_check], render_kw={"class": "form-control"})
    last_name = StringField('Lastname', validators=[InputRequired(), fill_form_check], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[InputRequired(), fill_form_check], render_kw={"class": "form-control"})
    society = SelectField('Choose a Society:', choices=[
        ('', 'Choose a Society:'),
        ('1', 'Eat and Retreat'),
        ('2', 'Sci-Fi gee'),
        ('3', 'Clue Seekers'),
        ('4', 'Law'),
        ('5', 'Foreign Exchange')
    ], render_kw={"class": "form-control"})
    submit = SubmitField('SIGN UP', render_kw={"class": "btn btn-primary form-control-color"})