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
    results = {"id":; "title":;"notes":;"status":;}
    return render_template ("index.html", title="results_page", **locals())

app.run(debug=True)