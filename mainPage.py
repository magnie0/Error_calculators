from flask import Flask, render_template, jsonify

from maxStandardErrorForm import maxStandardError
from maxStandardErrorFormSimplifiedForm import maxStandardErrorSimplified
from fpcForm import fpc
from lissowskiForm import lissowski
app = Flask(__name__) #flaskthen knows where to look for templates and static files

#without it error is RuntimeError: A secret key is required to use CSRF.
#also mentioned in https://www.youtube.com/watch?v=UIJKdCIEXUQ 16 minute explenation
app.config['SECRET_KEY'] = '1898a27ef0e1131a8433412d45b70b39'

@app.route('/', methods=['GET', 'POST']) #route on page
def index():
    return render_template('layout.html')

@app.route('/maxStandardError', methods=['GET', 'POST'])
def maxStandardErrorFunction():
    form2 = maxStandardError()
    if form2.validate_on_submit():
        result = form2.calculate()
        return jsonify({'error': result})
    return render_template('maxStandardErrorHtml.html', title = 'Maksymalny standardowy błąd', form=form2 )

@app.route('/maxStandardErrorSimplified', methods=['GET', 'POST'])
def maxStandardErrorFunctionSimplified():
    form2 = maxStandardErrorSimplified()
    if form2.validate_on_submit():
        result = form2.calculate()
        return jsonify({'error': result})
    return render_template('maxStandardErrorSimplifiedHtml.html', title = 'Uproszczony maksymalny standardowy błąd', form=form2 )

@app.route('/fpc', methods=['GET', 'POST'])
def fpcFunction():
    form2 = fpc()
    if form2.validate_on_submit():
        result = form2.calculate()
        return jsonify({'error': result})
    return render_template('fpcHtml.html', title = 'FPC', form=form2 )


@app.route('/lissowski', methods=['GET', 'POST'])
def lissowskiFunction():
    form2 = lissowski()
    if form2.validate_on_submit():
        result = form2.calculate()
        return jsonify({'error': result})
    return render_template('lissowskiHtml.html', title = 'Lissowski', form=form2 )



if __name__ == '__main__':
    app.run(debug=True)