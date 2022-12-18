from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/gat'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    FirstName = db.Column(db.String(100))
    LastName = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    Gender = db.Column(db.String(100))
    BirthDay = db.Column(db.Date)
    Address = db.Column(db.String(100))
    City = db.Column(db.String(100))
    PinCode = db.Column(db.String(100))
    State = db.Column(db.String(100))
    Country = db.Column(db.String(100))

    def __init__(self, FirstName, LastName, email, phone, Gender, BirthDay, Address, City, PinCode, State, Country):
 
        self.FirstName = FirstName
        self.LastName = LastName
        self.email = email
        self.phone = phone
        self.Gender = Gender
        self.BirthDay = BirthDay
        self.Address = Address
        self.City = City
        self.PinCode = PinCode
        self.State = State
        self.Country = Country

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/teacherlogin')
def teacherlogin():
   return render_template('teacherlogin.html')

@app.route('/studentlogin')
def studentlogin():
   return render_template('studentlogin.html')

@app.route('/teacherpage')
def teacherpage():
   return render_template('teacherpage.html')

@app.route('/insert')
def insert():
   if request.method == 'POST':
 
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        email = request.form['email']
        phone = request.form['phone']
        Gender = request.form['Gender']
        BirthDay = request.form['BirthDay']
        Address = request.form['Address']
        City = request.form['City']
        PinCode = request.form['PinCode']
        State = request.form['State']
        Country = request.form['Country']
 
        my_data = Data(FirstName, LastName, email, phone, Gender, BirthDay, Address, City, PinCode, State, Country)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Events Added Successfully")
 
        return render_template(url_for('insert'))
   

if __name__ == '__main__':
   app.run(debug = True)