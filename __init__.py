from flask    import Flask 
import MySQLdb

app = Flask(__name__)

app.config['SECRET_KEY'] = '62cc226f17d7c1d1a633dab4b6ae7298'

from Inventory_Management  import routes
