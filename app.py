from flask import Flask, render_template, url_for, flash, redirect,request
from forms    import addProductForm, editProductForm,addLocationForm, editLocationForm, addProductMovementForm, editProductMovementForm
from flask_mysqldb import MySQL
app = Flask(__name__)
mysql = MySQL(app)


app.config["MYSQL_HOST"]: 'localhost'
app.config["MYSQL_USER"]: 'root'
app.config["MYSQL_PASSWORD"]:''
app.config["MYSQL_DB"]: 'Management'

app.config['SECRET_KEY'] = '62cc226f17d7c1d1a633dab4b6ae7298'


@app.route("/")
@app.route("/dashboard")
def dashboard():
	return render_template('dashboard.html')

 
@app.route("/product")
def product():
	return render_template('product.html')

 

@app.route("/addProduct", methods =['GET','POST'])
def addProduct():
	form = addProductForm()
	if form.validate_on_submit():
		if form.validate_on_submit():
			product_id=""
			qty=""
			if request.method == 'POST':
				product_id=request.form['product_id']
				qty=request.form['qty']
				cur = mysql.connection.cursor()
				cur.execute("INSERT INTO product(product_id,qty) VALUES(%s, %s)",(product_id,qty))

				mysql.connection.commit()
				cur.close()     
				flash(f' {form.product_id.data} Product is Added successfully!', 'success')
	return render_template('addProduct.html', form = form)

@app.route("/editProduct", methods =['GET','POST'])
def editProduct():
	form = editProductForm()
	if form.validate_on_submit():
		product_id=""
		qty=""
		if request.method == 'POST':
			product_id=request.form['product_id']
			new_qty=request.form['new_qty']
			cur = mysql.connection.cursor()
			cur.execute("UPDATE product SET qty = new_qty WHERE product_id=product_id" )
			mysql.connection.commit()
			cur.close()     
			flash(f' {form.product_id.data} Product is edited successfully!', 'success')
	return render_template('editProduct.html', form = form)


@app.route("/viewProduct")
def viewProduct():
	cur = mysql.connection.cursor()
 	cur.execute("SELECT product_id, qty FROM product" )
	result = cursor.fetchall() 
	dict(result)
	mysql.connection.commit()
	cur.close()     	
	return render_template('viewProduct.html', result=dict(result))

@app.route("/location")
def location():
	return render_template('location.html') 	

@app.route("/addLocation", methods =['GET','POST'])
def addLocation():
	form = addLocationForm()
	if form.validate_on_submit():
		location_id=""
		if request.method == 'POST':
			location_id=request.form['location_id'] 
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO location(location_id) VALUES(%s, %s)",(location_id))
			mysql.connection.commit()
			cur.close()    
			flash(f' {form.location_id.data} Location is Added successfully!', 'success')
	return render_template('addLocation.html', form = form)

@app.route("/editLocation", methods =['GET','POST'])
def editLocation():
	form = editLocationForm()
	if form.validate_on_submit():
		location_id=""
		new_location_id=""
		if request.method == 'POST':
			location_id=request.form['location_id']
			new_location_id=request.form['new_location_id']
			cur = mysql.connection.cursor()
			cur.execute("UPDATE location SET location_id = new_location_id WHERE location_id=location_id" )
			mysql.connection.commit()
			cur.close()     
			flash(f' {form.location_id.data} Location is edited successfully!', 'success')
	return render_template('editLocation.html', form = form)


@app.route("/viewLocation")
def viewLocation():
	cur = mysql.connection.cursor()
	cur.execute("SELECT location_id FROM location" )
	result = cursor.fetchall() 
	dict(result)
	mysql.connection.commit()
	cur.close()     	
 	return render_template('viewLocation.html',result=dict(result))

@app.route("/productMovement")
def productMovement():
	return render_template('productMovement.html')	

@app.route("/addProductMovement", methods =['GET','POST'])
def addProductMovement():
	form = addProductMovementForm()
	if form.validate_on_submit():
		location_id=""
		if request.method == 'POST':
			movement_id=request.form['movement_id'] 
			from_location=request.form['from_location'] 
			to_location=request.form['to_location'] 
			product_id=request.form['product_id'] 
			qty=request.form['qty'] 
 			cur = mysql.connection.cursor()
 			cur.execute("SELECT qty FROM productmovement WHERE product_id=product_id AND from_location=from_location" )
			old_qty = cursor.fetchall()
			cur.execute("SELECT qty FROM productmovement WHERE product_id=product_id AND to_location=to_location" )
			old_x_qty = cursor.fetchall()
			cur.execute("INSERT INTO productmovement VALUES(%s, %s)",(movement_id,from_location,to_location,product_id,(qty+old_x_qty)))
			cur.execute("UPDATE product SET qty = (old_qty-qty) WHERE product_id=product_id" )
			mysql.connection.commit()
			cur.close()    
		flash(f' {form.movement_id.data} Movemevt is Added successfully!', 'success',)
	return render_template('addProductMovement.html', form = form)
 
@app.route("/editProductMovement", methods =['GET','POST'])
def editProductMovement():
	form = editProductMovementForm()
	if form.validate_on_submit():
		product_id=""
		qty=""
		if request.method == 'POST':
			movement_id=request.form['movement_id'] 
			from_location=request.form['from_location'] 
			to_location=request.form['to_location'] 
			product_id=request.form['product_id'] 
			qty=request.form['qty'] 
			cur = mysql.connection.cursor()
			cur.execute("UPDATE productmovement SET from_location = from_location, to_location= to_location, product_id =product_id, qty=qty WHERE movement_id=movement_id" )
			
			mysql.connection.commit()
			cur.close()     
		flash(f' {form.movement_id.data} Movemevt is edited successfully!', 'success',)
	return render_template('editProductMovement.html', form = form)


@app.route("/viewProductMovement")
def viewProductMovement():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM productmovement" )
	result = cursor.fetchall() 
	dict(result)
	mysql.connection.commit()
	cur.close() 
	return render_template('viewProductMovement.html',dict(result))


















if __name__ == '__main__':
  app.run(debug = True)