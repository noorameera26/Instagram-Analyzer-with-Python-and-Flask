from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, length

"""
Note:
- WTForms: library that provides flexible forms with validation & rendering library
- We can define the form fields in Python script and render them using an HTML template
- TextField: to represent the text field HTML form element
- Ref: https://www.analyticsvidhya.com/blog/2022/03/handling-forms-in-flask-with-flask-wtforms/
"""
class ValidateHashtag(Form):
    input_hashtag = TextField('Analyze', validators = [DataRequired(), length(min = 2)])