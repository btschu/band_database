import re
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, director, instrument, music_library

@app.route('/library/new')
def new_library():
    if 'director_id' not in session:
        return redirect('/logout')
    return render_template('create_music_library.html')

@app.route('/library/create',methods=['POST'])
def create_library():
    if 'director_id' not in session:
        return redirect('/logout')
    # todo add validation
    # if not *****.validate_*****(request.form):
    #     return redirect('/*****/new')
    data = {
        'number': request.form['number'],
        'song_title': request.form['song_title'],
        'composer_first_name': request.form['composer_first_name'],
        'composer_last_name': request.form['composer_last_name'],
        'arranger_first_name': request.form['arranger_first_name'],
        'arranger_last_name': request.form['arranger_last_name'],
        'difficulty_level': request.form['difficulty_level'],
        'genre': request.form['genre'],
        'ensemble_type': request.form['ensemble_type']
    }
    music_library.Music_Library.save_library(data)
    return redirect('/library/view/all')

@app.route('/library/edit/<int:id>')
def edit_library(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    context = {
        "edit" : music_library.Music_Library.get_one_title(data)
    }
    return render_template("edit_music_library.html", **context)

@app.route('/library/update',methods=['POST'])
def update_library():
    if 'director_id' not in session:
        return redirect('/logout')
    # todo add validation
    # if not student.Student.validate_student(request.form):
    #     return redirect(f'/student/edit/{student_id}') #todo LOOK INTO THIS!!!!!!!! and line 72
    library_info = {
        "id": request.form['id'],
        "number": request.form["number"],
        "song_title": request.form["song_title"],
        "composer_first_name": request.form["composer_first_name"],
        "composer_last_name": request.form["composer_last_name"],
        "arranger_first_name": request.form["arranger_first_name"],
        "arranger_last_name": request.form["arranger_last_name"],
        "difficulty_level": request.form["difficulty_level"],
        "genre": request.form["genre"],
        "ensemble_type": request.form["ensemble_type"],
    }
    music_library.Music_Library.update_library(library_info)
    return redirect('/library/view/all')

@app.route('/library/view/all')
def view_full_library():
    if 'director_id' not in session:
        return redirect('/logout')
    context = {
        'all_titles' : music_library.Music_Library.get_all_titles(),
    }
    return render_template('view_all_databases.html', **context)

@app.route('/library/destroy/<int:id>')
def destroy_library(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        'id':id
    }
    music_library.Music_Library.destroy_library(data)
    return redirect('/library/view/all')