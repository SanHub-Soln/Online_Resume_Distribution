import flask
from flask import render_template, redirect
import bot

start  = flask(__name__)

@app.route('/')
def route():
    render_template("idea1.html")

@app.route('/interface',Methods=['POST'])
def inter():
       start = Autofill() 