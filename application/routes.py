from flask import render_template, url_for, request, redirect, session
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
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

@app.route('/bellehall')
def bellehall():
    return render_template('belle_hall.html', title_head='belle hall', title_body='belle hall', subtitle='bliss', img="static/images/university/belle1.jpeg")

@app.route('/bunnyphall')
def bunnyhall():
    return render_template('bunny_hall.html', title_head='bunny hall', title_body='bunny hall', subtitle='adventious', img="static/images/university/bunny1.jpeg")




@app.route('/contact')
def contact():
    return render_template('contact.html', title_head='contact us', title_body='contact us', subtitle='connect with our front desk', img="static/images/university/campus.jpg")

@app.route('/students')
def students():
    return render_template('students.html', title_head='Students', title_body='PPU Students', subtitle='current students enrolled in a society', img="static/images/university/ppg.jpeg")

@app.route('/signup')
def signup():
    return render_template('sign_up.html', title_head='sign up', title_body='sign up', subtitle="join a society by signing up and choosing a society.", img="static/images/university/campus5.png")

@app.route("/eatretreatsociety")
def eat_retreat():
    return render_template('eat_and_retreat_society.html', title_head="eat and retreat society", title_body="Eat & Retreat Society", subtitle="This is  a society for explorers of local delicacy and hidden gem", img="static/images/eatretreat3.jpeg")









@app.route('/sumit', methods =['POST'])
def submit():
    firstname = request.form ['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    society = request.form['society']
    return f"Welcome {firstname.title()} {lastname.title()}  to the {society} Society. We will send a notification to {email}."


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    error = ""
    signup_form = RegisterForm()

    if request.method == 'POST':
        first_name = register_form.first_name.data
        last_name = register_form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = 'Please supply both a first and last name'

        else:
            people.append({'Firstname': first_name, 'Lastname': last_name})
            add_person(first_name, last_name)
            return redirect(url_for('register'))

    return render_template('register.html', form=register_form, title='Add Person', message=error)