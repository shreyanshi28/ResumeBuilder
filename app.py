from flask import Flask, render_template, request, redirect, url_for, session, send_file, make_response
from flask_mysqldb import MySQL
import pdfkit
import MySQLdb.cursors
import re
path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
options = {'enable-local-file-access': None}
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

app.secret_key = 'try'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flasklogin'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

@app.route('/flasklogin/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password'].encode()
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username LIKE %s', [username])
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)


@app.route('/flasklogin/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return render_template('filler.html')
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

@app.route('/help', methods=['GET','POST'])
def help():
    if request.method=='POST' and 'comment' in request.form:
        comment = request.form['comment']
        cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor2.execute('INSERT INTO feedback1 VALUES (%s)', (comment))
        mysql.connection.commit()
        return render_template('help.html', comment=comment)
    return render_template('help.html')

@app.route('/flasklogin/filler/choice')
def choice():
    return render_template('choice.html')
    
@app.route('/flasklogin/filler/choice/form1')
def form1():
    return render_template('form1.html')

@app.route('/flasklogin/filler/choice/form2')
def form2():
    return render_template('form2.html')

@app.route('/flasklogin/filler/choice/form3')
def form3():
    return render_template('form3.html')

@app.route('/flasklogin/filler/choice/form1/resumet1',methods = ['POST', 'GET'])
def resume1():
    if request.method == 'POST':   
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address= request.form['address']
        zipcode = request.form['zipcode']
        city = request.form['city']
        phone = request.form['phone']
        country = request.form['country']
        email = request.form['email']
        highschool = request.form['highschool']
        inter = request.form['inter']
        undergrad = request.form['undergrad']
        grad = request.form['grad']
        others = request.form['others']
        experience = request.form['experience']
        skills = request.form['skills']
        interest = request.form['interest']
        summary = request.form['summary']
           
        return render_template("resumet1.html",firstname = firstname, lastname=lastname,address=address,zipcode=zipcode,city=city, country=country, email=email, phone=phone,highschool=highschool, inter=inter, undergrad=undergrad,grad=grad,others=others,experience=experience,skills=skills,interest=interest,summary=summary)
      
@app.route('/flasklogin/filler/choice/form1/resumetd1',methods = ['POST', 'GET'])
def resumed1():
    if request.method == 'POST':   
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address= request.form['address']
        zipcode = request.form['zipcode']
        city = request.form['city']
        phone = request.form['phone']
        country = request.form['country']
        email = request.form['email']
        highschool = request.form['highschool']
        inter = request.form['inter']
        undergrad = request.form['undergrad']
        grad = request.form['grad']
        others = request.form['others']
        experience = request.form['experience']
        skills = request.form['skills']
        interest = request.form['interest']
        summary = request.form['summary']
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('INSERT INTO formdata2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (firstname,lastname,address,city,zipcode,country,email,phone,highschool,inter,undergrad,grad,others,experience,skills,interest,summary))
        mysql.connection.commit() 
        rendered = render_template("resumetd1.html",firstname = firstname, lastname=lastname,address=address,zipcode=zipcode,city=city, country=country, email=email, phone=phone,highschool=highschool, inter=inter, undergrad=undergrad,grad=grad,others=others,experience=experience,skills=skills,interest=interest,summary=summary)
        pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=resume.pdf'
        return response
    
@app.route('/flasklogin/filler/choice/form2/resumet2',methods = ['POST', 'GET'])
def resume2():
    if request.method == 'POST':   
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address= request.form['address']
        zipcode = request.form['zipcode']
        city = request.form['city']
        phone = request.form['phone']
        country = request.form['country']
        email = request.form['email']
        highschool = request.form['highschool']
        inter = request.form['inter']
        undergrad = request.form['undergrad']
        grad = request.form['grad']
        others = request.form['others']
        experience = request.form['experience']
        skills = request.form['skills']
        interest = request.form['interest']
        summary = request.form['summary']
           
        return render_template("resumet2.html",firstname = firstname, lastname=lastname,address=address,zipcode=zipcode,city=city, country=country, email=email, phone=phone,highschool=highschool, inter=inter, undergrad=undergrad,grad=grad,others=others,experience=experience,skills=skills,interest=interest,summary=summary)
      
@app.route('/flasklogin/filler/choice/form2/resumetd2',methods = ['POST', 'GET'])
def resumed2():
    if request.method == 'POST':   
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address= request.form['address']
        zipcode = request.form['zipcode']
        city = request.form['city']
        phone = request.form['phone']
        country = request.form['country']
        email = request.form['email']
        highschool = request.form['highschool']
        inter = request.form['inter']
        undergrad = request.form['undergrad']
        grad = request.form['grad']
        others = request.form['others']
        experience = request.form['experience']
        skills = request.form['skills']
        interest = request.form['interest']
        summary = request.form['summary']
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('INSERT INTO formdata2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (firstname,lastname,address,city,zipcode,country,email,phone,highschool,inter,undergrad,grad,others,experience,skills,interest,summary))
        mysql.connection.commit() 
        rendered = render_template("resumetd2.html",firstname = firstname, lastname=lastname,address=address,zipcode=zipcode,city=city, country=country, email=email, phone=phone,highschool=highschool, inter=inter, undergrad=undergrad,grad=grad,others=others,experience=experience,skills=skills,interest=interest,summary=summary)
        pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=resume.pdf'
        return response
    
@app.route('/flasklogin/filler/choice/form3/resumet3',methods = ['POST', 'GET'])
def resume3():
    if request.method == 'POST':   
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address= request.form['address']
        zipcode = request.form['zipcode']
        city = request.form['city']
        phone = request.form['phone']
        country = request.form['country']
        email = request.form['email']
        highschool = request.form['highschool']
        inter = request.form['inter']
        undergrad = request.form['undergrad']
        grad = request.form['grad']
        others = request.form['others']
        experience = request.form['experience']
        skills = request.form['skills']
        interest = request.form['interest']
        summary = request.form['summary']
           
        return render_template("resumet3.html",firstname = firstname, lastname=lastname,address=address,zipcode=zipcode,city=city, country=country, email=email, phone=phone,highschool=highschool, inter=inter, undergrad=undergrad,grad=grad,others=others,experience=experience,skills=skills,interest=interest,summary=summary)
      
@app.route('/flasklogin/filler/choice/form3/resumetd3',methods = ['POST', 'GET'])
def resumed3():
    if request.method == 'POST':   
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address= request.form['address']
        zipcode = request.form['zipcode']
        city = request.form['city']
        phone = request.form['phone']
        country = request.form['country']
        email = request.form['email']
        highschool = request.form['highschool']
        inter = request.form['inter']
        undergrad = request.form['undergrad']
        grad = request.form['grad']
        others = request.form['others']
        experience = request.form['experience']
        skills = request.form['skills']
        interest = request.form['interest']
        summary = request.form['summary']
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute('INSERT INTO formdata2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (firstname,lastname,address,city,zipcode,country,email,phone,highschool,inter,undergrad,grad,others,experience,skills,interest,summary))
        mysql.connection.commit() 
        rendered = render_template("resumetd3.html",firstname = firstname, lastname=lastname,address=address,zipcode=zipcode,city=city, country=country, email=email, phone=phone,highschool=highschool, inter=inter, undergrad=undergrad,grad=grad,others=others,experience=experience,skills=skills,interest=interest,summary=summary)
        pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=resume.pdf'
        return response
    
if __name__=='__main__':
    app.run(debug=True)
