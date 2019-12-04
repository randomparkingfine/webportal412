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
            'user':'hai32064fkjrmfsl',
            'password':'k0jmbqf380zmenkj',
            'host':'bfjrxdpxrza9qllq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            'port':'3306',
            'database':'czb69utqx3tir481',
        }
        self.conn = mysql.connector.connect(**self.config)
        curs = self.conn.cursor(buffered=True)
        curs.close()
        self.conn.close()
        #cursor.execute("CREATE TABLE assets (name TEXT)")
        

    def insert_asset(self, args):
    	self.conn = mysql.connector.connect(**self.config)
    	curs = self.conn.cursor(buffered=True)
    	curs.execute(query, args)
    	print(curs.execute("SHOW TABLES"))
    	curs.close()
    	self.conn.close()

    def select_query(self):
    	sql_select_query = "select * from assets"
    	self.conn = mysql.connector.connect(**self.config)
    	curs = self.conn.cursor(buffered=True)
    	curs.execute(sql_select_query)
    	records = curs.fetchall()
    	print("Total number of rows in assets is: ", curs.rowcount)
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
    		#args = (assest_num, nm, addr, phone, web, model, date_purch, price, expr, retired, descript, comments)
    		#database.insert_asset(args)

    else:
        return 'Method not supported', 400
    return render_template('index.html')

@app.route('/asset', methods=['GET', 'POST'])
def asset():
	info = {
		'manufacturer':'Asus',
		'asset_num': '1321',
		'manufacturer_Addr': '',
		'manu_Phone': '',
		'manuWeb': '',
		'model': '',
		'purchased_Date': '',
		'purchase_Price': '',
		'warrantyExpDate': '',
		'retired_Date': '',
		'description': '',
		'comments': '',
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