from app import app
from flask import render_template, request
from models.student import Student
from models import db

# Rota inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']

    studant = Student(fname, lname, email)
    db.session.add(studant)
    db.session.commit()

    studentsResult = db.session.query(Student).filter(Student.id==1)
    for result in studentsResult:
        print(result.fname)

    return render_template('success.html', data=fname)