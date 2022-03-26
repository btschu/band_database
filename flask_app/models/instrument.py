from re import U
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import director, student
from pprint import pp, pprint

db = "music_program_database"

# class Instrument:
#     def __init__( self , data ):
#         self.id = data['id']
#         self.primary_instrument = data['primary_instrument']
#         self.secondary_instrument = data['secondary_instrument']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#         self.student_id = data['student_id']

    # @classmethod
    # def add_new_instrument(cls,data):
    #     query = '''
    #     INSERT INTO instruments (primary_instrument, secondary_instrument, student_id)
    #     VALUES (%(primary_instrument)s, %(secondary_instrument)s, %(student_id)s);'''
    #     return connectToMySQL(db).query_db(query,data)

    # @classmethod
    # def update_instrument(cls, data):
    #     query = '''
    #     UPDATE instruments
    #     SET primary_instrument=%(primary_instrument)s, secondary_instrument=%(secondary_instrument)s, student_id=%(student_id)s
    #     WHERE id = %(id)s;'''
    #     return connectToMySQL(db).query_db(query,data)