from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    user_ip = request.remote_addr
    return 'Hello World! Your IP is {}'.format(user_ip)
