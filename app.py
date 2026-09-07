# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:18:11 2026

@author: shrih
"""
from flask import Flask
#Import tne Flask class from the Flask package
app=Flask(__name__)
#Import the Flask class from the flask package
#_name_ tells Flask where to look for files (templates, statics)
@app.route("/")
#This is a decorator
#Maps URL \ function below
def home():
    return "Hello World!"
#Function that handles request
#Maps URL/-function below
if __name__=="__main__":
     app.run(debug=True)
#Runs the server
#debug=True
