from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv(override=True)

from models import db  # importa o db AQUI

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY_FLASK")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # inicializa aqui

with app.app_context():
    db.create_all()

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
