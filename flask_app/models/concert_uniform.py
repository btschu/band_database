from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = "music_program_database"

class Concert_Uniform:
    def __init__( self , data ):
        self.id = data['id']
        self.tux_coat = data['tux_coat']
        self.tux_pants = data['tux_pants']
        self.dress = data['dress']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.student_id = data['student_id']

    @classmethod
    def add_concert_uniform_to_student(cls,data):
        query = '''
        INSERT INTO concert_uniforms (tux_coat, tux_pants, dress, student_id)
        VALUES (%(tux_coat)s, %(tux_pants)s, %(dress)s, %(student_id)s);'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_concert_uniform_checked_out(cls, data):
        query = """
        UPDATE concert_uniforms
        SET tux_coat=%(tux_coat)s, tux_pants=%(tux_pants)s, dress=%(dress)s, student_id=%(student_id)s
        WHERE student_id = %(student_id)s;"""
        return connectToMySQL(db).query_db(query,data)