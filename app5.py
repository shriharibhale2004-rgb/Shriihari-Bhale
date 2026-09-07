# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:52:53 2026

@author: shrih
"""

from flask import Flask
app=Flask(__name__)

#1 STRING
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}! (String Example)"

#2 INT
@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post ID: {post_id} (Integer example)"

#3 FLOAT
@app.route("/price/<float:value>")
def price(value):
    return f"Price: {value} (float Example)"

#4 Path
@app.route("/file/<path:filename>")
def file(filename):
    return f"file Path: {filename} (path Example)"

#5any

@app.route("/color/<any(red,blue,green):choice>")
def color(choice):
    return f"Slected color: {choice} (Any Example)"

#6 UUID
from uuid import UUID

@app.route("/uuid_example/<uuid:user_id>")
def uuid_example(user_id):
    return f"UUID: {user_id} (UUID example)"

#home route (for testing links)
@app.route("/")
def home():
    return """
    <h2>Flask Variable Rules Demo</h2>
    <ul>
        <li>/user/Mahesh</li>
        <li>/post/10</li>
        <li>/price/99.99</li>
        <li>/file/c:/4-flask/test.txt</li>
        <li>/color/red</li>
        <li>/uuid_example/123:456:789</li>
    </ul>
    """
#run the app
if __name__=="__main__":
    app.run(debug=True)    