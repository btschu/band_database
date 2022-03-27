import re
from turtle import st
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, director, instrument, marching_uniform, concert_uniform, account

@app.route('/student/charge/<int:id>')
def charge_account(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    context = {
        "student" : student.Student.get_one_student(data),
    }
    return render_template('charge_account.html', **context)

@app.route('/student/charge',methods=['POST'])
def create_student_charge():
    if 'director_id' not in session:
        return redirect('/logout')
    # if not *****.validate_*****(request.form):
    #     return redirect('/*****/new')
    data = {
        'item_description': request.form['item_description'],
        'item_cost': request.form['item_cost'],
        'item_payment': request.form['item_payment'],
        'student_id': request.form['student_id']
    }
    account.Account.charge_account(data)
    return redirect('/accounts/view')

@app.route('/accounts/view')
def view_accounts():
    if 'director_id' not in session:
        return redirect('/logout')
    context = {
        'all_students' : student.Student.get_student_accounts(),
    }
    return render_template('view_student_accounts.html', **context)

@app.route('/charge/edit/<int:id>')
def edit_charge(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    context = {
        "edit" : student.Student.get_one_charge(data),
    }
    return render_template("edit_charge_account.html", **context)

@app.route('/charge/update',methods=['POST'])
def update_charge():
    if 'director_id' not in session:
        return redirect('/logout')
    # student_id = id
    # if not student.Student.validate_student(request.form):
    #     return redirect(f'/student/edit/{student_id}') #todo LOOK INTO THIS!!!!!!!!
    account_info = {
        'id' : request.form['id'],
        'item_description' : request.form['item_description'],
        'item_cost' : request.form['item_cost'],
        'item_payment' : request.form['item_payment'],
        'student_id' : request.form['student_id']
    }
    # student.Student.update_student_information(student_info)
    account.Account.update_charge(account_info)
    return redirect('/accounts/view')