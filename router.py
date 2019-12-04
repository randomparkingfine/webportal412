import mysql.connector
import secrets
from flask import Flask, session
from flask_session import Session
from flask import request
from flask import render_template
from random import randint
from datetime import date, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)


class DB:
    def __init__(self):
        # user: hai32064fkjrmfsl
        # pass: k0jmbqf380zmenkj
        # host: bfjrxdpxrza9qllq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com
        # port: 3306
        # dbname: czb69utqx3tir481

        # NOTE: don't ever do this in ANY codebase(keeping passwords in code)
        # I'm doing it here to reduce cognitive load
        self.config = {
            'user':'hai32064fkjrmfsl',
            'password':'k0jmbqf380zmenkj',
            'host':'bfjrxdpxrza9qllq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            'port':'3306',
            'database':'czb69utqx3tir481',
        }
        self.conn = mysql.connector.connect(**self.config)

    def search(self, **values):
        pass

    def insert(self, values):
        # generate the format string we need to actually build the meme
        now = datetime.now().date()
        ins_str =   'INSERT INTO assets(asset_no, m_name, m_addess,' \
                    'm_phone, m_website, model, purchase_date,' \
                    'price, exp_date, retire_date, description, comments)' \
                    'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor = self.conn.cursor()

        cursor.execute(ins_str, values)

    def delete(self, key):
        d_str = 'DELETE FROM assets WHERE asset_no=?'
        cursor = self.conn.cursor()
        cursor.execute(d_str, (key))
        self.conn.commit()

    def close(self):
        self.conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        pass

    else:
        return 'Method not supported', 400

@app.route('/insert', methods=['POST'])
def insert():
    pass

@app.route('/search', methods=['POST'])
def search():
    '''
    Request parameters are found in request.form for forms btw
    '''
    pass

@app.route('/delete', methods=['POST'])
def delete():
    pass


if __name__ == "__main__":
    app.run()
    pass
