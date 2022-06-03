from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.models import company_model
from flask_app.models import user_model
from flask_app.models import company_model
import re	  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Company:
    db = 'HVAC_Estimate_Website'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def register_company(cls,data):
        query= "INSERT INTO companies (name, email, password, created_at ) VALUES( %(name)s,%(email)s,%(password)s,NOW() );"
        return MySQLConnection(cls.db).query_db(query,data)

    @staticmethod
    def validate_registration_company(company_model):
        is_valid = True # we assume this is true
        if len(company_model['name']) < 2:
            flash("Company Name must be at least 2 characters.")
            is_valid = False
        if len(company_model['password']) < 7:
            flash("Password must be at least 8 characters long.")
            is_valid = False
        if company_model['password'] !=company_model['confirm_password']:
            flash("Password and Confirm Password must match.")
            is_valid = False
        if not EMAIL_REGEX.match(company_model['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email_company(cls,data):
        query = "SELECT * FROM companies WHERE email = %(email)s;"
        result = MySQLConnection(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0]) 

    @classmethod
    def get_one_company(cls,data):
        query='SELECT * FROM companies WHERE id=%(id)s '
        result = MySQLConnection(cls.db).query_db(query,data)
        return cls(result[0])
