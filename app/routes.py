from flask import render_template, request, Blueprint, flash, redirect, url_for
from app.models.student import Student
from app.models import db

main_bp = Blueprint('main', __name__)

# Rota inicial
@main_bp.route('/')
def index():
    list_users = Student.query.all()
    return render_template('index.html', list_users=list_users)

@main_bp.route('/submit', methods=['POST'])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']

    student = Student(fname, lname, email)
    db.session.add(student)
    db.session.commit()

    studentsResult = db.session.query(Student).filter(Student.id==1)
    for result in studentsResult:
        print(result.fname)

    flash('Estudante Adcionado com sucesso')

    return redirect(url_for('main.index'))