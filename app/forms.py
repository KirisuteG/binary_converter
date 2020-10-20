from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField
from wtforms.validators import DataRequired


class DecimalForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired('Please enter a valid integer number.')])

class FloatBinaryForm(FlaskForm):
    number = FloatField('Size',validators=[DataRequired('Please enter a valid float number.')])

class BinaryFloatForm(FlaskForm):
    sign = IntegerField('Sign', validators=[DataRequired('Please enter a valid binary number.')])
    exponent = IntegerField('exponent', validators=[DataRequired('Please enter a valid binary number.')])
    mantissa = IntegerField('exponent', validators=[DataRequired('Please enter a valid binary number.')])