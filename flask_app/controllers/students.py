from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, instrument, marching_uniform, concert_uniform

# create new student with instruments and uniform information
@app.route('/student/new')
def new_student():
    if 'director_id' not in session:
        return redirect('/logout')
    context = {
        'all_students' : student.Student.get_all_students()
    }
    return render_template('create_student.html', **context)

@app.route('/student/create',methods=['POST'])
def create_student():
    if 'director_id' not in session:
        return redirect('/logout')
    # todo add more validation
    if not student.Student.validate_student(request.form):
        return redirect('/student/new')
    student_info = {
        "id": id,
        "student_first_name": request.form["student_first_name"],
        "student_last_name": request.form["student_last_name"],
        "concert_instrument": request.form["concert_instrument"],
        "marching_instrument": request.form["marching_instrument"],
        "jazz_instrument": request.form["jazz_instrument"],
        "director_id": session["director_id"],
    }
    student_id = student.Student.add_new_student(student_info)
    marching_uniform_info = {
        "marching_jacket": request.form["marching_jacket"],
        "marching_pants": request.form["marching_pants"],
        "marching_pants": request.form["marching_pants"],
        "hat": request.form["hat"],
        "gauntlets": request.form["gauntlets"],
        "colorguard_uniform": request.form["colorguard_uniform"],
        "student_id": student_id
    }
    concert_uniform_info = {
        "tux_coat": request.form["tux_coat"],
        "tux_pants": request.form["tux_pants"],
        "dress": request.form["dress"],
        "student_id": student_id
    }
    school_instrument_info = {
        "instrument_type": request.form["instrument_type"],
        "instrument_serial_number": request.form["instrument_serial_number"],
        "student_id": student_id
    }
    concert_uniform.Concert_Uniform.add_concert_uniform_to_student(concert_uniform_info)
    marching_uniform.Marching_Uniform.add_marching_uniform_to_student(marching_uniform_info)
    instrument.Instrument.add_new_instrument(school_instrument_info)
    return redirect('/students/view/all')

# edit student, instruments and uniform info
@app.route('/student/edit/<int:id>')
def edit_student(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    context = {
        "edit" : student.Student.get_one_student(data)
    }
    return render_template("view_one_student.html", **context)

@app.route('/student/update',methods=['POST'])
def update_student():
    if 'director_id' not in session:
        return redirect('/logout')
    # todo add validation
    # if not student.Student.validate_student(request.form):
    #     return redirect(f'/student/edit/{student_id}') #todo LOOK INTO THIS!!!!!!!! and line 72
    student_info = {
        "id": request.form['id'],
        "student_first_name": request.form["student_first_name"],
        "student_last_name": request.form["student_last_name"],
        "concert_instrument": request.form["concert_instrument"],
        "marching_instrument": request.form["marching_instrument"],
        "jazz_instrument": request.form["jazz_instrument"],
        "director_id": session["director_id"],
    }
    marching_uniform_info = {
        "marching_jacket": request.form["marching_jacket"],
        "marching_pants": request.form["marching_pants"],
        "marching_pants": request.form["marching_pants"],
        "hat": request.form["hat"],
        "gauntlets": request.form["gauntlets"],
        "colorguard_uniform": request.form["colorguard_uniform"],
        "student_id": request.form["student_id"]
    }
    concert_uniform_info = {
        "tux_coat": request.form["tux_coat"],
        "tux_pants": request.form["tux_pants"],
        "dress": request.form["dress"],
        "student_id": request.form["student_id"]
    }
    school_instrument_info = {
        "instrument_type": request.form["instrument_type"],
        "instrument_serial_number": request.form["instrument_serial_number"],
        "student_id": request.form["student_id"]
    }
    student.Student.update_student_information(student_info)
    marching_uniform.Marching_Uniform.update_marching_uniform_checked_out(marching_uniform_info)
    concert_uniform.Concert_Uniform.update_concert_uniform_checked_out(concert_uniform_info)
    instrument.Instrument.update_instrument(school_instrument_info)
    return redirect('/students/view/all')

# view all students
@app.route('/students/view/all')
def view_all_students():
    if 'director_id' not in session:
        return redirect('/logout')
    context = {
        "all_students" : student.Student.get_all_students()
    }
    return render_template("view_all_students.html", **context)

# delete student and all information associated with it
@app.route('/student/destroy/<int:id>')
def destroy_student(id):
    if 'director_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    student.Student.delete_student(data)
    return redirect('/students/view/all')

