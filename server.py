from flask_app import app
from flask_app.controllers import directors, students, instruments, marching_uniforms, concert_uniforms, accounts

if __name__ == '__main__':
    app.run(debug = True)