from flask import Flask
from flask_restful import Resource, Api
import flask
from db import list_all_db
import sqlite3
from os.path import exists, isfile

print(list_all_db())

app = Flask(__name__)
api = Api(app)

class ListAll(Resource):
    def get(self):
