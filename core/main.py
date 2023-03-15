#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
MyManual - 2023 - por [jero98772,jhonmesa]
MyManual - 2023 - by [jero98772,jhonmesa]
"""
from flask import Flask, render_template, request, flash, redirect ,session
from .tools.dbInteracion import dbInteracion
from .tools.tools import *
from .constants_defines import *
app = Flask(__name__)
app.secret_key = str(enPassowrdHash(generatePassword()))

class webpage():
	WEBPAGE = "/"
	@app.route(WEBPAGE+"info.html")
	def info():
		return render_template("info.html")
	@app.route(WEBPAGE+"user_register.html", methods = ['GET','POST'])
	def register():
		if request.method == 'POST':
			pwd = request.form["pwd"]
			pwd2 = request.form["pwd2"]
			if pwd == pwd2 :
				usr = request.form["usr"]
				db = dbInteracion(DBNAMESQL)
				db.connect(LOGINTABLE)
				if db.userAvailable(usr,"usr") :
					encpwd = enPassowrdStrHex(pwd+usr) 
					db.saveUser(usr,enPassowrdStrHex(pwd))
					db.addtouchme()
					try:
						session['loged'] = True
						session['user'] = usr
						session['id'] = db.get_id()
						session['encpwd'] = encpwd
					except db.userError():
						return "invalid user , please try with other username and password"		
				else:
					return "invalid user , username have been taked"		
		return render_template("user_register.html")
	@app.route(WEBPAGE+"login.html", methods=['GET', 'POST'])
	def login():	
		usr = request.form['username']
		pwd = request.form["password"]
		encpwd = enPassowrdStrHex(pwd+usr)
		protectpwd = enPassowrdStrHex(pwd)
		db = dbInteracion(DBNAMESQL)
		db.connect(LOGINTABLE)
		if db.findUser(usr) and db.findPassword(protectpwd)  :
			session['loged'] = True
			session['user'] = usr
			session['encpwd'] = encpwd
			return redirect("/main.html")
		else:
			flash('wrong password!')
		return webpage.main()
	@app.route(WEBPAGE, methods = ['GET','POST'])
	@app.route(WEBPAGE+"main.html", methods = ['GET','POST'])
	def main():
		if not session.get('loged'):
			return render_template('login.html')	
		else:
			
			return render_template("main.html")	

	@app.route(WEBPAGE+"trustslevels.html",)
	def trustslevels():
		return render_template("trustslevels.html")	
	@app.route(WEBPAGE+"trustslevel1.html", methods = ['GET','POST'])
	def trustslevels1():
		#if request.method == "POST":
		return render_template("trustslevel1.html")	
	@app.route(WEBPAGE+"touchme.html", methods = ['GET','POST'])
	def touchme():
		if request.method == "POST":
			values=multrequest(PART_NAME)
			db = dbInteracion(DBNAMESQL)
			db.connect(PARTS_TABLE)
			db.insert(,PART_NAME,str(id)+values)
		return render_template("touchme.html",part_name=PART_NAME)	
	@app.route(WEBPAGE+'gas/actualisar<string:id>', methods = ['GET','POST'])
	def update(id):
		user = session.get('user')
		db = dbInteracion(DBNAMEGAS)
		db.connect(TABLEGAS+user)
		key = session.get('encpwd')
		keys = len(DATANAMEGAS)*[key]
		if request.method == 'POST':
			data = multrequest(DATANAMEGAS)
			encdata = list(map(encryptAES , data, keys))
			encdata = list(map(str,encdata))
			del key,keys,data
			sentence = setUpdate(DATANAMEGAS,encdata)
			db.updateGas(sentence,id)
			flash(' Updated Successfully')
		return redirect('/gas.html')
	@app.route(WEBPAGE+'gas/editar<string:id>', methods = ['POST', 'GET'])
	def get(id):
		user = session.get('user')
		db = dbInteracion(DBNAMEGAS)
		db.connect(TABLEGAS+user)
		key = session.get('encpwd')
		keys = len(DATANAMEGAS)*[key]
		rows = db.getDataGasWhere("item_id",id)[0]
		idData = [id]+list(map(decryptAES,rows,keys))
		del key,keys , user , rows
		return render_template('gas_update.html', purchase = idData )
	@app.route(WEBPAGE+"gas/eliminar/<string:id>", methods = ['GET','POST'])
	def delete(id):
		user = session.get('user')
		db = dbInteracion(DBNAME)
		db.connect(TABLEGAS+user)
		db.deleteWhere("item_id",id)
		#flash('you delete that')
		return redirect('/gas.html')
