from flask_app import app
from flask_app.controllers import directors, students, accounts, music_libraries

if __name__ == '__main__':
    app.run(debug = True)