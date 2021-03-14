from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class ExampleForm(FlaskForm):
    select = SelectField('Select', choices=[
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three')
    ])
    submit = SubmitField('Go!')
