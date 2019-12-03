from flask import Flask
from flask import request
from flask import render_template, url_for

@app.route('/', method=['GET'])
def home():
    if requeset.method == 'GET':
        return render_template('index')
    elif request.method == 'POST':
        pass
    else:
        return 'Method not supported', 400

