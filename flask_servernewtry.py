from flask import Flask, render_template, request, redirect, url_for, g, session, send_from_directory
from os import path, walk
import os
import pandas as pd
import time
import pymysql
from Rankstatement import rankstatement

db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="testdatabase",
    cursorclass=pymysql.cursors.DictCursor,
autocommit = True)

cursor  = db.cursor()

nwdb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="NWdatabase",
autocommit = True)

#nwcursor = nwdb.cursor()
# Assign the name of the application to 'app'
app = Flask(__name__)

# Key required for 'session'
app.secret_key = os.urandom(24)


#######################################################################
# Login
#######################################################################
@app.route('/',methods=['GET','POST'])
def login():

    # Output message if something goes wrong
    error = ''

    # If the user requests to log in (POST)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        # Replace 'user' with None to reset the session
        session.pop('user',None)

        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        # Check if account exists in MySQL
        cursor.execute('SELECT * FROM pythonlogin.accounts WHERE username = %s AND password = %s', (username, password))
        #Fetch one record and return result
        account = cursor.fetchone()

        print(account)

        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True

            # The user session is for 'username'
            session['user'] = request.form['username']
            session['branch'] = account['Branch']

            # Redirect to homepage after succesful login
            return redirect(url_for('homepage'))

        else:

            # Error message if doesnt log in
            error = 'Invalid Credentials, Please Try Again'

    # Default render login.html   
    return render_template('login.html',error=error)

#######################################################################
# Check Session
#######################################################################
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

#######################################################################
# Homepage
#######################################################################
@app.route('/homepage')
def homepage():
    if g.user:
        return render_template('homepage.html')
    return redirect(url_for('login'))
def lookupstatment(branch):
   return 'SELECT *FROM branchdatabase.' + str(branch)

#######################################################################
# My Profile
#######################################################################
@app.route('/project')
def profile():
    if g.user:
        rankedlads = rankstatement(str(session['branch']), 'EigenvectorCent')
        topcol = []
        for i in range(len(rankedlads)):
            if i < 3:
                topcol.append(rankedlads[i][0])

        rankedlads = rankstatement(str(session['branch']), 'BetweenessCent')
        knowbro = []
        for i in range(len(rankedlads)):
            if i < 3:
                knowbro.append(rankedlads[i][0])

        rankedlads = rankstatement(str(session['branch']), 'CLoseCent')
        print(rankedlads)
        reversedlads = rankedlads[::-1]
        print(reversedlads)
        isobro = []
        for i in range(len(reversedlads)):
            if i < 3:
                isobro.append(reversedlads[i][0])



        return render_template('project.html', branch = str(session['branch']), topcol = topcol, knowbro = knowbro, isobro = isobro)
    return redirect(url_for('login'))


#######################################################################
# Project Search
#######################################################################
@app.route('/search', methods=['GET','POST'])
def search():

    if request.method == "POST":
        branch = request.form['branch']

        #select database

        cursor.execute('SELECT table_name FROM information_schema.tables WHERE table_schema = \'branchdatabase\' AND TABLE_NAME = %s ', [branch])
        data = cursor.fetchall()

        branchfound = 1


        print(len(data))
        if len(data) == 1 and branchfound == 1:
            cursor.execute(lookupstatment(branch))
            data = cursor.fetchall()
        else:
            branchfound = 0

        return render_template('search.html', data = data, branchfound = branchfound)
    return render_template('search.html')
    #return redirect(url_for('login'))

#######################################################################
# Employee Search
#######################################################################
@app.route('/global_search')
def global_search():
    if g.user:
        return render_template('global_search.html')
    return redirect(url_for('login'))

#######################################################################
# FAQ, About and Contact Page
#######################################################################
@app.route('/<page>')
def details(page):
    if g.user:
        if page == 'about':
            message1 = 'About Us'
            message2 = 'This webpage is a search engine for each employee \
                        social connectivity. The properties of each employee \
                        are based on their email traffic within the company'
        elif page == 'FAQ':
            message1 = 'FAQ Section'
            message2 = 'This is the FAQ Section'
        elif page == 'contact':
            message1 = 'Contact Us'
            message2 = 'This is the contact page'
        return render_template('{}.html'.format(page),message1=message1,message2=message2)
    return redirect(url_for('login'))

#######################################################################
# Favicon identifyer
######################################################################
@app.route('/favicon.ico')
def favicon():
    # If asked of favicon, return icon favicon.ico
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#######################################################################
# Debug and Initialisation
#######################################################################
if __name__ == '__main__':

    # Load the database
    print('Loading Webserver...')

    # This is for debugging and searches for updated files whenever
    # the file is run. Auto refreshes the local server.
    extra_dirs = ['/static',]
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)
    app.run(extra_files=extra_files,debug=True)
