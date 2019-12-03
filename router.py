from flask import Flask, session
from flask_session import Session
from flask import request
from flask import render_template

sesh = Session()

app = Flask(__name__)
sesh.init_app(app)


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
