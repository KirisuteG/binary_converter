from flask import render_template, request
from app import app
from app.forms import DecimalForm, FloatBinaryForm, BinaryFloatForm
from functions import *

from flask import render_template, flash, redirect

@app.route('/')
@app.route('/decimal', methods=['GET', 'POST'])
def decimal():
    form = DecimalForm()
    notbinary = False
    if (form.validate_on_submit()):
        select1 = request.form.get('select1')
        select2 = request.form.get('select2')
        number = request.form['number']
        if(select1 == 'Decimal' and select2 == 'Binary'):
            result = decimalToBinary(number)
            return render_template('decimal.html',
                                    form=form,
                                    result=result, 
                                    notbinary=notbinary)
        else:
            if(select1 == 'Binary' and select2 == 'Decimal'):
                if(validate(number)):
                    result = binaryToDecimal(number)
                    return render_template('decimal.html',
                                            form=form, 
                                            result=result, 
                                            notbinary=notbinary)
                else:
                    notbinary = True
                    return render_template('decimal.html', 
                                            form=form, 
                                            result="", 
                                            notbinary=notbinary)
            else:
                if(select1 == 'Binary' and select2 == 'Binary'):
                    if(validate(number)):
                        return render_template('decimal.html', 
                                                form=form, 
                                                result=number, 
                                                notbinary=notbinary)
                    else:
                        notbinary = True
                        return render_template('decimal.html', 
                                                form=form, 
                                                result="", 
                                                notbinary=notbinary)
                else:
                    if(select1 == 'Decimal' and select2 == 'Decimal'):
                        return render_template('decimal.html', 
                                                form=form, 
                                                result=number, 
                                                notbinary=notbinary)
    return render_template('decimal.html', 
                            form=form, 
                            result="",
                            notbinary=notbinary) 

@app.route('/float', methods=['GET', 'POST'])
def float():
    form = FloatBinaryForm()
    form2 = BinaryFloatForm()
    notbinarysign = False
    notbinaryexponent = False
    notbinarymantissa = False

    if(form.validate_on_submit()):
        select1 = request.form.get('select1')
        number = request.form['number']
        if(select1 == 'Single'):
            result = floatToBinary(number, 'single')
            return render_template('float.html',
                                    form=form,
                                    form2=form2,
                                    notbinarysign=notbinarysign,
                                    notbinaryexponent=notbinaryexponent,
                                    notbinarymantissa=notbinarymantissa,
                                    result=result,
                                    result2="")
        else:
            if(select1 == 'Double'):
                result = floatToBinary(number, 'double')
                return render_template('float.html',
                                    form=form,
                                    form2=form2,
                                    notbinarysign=notbinarysign,
                                    notbinaryexponent=notbinaryexponent,
                                    notbinarymantissa=notbinarymantissa,
                                    result=result,
                                    result2="")
    

    if(form2.validate_on_submit()):
        sign = request.form['sign']
        exponent = request.form['exponent']
        mantissa = request.form['mantissa']
        select2 = request.form.get('select2')
        if(select2 == 'Single'):
            result2 = binaryToFloat(sign, exponent, mantissa, 'single')
            return render_template('float.html',
                                    form=form,
                                    form2=form2,
                                    notbinarysign=notbinarysign,
                                    notbinaryexponent=notbinaryexponent,
                                    notbinarymantissa=notbinarymantissa,
                                    result="",
                                    result2=result2)
        else:
            if(select2 == 'Double'):
                result2 = binaryToFloat(sign, exponent, mantissa, 'double')
                return render_template('float.html',
                                    form=form,
                                    form2=form2,
                                    notbinarysign=notbinarysign,
                                    notbinaryexponent=notbinaryexponent,
                                    notbinarymantissa=notbinarymantissa,
                                    result="",
                                    result2=result2)

    return render_template('float.html', 
                            form=form,
                            form2=form2,
                            notbinarysign=notbinarysign,
                            notbinaryexponent=notbinaryexponent,
                            notbinarymantissa=notbinarymantissa,
                            result="",
                            result2="")


