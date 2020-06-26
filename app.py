from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.secret_key = ''

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/serasa_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

