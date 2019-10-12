#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:41:41 2019

@author: benpradko, anoushkaalavilli, ryangayhour
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("format.html")

@app.route("/about")

if __name__ == "__main__":
    app.run(debug=True)
