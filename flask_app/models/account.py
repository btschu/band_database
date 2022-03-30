from re import U
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import student, director, instrument, marching_uniform, concert_uniform
from pprint import pprint

db = "music_program_database"

class Account:
    def __init__( self , data ):
        self.id = data['id']
        self.item_description = data['item_description']
        self.item_cost = data['item_cost']
        self.item_payment = data['item_payment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.student_id = data['student_id']

    def account_balance(self):
        account_balance = 0
        self.item_cost += account_balance
        return account_balance

    @classmethod
    def charge_account(cls,data):
        query = '''
        INSERT INTO financial_accounts (item_description, item_cost, item_payment, student_id)
        VALUES (%(item_description)s, %(item_cost)s, %(item_payment)s, %(student_id)s);'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_charge(cls, data):
        query = '''
        UPDATE financial_accounts
        SET item_description=%(item_description)s, item_cost=%(item_cost)s, item_payment=%(item_payment)s, student_id=%(student_id)s
        WHERE financial_accounts.id = %(id)s;'''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_one_charge(cls, data):
        query = '''
        SELECT * FROM financial_accounts
        JOIN students ON students.id = financial_accounts.student_id
        WHERE financial_accounts.id = %(id)s;'''
        results = connectToMySQL(db).query_db(query, data)
        student_info = {
            "id": results[0]['id'],
            "student_first_name": results[0]["student_first_name"],
            "student_last_name": results[0]["student_last_name"],
            "concert_instrument": results[0]["concert_instrument"],
            "marching_instrument": results[0]["marching_instrument"],
            "jazz_instrument": results[0]["jazz_instrument"],
            "created_at": results[0]["created_at"],
            "updated_at": results[0]["updated_at"],
            "director_id": results[0]["director_id"]
        }
        this_charge = cls(results[0])
        this_charge.financial_accounts = student.Student(student_info)
        pprint(results)
        pprint(this_charge.financial_accounts)
        return this_charge

    @classmethod
    def get_all_charges_for_one_student(cls, data):
        query = '''
        SELECT * FROM financial_accounts
        LEFT JOIN students ON students.id = financial_accounts.student_id
        WHERE students.id = %(id)s;'''
        results = connectToMySQL(db).query_db(query, data)
        this_charge = []
        for row in results:
            student_info = {
                "id": row['id'],
                "student_first_name": row["student_first_name"],
                "student_last_name": row["student_last_name"],
                "concert_instrument": row["concert_instrument"],
                "marching_instrument": row["marching_instrument"],
                "jazz_instrument": row["jazz_instrument"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "director_id": row["director_id"]
            }
            this_charge.append(cls(row))
            this_charge[-1].financial_accounts = (student.Student(student_info))
            pprint(row,sort_dicts = False)
        return this_charge

    @classmethod
    def delete_charge(cls,data):
        query = "DELETE FROM financial_accounts WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)