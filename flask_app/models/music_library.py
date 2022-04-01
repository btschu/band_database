from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pprint import pprint

db = "music_program_database"

class Music_Library:
    def __init__( self , data ):
        self.id = data['id']
        self.number = data['number']
        self.song_title = data['song_title']
        self.composer_first_name = data['composer_first_name']
        self.composer_last_name = data['composer_last_name']
        self.arranger_first_name = data['arranger_first_name']
        self.arranger_last_name = data['arranger_last_name']
        self.difficulty_level = data['difficulty_level']
        self.genre = data['genre']
        self.ensemble_type = data['ensemble_type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_library(cls,data):
        query = '''
        INSERT INTO music_libraries (number, song_title, composer_first_name, composer_last_name, arranger_first_name, arranger_last_name, difficulty_level, genre, ensemble_type)
        VALUES (%(number)s, %(song_title)s, %(composer_first_name)s, %(composer_last_name)s, %(arranger_first_name)s, %(arranger_last_name)s, %(difficulty_level)s, %(genre)s, %(ensemble_type)s);'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_library(cls, data):
        query = '''
        UPDATE music_libraries
        SET number=%(number)s, song_title=%(song_title)s, composer_first_name=%(composer_first_name)s, composer_last_name=%(composer_last_name)s, arranger_first_name=%(arranger_first_name)s, arranger_last_name=%(arranger_last_name)s, arranger_first_name=%(arranger_first_name)s, difficulty_level=%(difficulty_level)s, genre=%(genre)s, ensemble_type=%(ensemble_type)s
        WHERE id = %(id)s;'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all_titles(cls):
        query = 'SELECT * FROM music_libraries'
        results = connectToMySQL(db).query_db(query)
        all_titles = []
        for row in results:
            all_titles.append(cls(row))
            pprint(row, sort_dicts= False)
        return all_titles

    @classmethod
    def get_one_title(cls,data):
        query  = '''
        SELECT * FROM music_libraries
        WHERE id = %(id)s;'''
        result = connectToMySQL(db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def destroy_library(cls,data):
        query = 'DELETE FROM music_libraries WHERE id = %(id)s;'
        return connectToMySQL(db).query_db(query,data)

    @staticmethod
    def validate_library(library):
        is_valid = True
        if len(library['number']) < 1:
            is_valid = False
            flash("Please enter a LIBRARY NUMBER.","library")
        if len(library['song_title']) < 1:
            is_valid = False
            flash("Please enter a SONG TITLE.","library")
        if len(library['ensemble_type']) < 1:
            is_valid = False
            flash("Please enter an ENSEMBLE TYPE.","library")
        return is_valid