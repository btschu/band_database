from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = "music_program_database"

class Director:
    def __init__( self , data ):
        self.id = data['id']
        self.director_first_name = data['director_first_name']
        self.director_last_name = data['director_last_name']
        self.director_email = data['director_email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def director_full_name(self):
        director_full_name = f"{self.director_first_name} {self.director_last_name}"
        return director_full_name

    @classmethod
    def add_new_director(cls,data):
        query = """INSERT INTO directors (director_first_name, director_last_name, director_email, password)
        VALUES(%(director_first_name)s, %(director_last_name)s, %(director_email)s, %(password)s)"""
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = """
        SELECT * FROM directors
        WHERE director_email = %(director_email)s;"""
        results = connectToMySQL(db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_director(director):
        is_valid = True
        query = """
        SELECT * FROM directors
        WHERE director_email = %(director_email)s;"""
        results = connectToMySQL(db).query_db(query,director)
        if len(director['director_first_name']) < 1:
            flash("Please enter your FIRST NAME.","register")
            is_valid= False
        if len(director['director_last_name']) < 1:
            flash("Please enter your LAST NAME","register")
            is_valid= False
        if len(results) >= 1:
            flash("That EMAIL ADDRESS is already registered.","register")
            is_valid=False
        if not EMAIL_REGEX.match(director['director_email']):
            flash("Please enter a valid EMAIL ADDRESS.","login")
            is_valid=False
        if len(director['password']) < 8:
            flash("Your PASSWORD must be at least 8 characters long.","register")
            is_valid = False
        if not any(char.isdigit() for char in director['password']):
            flash("Your PASSWORD must contain at least one number.", "register")
            is_valid = False
        if not any(char.isupper() for char in director['password']):
            flash("Your PASSWORD must contain at least one uppercase letter.", "register")
            is_valid = False
        if director['password'] != director['confirm']:
            flash("Your PASSWORDS do not match.","register")
            is_valid = False
        return is_valid
