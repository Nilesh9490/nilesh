from flask import Flask, request, render_template
import socket
import sys
from flaskext.mysql import MySQL
import MySQLdb
import requests
app = Flask(__name__)

db = MySQLdb.connect(host="localhost", user="root", passwd="empire", db="blog_py")
cursor = db.cursor()
@app.route("/view")
def hello():
	return render_template('view.html')

@app.route("/hello", methods=['POST', 'GET'])
def create():
	first_name = request.form.get("firstname")
	last_name = request.form.get("lastname")
	email = request.form.get("email")
	blog = request.form.get("blog")
	sql = """INSERT INTO `blog`(`firstname`, `lastname`, `email`, `blog`) VALUES ( '%s','%s','%s','%s')""" % (first_name, last_name,email,blog)
	cursor.execute(sql)
	db.commit()
	db.close()
	return "sucess"

@app.route("/select")
def select():
	sql = """select * from `blog`"""
	cursor.execute(sql)
	data = cursor.fetchall()
	print str(data)
	# for i in data:
	# 	print i
	return str(data)
	# db.close()

@app.route("/update")
def update():


if __name__ == "__main__":
    app.run()