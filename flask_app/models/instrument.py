from re import U
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import director, student, instrument
from pprint import pp, pprint

db = "music_program_database"

class Instrument:
    def __init__( self , data ):
        self.id = data['id']
        self.instrument_type = data['instrument_type']
        self.instrument_serial_number = data['instrument_serial_number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.student_id = data['student_id']

    @classmethod
    def add_new_instrument(cls,data):
        query = '''
        INSERT INTO instruments (instrument_type, instrument_serial_number, student_id)
        VALUES (%(instrument_type)s, %(instrument_serial_number)s, %(student_id)s);'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_instrument(cls, data):
        query = '''
        UPDATE instruments
        SET instrument_type=%(instrument_type)s, instrument_serial_number=%(instrument_serial_number)s, student_id=%(student_id)s
        WHERE id = %(id)s;'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all_instruments(cls):
        query = 'SELECT * FROM instruments;'
        results = connectToMySQL(db).query_db(query)
        all_instruments = []
        for row in results:
            all_instruments.append(cls(row))
        return all_instruments

    @classmethod
    def destroy_instrument(cls,data):
        query = 'DELETE FROM instruments WHERE id = %(id)s;'
        return connectToMySQL(db).query_db(query,data)