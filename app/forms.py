from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField
from wtforms.validators import DataRequired

class IntegerForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired('Please enter a valid integer number.')])

class DecimalForm(FlaskForm):
    number = FloatField('Number', validators=[DataRequired('Please enter a valid integer number.')])

class FloatBinaryForm(FlaskForm):
    number = FloatField('Number')
    sign = IntegerField('Sign')
    exponent = IntegerField('Exponent')
    mantissa = IntegerField('Mantissa')

class BinaryFloatForm(FlaskForm):
    sign = IntegerField('Sign', validators=[DataRequired('Please enter a valid binary number.')])
    exponent = IntegerField('Exponent', validators=[DataRequired('Please enter a valid binary number.')])
    mantissa = IntegerField('Mantissa', validators=[DataRequired('Please enter a valid binary number.')])