from re import U
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import director, instrument, marching_uniform, concert_uniform
from pprint import pp, pprint

db = "music_program_database"

class Account:
    def __init__( self , data ):
        self.id = data['id']
        self.item_date = data['item_date']
        self.item_description = data['item_description']
        self.item_cost = data['item_cost']
        self.item_payment = data['item_payment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.student_id = data['student_id']

    @classmethod
    def charge_account(cls,data):
        query = '''
        INSERT INTO financial_accounts (item_date, item_description, item_cost, item_payment, student_id)
        VALUES (%(item_date)s, %(item_description)s, %(item_cost)s, %(item_payment)s, %(student_id)s);'''
        return connectToMySQL(db).query_db(query,data)