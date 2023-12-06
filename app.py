import os
from os.path import join, dirname
from dotenv import load_dotenv

from pymongo import MongoClient
import jwt
from datetime import datetime, timedelta
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = './static/profile_pics'

SECRET_KEY = 'MERZY'

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

TOKEN_KEY = 'mytoken'

@app.route('/', methods= ['GET'])
def home():
  user_info = {
    'name': "Cindi"
  }
  logged_in = False
  is_admin = False
  return render_template('index.html', user_info=user_info, logged_in=logged_in, is_admin=is_admin)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)