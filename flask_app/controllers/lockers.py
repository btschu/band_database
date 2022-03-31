import re
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, director, instrument, music_library, locker

@app.route('/locker/new')
def new_locker():
    if 'director_id' not in session:
        return redirect('/logout')
    return render_template('create_locker.html')

@app.route('/locker/create',methods=['POST'])
def create_locker():
    if 'director_id' not in session:
        return redirect('/logout')
    # todo add validation
    # if not *****.validate_*****(request.form):
    #     return redirect('/*****/new')
    data = {
        'locker_number': request.form['locker_number'],
        'lock_number': request.form['lock_number'],
        'combination': request.form['combination'],
        'student_id': request.form['student_id']
    }
    locker.Locker.save_locker(data)
    return redirect('/locker/view/all')

@app.route('/locker/edit/<int:id>')
def edit_locker(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    context = {
        "edit" : locker.Locker.get_one_locker(data)
    }
    return render_template("edit_locker.html", **context)

@app.route('/locker/update',methods=['POST'])
def update_locker():
    if 'director_id' not in session:
        return redirect('/logout')
    # todo add validation
    # if not student.Student.validate_student(request.form):
    #     return redirect(f'/student/edit/{student_id}') #todo LOOK INTO THIS!!!!!!!! and line 72
    locker_info = {
        "id":id,
        "locker_number": request.form["locker_number"],
        "lock_number": request.form["lock_number"],
        "combination": request.form["combination"],
        "student_id": request.form["student_id"]
    }
    locker.Locker.update_locker(locker_info)
    return redirect('/locker/view/all')

@app.route('/locker/view/all')
def view_all_lockers():
    if 'director_id' not in session:
        return redirect('/logout')
    context = {
        'all_lockers' : locker.Locker.get_all_lockers(),
    }
    return render_template('view_all_databases.html', **context)

@app.route('/locker/destroy/<int:id>')
def destroy_locker(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        'id':id
    }
    locker.Locker.destroy_locker(data)
    return redirect('/locker/view/all')