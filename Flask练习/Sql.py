# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE_NAME = 'pythonDB'
# USERNAME = 'pymysql'
# PASSWORD = '123'
#
# DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{databasename}?charset=utf8mb4" \
#     .format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, databasename=DATABASE_NAME)
#
# print(DB_URI)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOST = '127.0.0.1'
PORT = '3306'
DATABASE_NAME = 'pythonDB'
USERNAME = 'pymysql'
PASSWORD = '123'
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{databasename}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,host=HOST,port=PORT,databasename=DATABASE_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)