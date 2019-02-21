# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:50:25 2019

@author: amand
"""

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
        conn = sqlite3.connect("to_do_list.db")
        c = conn.cursor()
        return conn, c
    except:
        return None

def get_data_from_db(query, search_term):
    try:
        conn, c = get_db()
        c.execute(query, (search_term,))
        return c.fetchall()
    except:
        return None

def add_task(id_number, title, description, status, importance, date):
    task_delete = get_data_from_db("INSERT INTO to_do_list(id_number, title, description, status, importance, date) VALUES ({}, {}, {}, {}, {}, {})".format(id_number, title, description, status, importance, date))
    return task_delete

def get_all_tasks():
    all_tasks = get_data_from_db("SELECT * FROM to_do_list")
    return all_tasks
        
def get_task_by_id(id_number):
    task_info = get_data_from_db("SELECT * FROM person WHERE id = {}".format(id_number))
    return task_info
        
def change_task_title(id_number, new_title):
    title_change = get_data_from_db("UPDATE to_do_list SET title = {} WHERE id = {}".format(id_number, new_title))
    return title_change
        
def delete_task(id_number):
    task_delete = get_data_from_db("DELETE FROM to_do_list WHERE id = {}".format(id_number))
    return task_delete


