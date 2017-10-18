"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request, json
from werkzeug import generate_password_hash, check_password_hash
from BucketListApp import app, mysql

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/')
@app.route('/bucket')
def bucket():
    """Renders the root page of the Bucket List App"""
    return render_template('BucketList.html') 

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():

    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    if _name and _email and _password:
        conn = mysql.connect()
        cursor = conn.cursor()
        _hashed_password = generate_password_hash(_password)

        cursor.callproc('sp_createUser',(_name, _email, _hashed_password))

        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()

            the_json = json.dumps({'message' : 'User created successfully', 'redirect': True, 'redirect_url': request.url_root + 'bucket'})

            return the_json
        else:
            return json.dumps({'error' : str(data[0])})
    else:
        return json.dumps({'html' : '<span>Enter the required fields</span>'})

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
