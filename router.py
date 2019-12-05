from datetime import datetime

import mysql.connector
import secrets
from flask import Flask, session
from flask_session import Session
from flask import request, redirect, url_for
from flask import render_template
from random import randint

query = "INSERT INTO  assets(asset_no, m_name, m_address, m_phone, m_website, model, purchase_date, price, exp_date, retire_date, description, comments) " \
        "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)


class DB:
    def __init__(self):
        # user: hai32064fkjrmfsl
        # pass: k0jmbqf380zmenkj
        # host: bfjrxdpxrza9qllq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com
        # port: 3306
        # dbname: czb69utqx3tir481

        self.config = {
            'user': 'hai32064fkjrmfsl',
            'password': 'k0jmbqf380zmenkj',
            'host': 'bfjrxdpxrza9qllq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            'port': '3306',
            'database': 'czb69utqx3tir481',
        }
        self.conn = mysql.connector.connect(**self.config)


    def search(self, **values):
        pass

    def insert_asset(self, values):
        # generate the format string we need to actually build the meme
        now = datetime.now().date()
        ins_str = 'INSERT INTO assets(asset_no, m_name, m_address,' \
                  'm_phone, m_website, model, purchase_date,' \
                  'price, exp_date, retire_date, description, comments)' \
                  'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor = self.conn.cursor()
        cursor.execute(ins_str, values)
        self.conn.commit()

    def delete(self, key):
        d_str = 'DELETE FROM assets WHERE asset_no=?'
        cursor = self.conn.cursor()
        cursor.execute(d_str, (key))
        self.conn.commit()

    def close(self):
        curs = self.conn.cursor(buffered=True)
        curs.close()
        self.conn.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        if request.form['submit'] == 'search':
            session['txtSearchAsset'] = request.form['txtSearchAsset']
            return redirect(url_for('asset'))
        else:
            database = DB()
            assest_num = request.form['txtAssetNumber']
            nm = request.form['txtManufacturerName']
            addr = request.form['txtManufacturerAddress']
            phone = request.form['txtManufacturerPhone']
            web = request.form['txtManufacturerWebPage']
            model = request.form['txtManufacturer']
            date_purch = request.form['txtDatePurchased']
            price = request.form['txtPurchasePrice']
            expr = request.form['txtExpirationDate']
            retired = request.form['txtRetiredDate']
            descript = request.form['txtDescription']
            comments = request.form['txtComments']
            args = (assest_num, nm, addr, phone, web, model, date_purch, price, expr, retired, descript, comments)
            database.insert_asset(args)

    else:
        return 'Method not supported', 400
    return render_template('index.html')


@app.route('/asset', methods=['GET', 'POST'])
def asset():
    database = DB()

    info = {
        'manufacturer': 'asdjfkl',
        'asset_num': 'shoothebox',
        'manufacturer_Addr': 'ads',
        'manu_Phone': 'adf',
        'manuWeb': 'adfs',
        'model': 'adf',
        'purchased_Date': 'dd',
        'purchase_Price': 'sss',
        'warrantyExpDate': 'dd',
        'retired_Date': 'ss',
        'description': 'ss',
        'comments': 'dd',
    }
    if request.method == 'POST':

        if request.form['submit'] == 'Update':
            return redirect(url_for('home'))

        elif request.form['submit'] == 'Return':
            return redirect(url_for('home'))

    return render_template('assets.html', data=info)


"""@app.route('/search', methods=['POST'])
def search():
    pass

@app.route('/delete', methods=['POST'])
def search():
    pass
"""

if __name__ == "__main__":
    app.run(debug=True)
