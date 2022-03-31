import re
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import student, director, instrument

@app.route('/view/instruments/all')
def view_all_instruments():
    if 'director_id' not in session:
        return redirect('/logout')
    context = {
        "all_instruments" : instrument.Instrument.get_all_instruments(),
    }
    return render_template("view_all_databases.html", **context)