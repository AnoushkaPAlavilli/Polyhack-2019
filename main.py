#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:41:41 2019

@author: benpradko, anoushkaalavilli, ryangayhour
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)