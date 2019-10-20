from flask import Flask, render_template, request
from flask_mysqldb import MySQL

import os

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'high'
app.config['MYSQL_PASSWORD'] = 'high'
app.config['MYSQL_DB'] = 'high'

mysql = MySQL(app)

@app.route("/", methods=['GET','POST'])
def index():
	if request.method == "POST":
		details = request.form
		name = details['name']
		email = details['email']
		address = details['address']
		print(name,email,address)
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Users(name, email, address) VALUES (%s, %s, %s)", (name, email, address))
		mysql.connection.commit()
		cur.close()
		return render_template('layouts/index.html')
	return render_template('layouts/index.html')

app.run()