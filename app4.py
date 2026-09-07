# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:16:23 2026

@author: shrih
"""

from flask import Flask
app=Flask(__name__)
#step 1: Create function
def home():
    return "Welcome to Home page"
def about():
    return "This is about page"

#step 2: bind URLs using add_url_rule()
app.add_url_rule("/","home",home)
app.add_url_rule("/about","about",about)
#step3: Run the app
if __name__=="__main__":
    app.run(debug=True)