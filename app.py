
from flask import Flask, render_template, request,redirect,session
import api
from db import Database

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
dbo = Database()


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# Perform Registration
@app.route("/perform_registration",methods=['post'])
def perform_registration():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response = dbo.insert(name,email,password)
    if response:
        return render_template('login.html',message='Registration successfull. Kindly login to proceed')
    else:
        return render_template('register.html',message='Email already exists')

# Perform Login
@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect("/profile")
    else:
        return render_template('login.html',message='Incorrect Email/Password')


# Profile
@app.route("/profile")
def profile():
    if session:
        return render_template("profile.html")
    else:
        return redirect('/')


# Named Entity Recognition
@app.route("/ner")
def ner():
    if session:
        return render_template("ner.html")
    else:
        return redirect("/")

@app.route('/perform_ner' ,methods=['post'])

def perform_ner():
    if session.get('logged_in'):
        text = request.form.get("ner_text")  # This should match the form field name
        response = api.ner(text)
        return render_template('ner.html',response={'entities' : response})
    else:
        return redirect("/")


# Sentiment Analysis
@app.route("/senti")
def senti():
    if session:
        return render_template("senti.html")
    else:
        return redirect("/")

@app.route('/perform_sentiment' ,methods=['post'])

def perform_sentiment():
    if session.get('logged_in'):
        text = request.form.get("senti_text")  # This should match the form field name
        response = api.sentiment_analysis(text)
        print(response)
        return render_template('senti.html',response={'sentiment' : response})
    else:
        return redirect("/")


# Language Detection
@app.route("/lange")

def lange():
    if session:
        return render_template("language.html")
    else:
        return redirect("/")

@app.route('/perform_language' ,methods=['post'])

def perform_language():
    if session.get('logged_in'):
        text = request.form.get("lang_text")  # This should match the form field name
        response = api.language_detection(text)
        print(response)
        return render_template('language.html',response={'lang' : response})
    else:
        return redirect("/")

app.run(debug=True)

