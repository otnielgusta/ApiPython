from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from mysql.connector import connection
class Server():
    
    mydb = connection.MySQLConnection(
        host='127.0.0.1',
        user='root',
        password='',
        database='trabalhootniel'
        )
    db_connect = create_engine('sqlite:///exemplo.db')

    app = Flask(__name__)
    api = Api(app)   
        
   
server = Server()