from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1} + {number2} = {number1} + {number2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greetings' in request.args.keys() and 'name' in request.args.keys():
        greetings = request.args['greetings']
        name = request.args.get('name')
        return f'{greetings},{name}'
    else:
        return 'Some parameters are missing'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)