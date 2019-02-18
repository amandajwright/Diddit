# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:50:25 2019

@author: amand
"""

import sqlite3
import os

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
        
def get_task():
    person_data = get_data_from_db("SELECT * FROM person WHERE surname = ?", surname.title())
    return person_data
