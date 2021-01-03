from flask import Flask, render_template, url_for, flash, redirect
from Inventory_Management.forms    import addProductForm, editProductForm,addLocationForm, editLocationForm, addProductMovementForm, editProductMovementForm
from Inventory_Management    import app
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
#conig database
app.config["MYSQL_HOST"]: 'localhost'
app.config["MYSQL_USER"]: 'root'
app.config["MYSQL_PASSWORD"]: ''
app.config["MYSQL_DB"]: 'Management'



@app.route("/")
@app.route("/dashboard")
def dashboard():
	return render_template('dashboard.html')

 
@app.route("/product")
def product():
	return render_template('product.html')

@app.route("/try1")
def try1():
	return render_template('try.html')

@app.route("/addProduct", methods =['GET','POST'])
def addProduct():
	form = addProductForm()
	if form.validate_on_submit():
 
		flash(f' {form.product_id.data} Product is Added successfully!', 'success')
	return render_template('addProduct.html', form = form)

@app.route("/editProduct", methods =['GET','POST'])
def editProduct():
	form = editProductForm()
	if form.validate_on_submit():
		flash(f' {form.product_id.data} Product is edited successfully!', 'success')
	return render_template('editProduct.html', form = form)


@app.route("/viewProduct")
def viewProduct():
	product.query.all()
	return render_template('viewProduct.html')

@app.route("/location")
def location():
	return render_template('location.html') 	

@app.route("/addLocation", methods =['GET','POST'])
def addLocation():
	form = addLocationForm()
	if form.validate_on_submit():
		flash(f' {form.location_id.data} Location is Added successfully!', 'success')
	return render_template('addLocation.html', form = form)

@app.route("/editLocation", methods =['GET','POST'])
def editLocation():
	form = editLocationForm()
	if form.validate_on_submit():
		flash(f' {form.location_id.data} Location is edited successfully!', 'success')
	return render_template('editLocation.html', form = form)


@app.route("/viewLocation")
def viewLocation():
	location.query.all()
	return render_template('viewLocation.html')

@app.route("/productMovement")
def productMovement():
	return render_template('productMovement.html')	

@app.route("/addProductMovement", methods =['GET','POST'])
def addProductMovement():
	form = addProductMovementForm()
	if form.validate_on_submit():
		flash(f' {form.movement_id.data} Movemevt is Added successfully!', 'success',)
	return render_template('addProductMovement.html', form = form)

@app.route("/editProductMovement", methods =['GET','POST'])
def editProductMovement():
	form = editProductMovementForm()
	if form.validate_on_submit():
		flash(f' {form.movement_id.data} Movemevt is edited successfully!', 'success',)
	return render_template('editProductMovement.html', form = form)


@app.route("/viewProductMovement")
def viewProductMovement():
	return render_template('viewProductMovement.html')

