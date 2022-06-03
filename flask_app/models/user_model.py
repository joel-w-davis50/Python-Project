from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.models import company_model
from flask_app.models import user_model
from flask_app.models import user_model
import re	  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'HVAC_Estimate_Website'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.company_id=data['company_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.jobs= []

    @classmethod
    def register_user(cls,data):
        query= "INSERT INTO users (first_name, last_name, email, password, created_at, company_id ) VALUES( %(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(), %(company_id)s );"
        return MySQLConnection(cls.db).query_db(query,data)

    @staticmethod
    def validate_registration(user_model):
        is_valid = True # we assume this is true
        if len(user_model['first_name']) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False
        if len(user_model['last_name']) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False
        if len(user_model['password']) < 7:
            flash("Password must be at least 8 characters long.")
            is_valid = False
        if user_model['password'] !=user_model['confirm_password']:
            flash("Password and Confirm Password must match.")
            is_valid = False
        if not EMAIL_REGEX.match(user_model['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email_user(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = MySQLConnection(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0]) 

    @classmethod
    def get_one_user(cls,data):
        query='SELECT * FROM users WHERE id=%(id)s '
        result = MySQLConnection(cls.db).query_db(query,data)
        return cls(result[0])