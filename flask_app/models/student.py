from re import U
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import director
from pprint import pp, pprint

db = "music_program_database"

class Student:
    def __init__( self , data ):
        self.id = data['id']
        self.student_first_name = data['student_first_name']
        self.student_last_name = data['student_last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.director_id = data['director_id']
        self.school_id = data['school_id']

    @classmethod
    def add_new_student(cls,data):
        query = """
        INSERT INTO students (student_first_name, student_last_name, director_id, school_id)
        VALUES (%(student_first_name)s, %(student_last_name)s, %(director_id)s, %(school_id)s);"""
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_student_information(cls, data):
        query = """
        UPDATE students
        SET student_first_name=%(student_first_name)s, student_last_name=%(student_last_name)s, director_id=%(director_id)s, school_id=%(school_id)s
        WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def delete_student(cls,data):
        query = "DELETE FROM students WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all_students(cls):
        query = '''
        SELECT * FROM students
        LEFT JOIN instruments ON instruments.student_id = students.id
        LEFT JOIN concert_uniforms ON concert_uniforms.student_id = students.id
        LEFT JOIN marching_uniforms ON marching_uniforms.student_id = students.id
        LEFT JOIN financial_accounts ON financial_accounts.student_id = students.id
        LEFT JOIN pictures ON pictures.student_id = students.id'''
        results = connectToMySQL(db).query_db(query)
        all_students = []
        for row in results:
            all_students.append(cls(row))
        return all_students

    @classmethod
    def get_one_student(cls, data):
        query = """
        SELECT * FROM students
        WHERE id = %(id)s;"""
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_student(student):
        is_valid = True
        if len(student['student_first_name']) < 1:
            is_valid = False
            flash("Please enter a FIRST NAME.","student")
        if len(student['student_last_name']) == "":
            is_valid = False
            flash("Please enter a LAST NAME.","student")
        return is_valid