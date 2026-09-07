# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:52:52 2026

@author: shrih
"""

from flask import Flask, url_for
app=Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/")
def home():
    user_url = url_for('user', name="Mahesh")
    return f'<a href="{user_url}">Go to User</a>'

if __name__=="__main__":
    app.run(debug=True)    
