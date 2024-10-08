from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
    myvalue = 'NeuralNine'
    myresult = 10 + 20
    mylist = [10,20,30,40,50,60]
    return render_template('index.html', pass_1=myvalue, pass_2=myresult, pass_3=mylist)

@app.route('/filter')
def filter():
    some_text = 'Hello World'
    return render_template('filter.html', pass_some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1] # This is how you reverse string in python

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filter'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)