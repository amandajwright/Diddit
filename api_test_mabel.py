from flask import Flask
from flask_restful import Resource, Api
from db import list_all_db, list_columns_db
import sqlite3
from os.path import exists, isfile
import jsonify

# print(list_all_db())
# print(list_columns_db())

app = Flask(__name__)
api = Api(app)

# @app.route('/v1/get_all')
# class ListAll(Resource):
#     def get(self):
#         list_items = list_all_db()
#         columns = list_columns_db()
#         full_list = zip(columns, list_items)
#         return full_list

@app.route('/api/v1/get_all', methods=['GET'])
def get_all():
    list_items = list_all_db()
    columns = list_columns_db()
    
    return jsonify(list_items)

# def testing():
#     data = list_all_db()
#     list_items = list(data[0])
#     columns = list_columns_db()
#     print(list_items)
#     print(columns)
    
#     for item in columns:
#         if     

# print(testing())
# testing()
# api.add_resource(ListAll, '/')

if __name__ == '__main__':
    app.run(debug=True)