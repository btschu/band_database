from re import U
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import director, student, locker
from pprint import pp, pprint

db = "music_program_database"

class Locker:
    def __init__( self , data ):
        self.id = data['id']
        self.locker_number = data['locker_number']
        self.lock_number = data['lock_number']
        self.combination = data['combination']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.student_id = data['student_id']

    @classmethod
    def save_locker(cls,data):
        query = '''
        INSERT INTO lockers (locker_number, lock_number, combination, student_id)
        VALUES (%(locker_number)s, %(lock_number)s, %(combination)s, Null);'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_locker(cls, data):
        query = '''
        UPDATE lockers
        SET locker_number=%(locker_number)s, lock_number=%(lock_number)s, combination=%(combination)s, student_id=Null
        ;'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all_lockers(cls):
        query = 'SELECT * FROM lockers'
        results = connectToMySQL(db).query_db(query)
        all_lockers = []
        for row in results:
            all_lockers.append(cls(row))
            pprint(row, sort_dicts= False)
        return all_lockers

    @classmethod
    def get_one_locker(cls,data):
        query  = '''
        SELECT * FROM lockers
        WHERE id = %(id)s;'''
        result = connectToMySQL(db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def destroy_locker(cls,data):
        query = 'DELETE FROM lockers WHERE id = %(id)s;'
        return connectToMySQL(db).query_db(query,data)
