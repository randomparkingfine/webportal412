import secrets
from flask import Flask, session
from flask_session import Session
from flask import request
from flask import render_template
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        pass

    else:
        return 'Method not supported', 400

if __name__ == "__main__":
    app.run()
