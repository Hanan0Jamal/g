from flask_wtf import FlaskForm
from wtforms   import StringField, SubmitField
from wtforms.validators  import DataRequired 

class addProductForm(FlaskForm):
	product_id = StringField('product_id', validators=[DataRequired()])
	qty		   = StringField('qty', validators=[DataRequired()] )
	submit = SubmitField('add_Product')

class editProductForm(FlaskForm):
	product_id = StringField('product_id', validators=[DataRequired()] )
	new_qty = StringField('new_qty', validators=[DataRequired()] )
	submit = SubmitField('edit Product')

 

class addLocationForm(FlaskForm):
	location_id = StringField('location_id', validators=[DataRequired()] )
	submit = SubmitField('add Location')


class editLocationForm(FlaskForm):
	location_id = StringField('location_id', validators=[DataRequired()] )
	new_location_id = StringField('new_location_id', validators=[DataRequired()] )
	submit = SubmitField('edit Location')

 

class addProductMovementForm(FlaskForm):
	movement_id = StringField('movement_id', validators=[DataRequired()] )
	submit = SubmitField('add Movement')


class editProductMovementForm(FlaskForm):
	movement_id = StringField('movement_id', validators=[DataRequired()] )
	submit = SubmitField('edit Movement')

 