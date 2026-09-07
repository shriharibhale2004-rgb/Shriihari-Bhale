# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:46:51 2026

@author: shrih
"""

from flask import Flask
app =Flask(__name__)

@app.route("/")
def home():
    return"<h1>Hello,World<h1>"
    
@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}"

if __name__=="__main__":
    app.run(debug=True)