from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder = 'templates')
app.secret_key = 'SOME KEY'

@app.route('/')
def index():
    return render_template('index.html', message='index')


@app.route('/set_data')
def set_data():
    session['name'] = 'Hasantha'
    session['other'] = 'Hello World'
    return render_template('index.html', message='Session data set')


@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message=f'Name: {name}, Other: {other}')
    else: 
        return render_template('index.html', message=f'No Session Found')


@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message='Session Cleared')


@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response


@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message=f'Cookie Value: {cookie_value}')


@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message='Cookie Removed'))
    response.set_cookie('cookie_name', expires=0)
    return response


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'testuser' and password == 'password':
            flash('Successful Login!')
            return render_template('index.html', message = 'Login Success')
        else:
            flash('Login Failed!')
            return render_template('login.html', message = 'Login Failed')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)