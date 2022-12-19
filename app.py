from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
# Import for Migrations
#from flask_migrate import Migrate, migrate
 
app = Flask(__name__)

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/gat_website'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

# Settings for migrations
#migrate = Migrate(app, db)

# Models
class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	FirstName = db.Column(db.String(20), unique=False, nullable=False)
	LastName = db.Column(db.String(20), unique=False, nullable=False)
	email = db.Column(db.String(20),unique=False, nullable=False)
	phone = db.Column(db.String(20),unique=False, nullable=False)
	Gender = db.Column(db.String(20), unique=False, nullable=False)
	BirthDay = db.Column(db.String(20),unique=False, nullable=False)
	Address = db.Column(db.String(30), unique=False, nullable=False)
	City = db.Column(db.String(20), unique=False, nullable=False)
	PinCode = db.Column(db.String(20),unique=False, nullable=False)
	State = db.Column(db.String(20), unique=False, nullable=False)
	Country = db.Column(db.String(20), unique=False, nullable=False)
	
	def __repr__(self):
		return f"FirstName : {self.FirstName},LastName : {self.LastName} email: {self.email},phone : {self.phone}, Gender: {self.Gender},BirthDay : {self.BirthDay}, Address: {self.Address},City : {self.City}, PinCode: {self.PinCode},  State: {self.State},  Country: {self.Country}"

# function to render index page
@app.route('/insert')
def insert():
	profiles = Profile.query.all()
	return render_template('insert.html', profiles=profiles)

@app.route('/add_data')
def add_data():
	return render_template('add_profile.html')

# function to add profiles
@app.route('/add', methods=["POST"])
def profile():
	FirstName = request.form.get("FirstName")
	LastName = request.form.get("LastName")
	email = request.form.get("email")
	phone = request.form.get("phone")
	Gender = request.form.get("Gender")
	BirthDay = request.form.get("BirthDay")
	Address = request.form.get("Address")
	City = request.form.get("City")
	PinCode = request.form.get("PinCode")
	State = request.form.get("State")
	Country = request.form.get("Country")

	# create an object of the Profile class of models and
	# store data as a row in our datatable
	if FirstName != '' and LastName != '' and email is not None:
		p = Profile(FirstName=FirstName, LastName=LastName, email=email, phone=phone, Gender=Gender, BirthDay=BirthDay, Address=Address, City=City, PinCode=PinCode, State=State, Country=Country)
		db.session.add(p)
		db.session.commit()
		return redirect('/insert')
	else:
		return redirect('/insert')

@app.route('/delete/<int:id>')
def erase(id):
	
	# deletes the data on the basis of unique id and
	# directs to home page
	data = Profile.query.get(id)
	db.session.delete(data)
	db.session.commit()
	return redirect('/insert')

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
   
if __name__ == '__main__':
   app.run(debug = True)