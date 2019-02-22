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
   form_data = request.form
   task_id = assign_task_id()
   title = form_data['formGroupTaskInput']
   description = form_data['formGroupTaskDescription']
   status = 'not done'
   if request.form.get('priority'):
       priority = "high"
   else:
       priority = "low"
   date = form_data['start_date']
   conn = sqlite3.connect("static/db/to_do_list.db")
   c = conn.cursor()
   c.execute('INSERT INTO to_do_list(id, title, description, status, priority, start_date) VALUES(?,?,?,?,?,?)',(task_id, title, description, status, priority, date,))
   conn.commit()
   close_db(c, conn)
   return redirect("http://127.0.0.1:5000/", code=302)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The entry could not be found.</p>", 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
