import sqlite3
import os
import requests

conn = sqlite3.connect("static/db/to_do_list.db")
c = conn.cursor()

def check_db(db_path):
    if os.path.exists(db_path):
        return True
    else:
        return False
    
def get_db():
    try:
        conn = sqlite3.connect("static/db/to_do_list.db")
        c = conn.cursor()
        return conn, c
    except:
        return None

def get_data_from_db(query):
    try:
        conn, c = get_db()
        c.execute(query)
        return c.fetchall()
    except:
        return None
        
# def get_task_by_id(id_number):
#     task_info = get_data_from_db("SELECT * FROM person WHERE id = ?", id_number)
#     return task_info
        
# def change_task_title(id_number, new_title):
#     title_change = get_data_from_db("UPDATE table SET title = ? WHERE id = ?", id_number, new_title)
#     return title_change

def assign_task_id():
    all_task_ids = get_data_from_db("SELECT id FROM to_do_list")
    latest_task = max(all_task_ids)
    new_task_id = latest_task[0] + 1
    return new_task_id
