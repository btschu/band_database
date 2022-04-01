from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, account

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
    student_id = request.form['student_id']
    if not account.Account.validate_account(request.form):
        return redirect(f'/student/charge/{student_id}')
    data = {
        'item_description': request.form['item_description'],
        'item_cost': request.form['item_cost'],
        'item_payment': request.form['item_payment'],
        'student_id': request.form['student_id']
    }
    account.Account.charge_account(data)
    return redirect(f'/account/view/{student_id}')

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
    id = request.form['id']
    if not account.Account.validate_account(request.form):
        return redirect(f'/charge/edit/{id}')
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
@app.route('/accounts/view/all')
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
        'student' : student.Student.get_one_student(data)
    }
    return render_template('view_one_account.html', **context)

# delete transaction
@app.route('/charge/destroy/<int:id>')
def destroy_charge(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    account.Account.delete_charge(data)
    return redirect('/accounts/view/all')