from ensurepip import bootstrap
from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'h7uyG65gv67BHgbVbjB'

todos = [
    'Take a breakfast',
    'Take my kid to kindergarden',
    'Take a lunch',
    'Bring my kid from kindergarden',
    'Take a family time']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos':todos,
    }
    return render_template('hello.html', **context)
