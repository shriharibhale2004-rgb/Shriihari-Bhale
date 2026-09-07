# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:57:56 2026

@author: shrih
"""
from flask import Flask

app=Flask(__name__)
@app.route("/")
def home():
    return "Ram Krushna Hari!"
if __name__=="__main__":
     app.run(debug=True)
