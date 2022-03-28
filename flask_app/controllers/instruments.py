import re
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, director, instrument

@app.route('/view/student/instruments')
def view_student_instruments():
    if 'director_id' not in session:
        return redirect('/logout')
    context = {
        "all_students" : student.Student.get_all_students(),
    }
    return render_template("view_student_instruments.html", **context)