from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import director, student, instrument
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route("/login",methods=['POST'])
def director_login():
    data = {
        "director_email": request.form['director_email']
    }
    user = director.Director.get_by_email(data)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect("/")
    session['director_id'] = user.id
    session['director_email'] = user.director_email
    session['director_first_name'] = user.director_first_name
    session['director_last_name'] = user.director_last_name
    return redirect('/dashboard')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/register',methods=['POST'])
def register():
    if not director.Director.validate_director(request.form):
        return redirect('/registration')
    data ={
        "director_first_name": request.form['director_first_name'],
        "director_last_name": request.form['director_last_name'],
        "director_email": request.form['director_email'],
        "password": bcrypt.generate_password_hash(request.form['password']),
    }
    id = director.Director.add_new_director(data)
    session['director_id'] = id
    session['director_email'] = request.form['director_email']
    session['director_first_name'] = request.form['director_first_name']
    session['director_last_name'] = request.form['director_last_name']
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')