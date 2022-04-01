from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

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
        INSERT INTO school_instruments (instrument_type, instrument_serial_number, student_id)
        VALUES (%(instrument_type)s, %(instrument_serial_number)s, %(student_id)s);'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_instrument(cls, data):
        query = '''
        UPDATE school_instruments
        SET instrument_type=%(instrument_type)s, instrument_serial_number=%(instrument_serial_number)s, student_id=%(student_id)s
        WHERE student_id = %(student_id)s;'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all_instruments(cls):
        query = 'SELECT * FROM school_instruments;'
        results = connectToMySQL(db).query_db(query)
        all_instruments = []
        for row in results:
            all_instruments.append(cls(row))
        return all_instruments

    @classmethod
    def get_one_instrument(cls,data):
        query  = '''
        SELECT * FROM school_instruments
        WHERE id = %(id)s;'''
        result = connectToMySQL(db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def destroy_instrument(cls,data):
        query = 'DELETE FROM school_instruments WHERE id = %(id)s;'
        return connectToMySQL(db).query_db(query,data)