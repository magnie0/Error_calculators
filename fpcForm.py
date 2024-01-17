from math import sqrt, ceil
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
#learned from https://www.youtube.com/watch?v=UIJKdCIEXUQ
class fpc(FlaskForm):
    d = FloatField('d błąd oszacowania',validators =[DataRequired()])
    N = FloatField('N - wielkość populacji',validators =[DataRequired()])
    n = FloatField('n - wielkość próby',validators =[DataRequired()])
    submit = SubmitField('Policz')

    def calculate(self):
        if self.d.data is not None and self.N.data is not None and self.n.data is not None:
            d = self.d.data
            N = self.N.data
            n = self.n.data
            return ceil(d*sqrt((N-n)/(N-1)) *100.0)/100.0
        return None