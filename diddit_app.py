# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:49:55 2019

@author: amand
"""

from flask import Flask, render_template, request
from diddit_funcs import *
app=Flask("MyApp")
      
@app.route("/", methods=["GET", "POST"])
def home():      
    results = {"id":1, "title":"Buy milk","description":"Make sure has best before of more than two days away.","status":"not done", "priority":"medium", "date":{"start_date":"2019-02-20T00:00:00Z", "end_date":"2019-02-20T00:30:00Z"}}
    return render_template ("index.html", title="results_page", **locals())

app.run(debug=True)