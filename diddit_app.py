from flask import Flask, render_template, request, jsonify
import sqlite3
from diddit_funcs import *
from db import *
import requests
import json
from flask import Markup
import datetime

app=Flask(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/", methods=["GET", "POST"])
def home():     
    data = requests.get('http://127.0.0.1:5000/v1/entries/tasks/all').text
    response = json.loads(data)
    today_html_block = []
    future_html_block = []
    for task in response:
        if task['end_date'] <= datetime.datetime.today().strftime('%Y-%m-%d'):
            
            if task['priority'] == 'high':
                html_block_template = '''<div class="single-task"><input name={} id={} class="strikethrough" type="checkbox">
                <label for="task-1" class="strikeThis"><a data-toggle="modal" href="#ViewTaskModal" style='color:red'>{}
                </a></label></div>'''.format(task['id'], task['id'], task['title'])
                today_html_block.append(Markup(html_block_template))

            else:
                html_block_template = '''<div class="single-task"><input name={} id={} class="strikethrough" type="checkbox">
                <label for="task-1" class="strikeThis"><a data-toggle="modal" href="#ViewTaskModal">{}
                </a></label></div>'''.format(task['id'], task['id'], task['title'])
                today_html_block.append(Markup(html_block_template))
        else:
            if task['priority'] == 'high':
                html_block_template = '''<div class="single-task"><input name={} id={} class="strikethrough" type="checkbox">
                <label for="task-1" class="strikeThis"><a data-toggle="modal" href="#ViewTaskModal" style='color:red'>{}
                </a></label></div>'''.format(task['id'], task['id'], task['title'])
                future_html_block.append(Markup(html_block_template))

            else:
                html_block_template = '''<div class="single-task"><input name={} id={} class="strikethrough" type="checkbox">
                <label for="task-1" class="strikeThis"><a data-toggle="modal" href="#ViewTaskModal">{}
                </a></label></div>'''.format(task['id'], task['id'], task['title'])
                future_html_block.append(Markup(html_block_template))

    return render_template("index.html", today_html_block=today_html_block, future_html_block=future_html_block)

@app.route("/v1/tasks/all", methods=["GET"])
def all_tasks():      
    conn = sqlite3.connect("static/db/to_do_list.db")
    conn.row_factory = dict_factory
    c = conn.cursor()
    all_tasks = c.execute("SELECT * FROM to_do_list;").fetchall()
    return jsonify(all_tasks)

@app.route("/v1/tasks/<float:task_id>/done", methods=["PATCH","GET"])
def mark_done(task_id):
    response = {'status code': 500}
    try:
        conn = sqlite3.connect("static/db/to_do_list.db")
        c = conn.cursor()
        print('woo')
        query = "UPDATE to_do_list SET status='done' WHERE id=?"
        c.execute(query, (task_id,))
        conn.commit()
        response['status code'] = 200
    except sqlite3.Error as e:
        response['status code'] = 500
        print(e)
    finally:
        return jsonify(response) 
    
# @app.route("/v1/entries/tasks/create", methods=["POST"])
def create_task():
    db_path = get_db()
    conn, c = connect_db(db_path)
    conn.row_factory = dict_factory
    task_id = 3
    title = 'Eat yoghurt'
    description = 'Yoghurt in fridge'
    status = 'not done'
    priority = 'high'
    start_date = '2019-02-21'
    end_date = '2019-02-21'
    c.execute("INSERT INTO to_do_list(id, title, description, status, priority, start_date, end_date) VALUES(?,?,?,?,?,?,?)",(task_id, title, description, status, priority, start_date, end_date,))
    conn.commit()
    # close_db(conn, c)
    c.close
    conn.close


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The entry could not be found.</p>", 404

@app.route("/v1/entries/tasks", methods=["GET"])
def tasks_filter():
    query_parameters = request.args
    id = query_parameters.get("id")
    title = query_parameters.get("title")
    status = query_parameters.get("status")
    importance = query_parameters.get("importance")
    
    query = "SELECT * FROM to_do_list WHERE"
    to_filter = []
    
    if id:
        query += " id=? AND"
        to_filter.append(id)
    if title:
        query += " title=? AND"
        to_filter.append(title)
    if status:
        query += " status=? AND"
        to_filter.append(status)
    if importance:
        query += " importance=? AND"
        to_filter.append(importance)
    if not (id or title or status or importance):
        return page_not_found(404)
    
    query = query[:-4] + ";"
    
    conn = sqlite3.connect("to_do_list.db")
    conn.row_factory = dict_factory
    c = conn.cursor()
    
    results = c.execute(query, to_filter).fetchall()
    
    return jsonify(results)
        
@app.route("/v1/entries/tasks/<int:id>", methods=["GET"])
def filter_by_id():
    sql_statement = "SELECT * FROM to_do_list WHERE id = {}".format(id)
    results = sql_statement.results
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
#from sqlalchemy import create_engine
#from json import dumps
#
#db_connect = create_engine("sqlite:///to_do_list")
#app = Flask(__name__)
#api = Api(app)
#
#class Tasks(Resource):
#    def post(self, id, title, status, importance):
#        conn = db_connect.connect()
#        query = conn.execute("INSERT INTO to_do_list(id, title, status, importance) VALUES (?, ?, ?, ?, ?, ?)", (id, title, status, importance,))
#        