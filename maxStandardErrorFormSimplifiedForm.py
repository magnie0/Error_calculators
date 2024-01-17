from math import sqrt, ceil
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
#learned from https://www.youtube.com/watch?v=UIJKdCIEXUQ
class maxStandardErrorSimplified(FlaskForm):
    n = FloatField('n - wielkość próby',validators =[DataRequired()])
    submit = SubmitField('Policz')

    def calculate(self):
        if self.n.data is not None:
            n = self.n.data
            #second *100 is for rounding to two decimal points 
            return ceil(1/sqrt(n)*100.0*100.0)/100.0
        return None