import re
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
        'item_date': request.form['item_date'],
        'item_description': request.form['item_description'],
        'item_cost': request.form['item_cost'],
        'item_payment': request.form['item_payment'],
        'student_id': request.form['student_id']
    }
    account.Account.charge_account(data)
    return redirect('/dashboard')