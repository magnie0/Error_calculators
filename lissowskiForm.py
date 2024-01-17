from math import sqrt, ceil
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
#learned from https://www.youtube.com/watch?v=UIJKdCIEXUQ
class lissowski(FlaskForm):
    N = FloatField('N - liczebność próby',validators =[DataRequired()])
    b = FloatField('b - wartość procentową błędu pokrycia',validators =[DataRequired()])
    submit = SubmitField('Policz')

    def calculate(self):
        if self.N.data is not None and self.b.data is not None:
            N = self.N.data
            b = self.b.data
            #second *100 is for rounding to two decimal points 
            return ceil(((1/sqrt(N))+ (0.5*b/100.0)) *100.0 * 100.0 )/100.0
        return None