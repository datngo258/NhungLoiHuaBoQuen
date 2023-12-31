from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'sdhvsdvsgdhu1ihbdjghjghjfghjfk345ger@sg23!d'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ngodinhdat12345@localhost/nhungloihuaboquen?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
admin = Admin(app=app, name='TheBest',template_mode='bootstrap4')
