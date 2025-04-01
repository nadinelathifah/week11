from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import ValidationError, InputRequired

# Flask-WTF is a flask extension that integrates WTForms with flask.
# WTForms is a form-handling library for python.


# Created a generic custom functin that raises a Validation error when the input field is empty.
def fill_form_check(form, field):
    if len(field.data) <= 0:
        raise ValidationError('Field must be filled')

# Added function to every instance of Stringfield.
# RegisterForm class defines a form for student societ registration via FlaskForm.
# Validators are used to validate the data before submission.
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

# first_name, last_name etc. are instances of StringField, which is a class in WTForms that defines a text input field.
# HTML equivalent: 
#   <form method="POST" action="/your_submit_url">
#        <label for="first_name">Firstname</label>
#        <input type="text" id="first_name" name="first_name" class="form-control">

# SelectField is used to create a drop-down list of options in web form.
#   HTML equivalent: renders <select... and <option... HTML elements.