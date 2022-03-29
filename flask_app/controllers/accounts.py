import re
from turtle import st
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, director, instrument, marching_uniform, concert_uniform, account

# charge student account
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
    # todo Add validation
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


# edit charge and add payment
@app.route('/charge/edit/<int:id>')
def edit_charge(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    context = {
        "edit" : account.Account.get_one_charge(data),
    }
    return render_template("edit_charge_account.html", **context)

@app.route('/charge/update',methods=['POST'])
def update_charge():
    if 'director_id' not in session:
        return redirect('/logout')
    # todo add validation
    # if not student.Student.validate_student(request.form):
    #     return redirect(f'/student/edit/{student_id}') #todo LOOK INTO THIS!!!!!!!!
    student_id = request.form['student_id']
    account_info = {
        'id' : request.form['id'],
        'item_description' : request.form['item_description'],
        'item_cost' : request.form['item_cost'],
        'item_payment' : request.form['item_payment'],
        'student_id' : request.form['student_id']
    }
    # student.Student.update_student_information(student_info)
    account.Account.update_charge(account_info)
    return redirect(f'/account/view/{student_id}')

# view all accounts
@app.route('/accounts/view')
def view_accounts():
    if 'director_id' not in session:
        return redirect('/logout')
    context = {
        'all_students' : student.Student.get_student_accounts(),
    }
    return render_template('view_all_accounts.html', **context)

# view one account
@app.route('/account/view/<int:id>')
def view_one_account(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    context = {
        'charges' : account.Account.get_all_charges_for_one_student(data),
        'student' : student.Student.get_one_student(data),
        "cost" : account.Account.get_sum_item_cost(data),
        "payment" : account.Account.get_sum_item_payment(data)
    }
    return render_template('view_one_account.html', **context)