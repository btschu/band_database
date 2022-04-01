from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = "music_program_database"

class Marching_Uniform:
    def __init__( self , data ):
        self.id = data['id']
        self.marching_jacket = data['marching_jacket']
        self.marching_pants = data['marching_pants']
        self.hat = data['hat']
        self.gauntlets = data['gauntlets']
        self.colorguard_uniform = data['colorguard_uniform']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.student_id = data['student_id']

    @classmethod
    def add_marching_uniform_to_student(cls,data):
        query = '''
        INSERT INTO marching_uniforms (marching_jacket, marching_pants, hat, gauntlets, colorguard_uniform, student_id)
        VALUES (%(marching_jacket)s, %(marching_pants)s, %(hat)s, %(gauntlets)s, %(colorguard_uniform)s, %(student_id)s);'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_marching_uniform_checked_out(cls, data):
        query = """
        UPDATE marching_uniforms
        SET marching_jacket=%(marching_jacket)s, marching_pants=%(marching_pants)s, hat=%(hat)s, gauntlets=%(gauntlets)s, colorguard_uniform=%(colorguard_uniform)s, student_id=%(student_id)s
        WHERE student_id = %(student_id)s;"""
        return connectToMySQL(db).query_db(query,data)