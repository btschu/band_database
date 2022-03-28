from re import U
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import director, instrument, marching_uniform, concert_uniform, account
from pprint import pp, pprint

db = "music_program_database"

class Student:
    def __init__( self , data ):
        self.id = data['id']
        self.student_first_name = data['student_first_name']
        self.student_last_name = data['student_last_name']
        self.concert_instrument = data['concert_instrument']
        self.marching_instrument = data['marching_instrument']
        self.jazz_instrument = data['jazz_instrument']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.director_id = data['director_id']
        self.school_instruments = None
        self.lockers = None
        self.concert_uniforms = None
        self.marching_uniforms = None
        self.financial_accounts = None

    def student_full_name(self):
        student_full_name = f"{self.student_first_name} {self.student_last_name}"
        return student_full_name

    @classmethod
    def add_new_student(cls,data):
        query = """
        INSERT INTO students (student_first_name, student_last_name, concert_instrument, marching_instrument, jazz_instrument, director_id)
        VALUES (%(student_first_name)s, %(student_last_name)s, %(concert_instrument)s, %(marching_instrument)s, %(jazz_instrument)s, %(director_id)s);"""
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_student_information(cls, data):
        query = """
        UPDATE students
        SET student_first_name = %(student_first_name)s, student_last_name = %(student_last_name)s, concert_instrument = %(concert_instrument)s, marching_instrument = %(marching_instrument)s, jazz_instrument = %(jazz_instrument)s, director_id = %(director_id)s
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
        LEFT JOIN school_instruments ON school_instruments.student_id = students.id
        LEFT JOIN concert_uniforms ON concert_uniforms.student_id = students.id
        LEFT JOIN marching_uniforms ON marching_uniforms.student_id = students.id
        LEFT JOIN lockers ON lockers.student_id = students.id'''
        results = connectToMySQL(db).query_db(query)
        all_students = []
        for row in results:
            marching_uniform_info = {
                "id": row["marching_uniforms.id"],
                "marching_jacket": row["marching_jacket"],
                "marching_pants": row["marching_pants"],
                "hat": row["hat"],
                "gauntlets": row["gauntlets"],
                "colorguard_uniform": row["colorguard_uniform"],
                "created_at": row["marching_uniforms.created_at"],
                "updated_at": row["marching_uniforms.updated_at"],
                "student_id": row["marching_uniforms.student_id"]
            }
            concert_uniform_info = {
                "id": row["concert_uniforms.id"],
                "tux_coat": row["tux_coat"],
                "tux_pants": row["tux_pants"],
                "dress": row["dress"],
                "created_at": row["concert_uniforms.created_at"],
                "updated_at": row["concert_uniforms.updated_at"],
                "student_id": row["concert_uniforms.student_id"]
            }
            all_students.append(cls(row))
            all_students[-1].marching_uniforms = marching_uniform.Marching_Uniform(marching_uniform_info)
            all_students[-1].concert_uniforms = concert_uniform.Concert_Uniform(concert_uniform_info)
            pprint(row, sort_dicts= False)
        return all_students

    @classmethod
    def get_student_accounts(cls):
        query = '''
        SELECT * FROM students
        LEFT JOIN school_instruments ON school_instruments.student_id = students.id
        LEFT JOIN concert_uniforms ON concert_uniforms.student_id = students.id
        LEFT JOIN marching_uniforms ON marching_uniforms.student_id = students.id
        LEFT JOIN financial_accounts ON financial_accounts.student_id = students.id
        LEFT JOIN lockers ON lockers.student_id = students.id'''
        results = connectToMySQL(db).query_db(query)
        all_students = []
        for row in results:
            marching_uniform_info = {
                "id": row["marching_uniforms.id"],
                "marching_jacket": row["marching_jacket"],
                "marching_pants": row["marching_pants"],
                "hat": row["hat"],
                "gauntlets": row["gauntlets"],
                "colorguard_uniform": row["colorguard_uniform"],
                "created_at": row["marching_uniforms.created_at"],
                "updated_at": row["marching_uniforms.updated_at"],
                "student_id": row["marching_uniforms.student_id"]
            }
            concert_uniform_info = {
                "id": row["concert_uniforms.id"],
                "tux_coat": row["tux_coat"],
                "tux_pants": row["tux_pants"],
                "dress": row["dress"],
                "created_at": row["concert_uniforms.created_at"],
                "updated_at": row["concert_uniforms.updated_at"],
                "student_id": row["concert_uniforms.student_id"]
            }
            account_info = {
                'id' : row['financial_accounts.id'],
                'item_description' : row['item_description'],
                'item_cost' : row['item_cost'],
                'item_payment' : row['item_payment'],
                'created_at' : row['financial_accounts.created_at'],
                'updated_at' : row['financial_accounts.updated_at'],
                'student_id' : row['financial_accounts.student_id']
            }
            if row['financial_accounts.id']:
                all_students.append(cls(row))
                all_students[-1].marching_uniforms = marching_uniform.Marching_Uniform(marching_uniform_info)
                all_students[-1].concert_uniforms = concert_uniform.Concert_Uniform(concert_uniform_info)
                all_students[-1].financial_accounts = account.Account(account_info)
            pprint(row, sort_dicts= False)
        return all_students

    @classmethod
    def get_one_student(cls, data):
        query = """
        SELECT * FROM students
        LEFT JOIN school_instruments ON school_instruments.student_id = students.id
        LEFT JOIN concert_uniforms ON concert_uniforms.student_id = students.id
        LEFT JOIN marching_uniforms ON marching_uniforms.student_id = students.id
        LEFT JOIN financial_accounts ON financial_accounts.student_id = students.id
        LEFT JOIN lockers ON lockers.student_id = students.id
        WHERE students.id = %(id)s;"""
        results = connectToMySQL(db).query_db(query, data)
        all_students = []
        for row in results:
            marching_uniform_info = {
                "id": row["marching_uniforms.id"],
                "marching_jacket": row["marching_jacket"],
                "marching_pants": row["marching_pants"],
                "hat": row["hat"],
                "gauntlets": row["gauntlets"],
                "colorguard_uniform": row["colorguard_uniform"],
                "created_at": row["marching_uniforms.created_at"],
                "updated_at": row["marching_uniforms.updated_at"],
                "student_id": row["marching_uniforms.student_id"]
            }
            concert_uniform_info = {
                "id": row["concert_uniforms.id"],
                "tux_coat": row["tux_coat"],
                "tux_pants": row["tux_pants"],
                "dress": row["dress"],
                "created_at": row["concert_uniforms.created_at"],
                "updated_at": row["concert_uniforms.updated_at"],
                "student_id": row["concert_uniforms.student_id"]
            }
            account_info = {
                'id' : row['financial_accounts.id'],
                'item_description' : row['item_description'],
                'item_cost' : row['item_cost'],
                'item_payment' : row['item_payment'],
                'created_at' : row['financial_accounts.created_at'],
                'updated_at' : row['financial_accounts.updated_at'],
                'student_id' : row['financial_accounts.student_id']
            }
        all_students.append(cls(row))
        all_students[-1].marching_uniforms = marching_uniform.Marching_Uniform(marching_uniform_info)
        all_students[-1].concert_uniforms = concert_uniform.Concert_Uniform(concert_uniform_info)
        if row['financial_accounts.student_id'] == all_students[-1].id:
            all_students[-1].financial_accounts = account.Account(account_info)
        student = all_students[0]
        pprint(row, sort_dicts=False)
        return student

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