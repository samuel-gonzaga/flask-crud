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
    fname = request.form['fname'].strip()
    lname = request.form['lname'].strip()
    email = request.form['email'].strip()

    if not fname or not lname or not email:
        flash('Todos os campos são obrigatórios.')
        return redirect(request.referrer)

    student = Student(fname, lname, email)
    db.session.add(student)
    db.session.commit()

    studentsResult = db.session.query(Student).filter(Student.id==1)
    for result in studentsResult:
        print(result.fname)

    flash('Estudante Adcionado com sucesso')

    return redirect(url_for('main.index'))

@main_bp.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    student = Student.query.get_or_404(id)
    return render_template('edit.html', student=student)

@main_bp.route('/update/<id>', methods=['POST'])
def update(id):
    fname = request.form['fname'].strip()
    lname = request.form['lname'].strip()
    email = request.form['email'].strip()

    if not fname or not lname or not email:
        flash('Todos os campos são obrigatórios.')
        return redirect(request.referrer)

    student = Student.query.get_or_404(id)

    student.fname = fname
    student.lname = lname
    student.email = email

    db.session.commit()

    flash("Estudante alterado com sucesso")

    return redirect(url_for('main.index'))

@main_bp.route('/delete/<string:id>', methods=['GET', 'POST'])
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()

    flash("Estudante deletado com sucesso")

    return redirect(url_for('main.index'))