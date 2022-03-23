import re
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, director

@app.route('/dashboard')
def dashboard():
    if 'director_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['director_id'],
    }
    context = {
        "all_students" : student.Student.get_all_students(),
    }
    return render_template("index.html", **context)

@app.route('/student/new')
def new_student():
    if 'director_id' not in session:
        return redirect('/logout')
    return render_template('create_student.html')

@app.route('/student/create',methods=['POST'])
def create_student():
    if 'director_id' not in session:
        return redirect('/logout')
    if not student.Student.validate_student(request.form):
        return redirect('/student/new')
    data = {
        "student_first_name": request.form["student_first_name"],
        "student_last_name": request.form["student_last_name"],
        "director_id": session["school_id"],
        "school_id": session["school_id"]
    }
    student.Student.add_new_student(data)
    return redirect('/dashboard')

@app.route('/student/edit/<int:id>')
def edit_student(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    context = {
        "edit" : student.Student.get_one_student(data),
    }
    return render_template("edit_student.html", **context)

@app.route('/student/update',methods=['POST'])
def update_student():
    if 'user_id' not in session:
        return redirect('/logout')
    student_id = request.form['id']
    if not student.Student.validate_student(request.form):
        return redirect(f'/student/edit/{student_id}')
    data = {
        "id": request.form['id'],
        "student_first_name": request.form["student_first_name"],
        "student_last_name": request.form["student_last_name"],
        "school_id": session['school_id']
    }
    student.Student.update_student_information(data)
    return redirect('/dashboard')

@app.route('/student/view/<int:id>')
def view_student(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id,
        "director_id":session['director_id'],
    }
    context = {
        "student" : student.Student.get_one_student(data)
    }
    return render_template("view_student.html", **context)

@app.route('/student/destroy/<int:id>')
def destroy_student(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    student.Student.delete_student(data)
    return redirect('/dashboard')