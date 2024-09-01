from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
    myvalue = 'NeuralNine'
    myresult = 10 + 20
    mylist = [10,20,30,40,50,60]
    return render_template('index.html', pass_1=myvalue, pass_2=myresult, pass_3=mylist)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)