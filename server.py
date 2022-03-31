from flask_app import app
from flask_app.controllers import directors, students, instruments, marching_uniforms, concert_uniforms, accounts, music_libraries, lockers

if __name__ == '__main__':
    app.run(debug = True)