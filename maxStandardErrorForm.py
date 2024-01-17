from math import sqrt, ceil
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
#learned from https://www.youtube.com/watch?v=UIJKdCIEXUQ
class maxStandardError(FlaskForm):
    z = FloatField('z - poziom ufności  ',validators =[DataRequired()])
    p = FloatField('p - rozkład parametrów w populacji',validators =[DataRequired()])
    n = FloatField('n - wielkość próby',validators =[DataRequired()])
    submit = SubmitField('Policz')

    def calculate(self):
        if self.z.data is not None and self.p.data is not None and self.n.data is not None:
            z = self.z.data
            p = self.p.data
            n = self.n.data
            #second *100 is for rounding to two decimal points 
            return ceil(z*sqrt(p*(1-p)/n)* 100.0 *100.0)/100.0
        return None