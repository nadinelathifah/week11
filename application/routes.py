from flask import render_template, url_for, request, redirect, session

from application import app
import os

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title_head='Powerpuff University', title_body='Powerpuff University', subtitle='★ explore your ambitions ★', img="static/images/university/campus1.png")

@app.route('/societies')
def societies():
    return render_template('societies.html', title_head='Societies', title_body='Student Societies', subtitle='★ connect, engage, build communities: discover our student societies ★', img="static/images/university/campus2.jpg")

@app.route('/blossomhall')
def blossomhall():
    return render_template('blossom_hall.html', title_head='blossom hall', title_body='blossom hall', subtitle='classy', img="static/images/university/blossomhall.jpeg")

@app.route('/bubbleshall')
def bubbleshall():
    return render_template('bubbles_hall.html', title_head='bubbles hall', title_body='bubbles hall', subtitle='whimsical', img="static/images/university/bubbleshall.jpeg")

@app.route('/buttercuphall')
def buttercuphall():
    return render_template('buttercup_hall.html', title_head='buttercup hall', title_body='buttercup hall', subtitle='grunge', img="static/images/university/buttercuphall.jpeg")

@app.route('/contact')
def contact():
    return render_template('contact.html', title_head='contact us', title_body='contact us', subtitle='connect with our front desk', img="static/images/university/campus.jpg")

@app.route('/signup')
def signup():
    return render_template('sign_up.html', title_head='sign up', title_body='sign up', subtitle="join a society by signing up and choosing a society.")
