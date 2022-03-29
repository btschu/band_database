import re
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, director, instrument

# view marching uniforms checked out to students
# @app.route('/view_student_marching_uniforms')
# def student_marching_uniforms():
#     if 'director_id' not in session:
#         return redirect('/logout')
#     context = {
#         "all_students" : student.Student.get_all_students(),
#     }
#     return render_template("view_student_marching_uniforms.html", **context)