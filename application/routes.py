from flask import render_template, url_for, request, redirect, session

from application import app
import os

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title_head='Powerpuff University', title_body='Powerpuff University', subtitle='explore your ambitions', img="static/images/university/campus1.png")


