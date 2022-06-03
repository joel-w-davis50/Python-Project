from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.models import company_model
from flask_app.models import user_model
from flask_app.models import user_model
import re	  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Job:
    db = 'HVAC_Estimate_Website'
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.company_id = data['company_id']
        self.name = data['name']
        self.address = data['address']
        self.total_cost = data['total_cost']
        self.bedrooms = data['bedrooms']
        self.livingareas = data['livingareas']
        self.kitchen = data['kitchen']
        self.bathrooms = data['bathrooms']
        self.dinning_room = data['dinning_room']
        self.customer_request = data['customer_request']
        self.material_cost = data['material_cost']
        self.labor_cost = data['labor_cost']
        self.material_supplier = data['material_supplier']
        self.order_date_material = data['order_date_material']
        self.pick_up_material = data['pick_up_material']
        self.material_ordered_list = data['material_ordered_list']
        self.total_square_foot = data['total_square_foot']
        self.address_city = data['address_city']
        self.address_state = data['address_state']
        self.address_zip = data['address_zip']
        self.file = data['file']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_job(cls,data):
        query= 'INSERT INTO jobs (created_at, name, address, total_cost, bedrooms, livingareas, kitchen, bathrooms, dinning_room, customer_request, material_cost, labor_cost, material_supplier, order_date_material, pick_up_material,material_ordered_list, total_square_foot, address_city, address_state, address_zip, file, user_id,company_id) VALUES(  NOW(), %(name)s, %(address)s, %(total_cost)s, %(bedrooms)s, %(livingareas)s, %(kitchen)s, %(bathrooms)s, %(dinning_room)s, %(customer_request)s, %(material_cost)s, %(labor_cost)s, %(material_supplier)s, %(order_date_material)s, %(pick_up_material)s, %(material_ordered_list)s, %(total_square_foot)s, %(address_city)s, %(address_state)s, %(address_zip)s, %(file)s, %(user_id)s, %(company_id)s);'
        return MySQLConnection(cls.db).query_db(query, data)

    @staticmethod
    def validate_create_job(jobs_models):
        is_valid = True # we assume this is true
        if len(jobs_models['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(jobs_models['filling']) < 3:
            flash("Filling must be at least 3 characters.")
            is_valid = False
        if len(jobs_models['crust'])<3:
            flash("Crust must be at least 3 characters long")
            is_valid= False
        return is_valid
    #view all jobs and users info
    @classmethod
    def get_all_jobs(cls):
        query='SELECT * FROM jobs LEFT JOIN users ON users.id = jobs.user_id '
        results = MySQLConnection(cls.db).query_db(query)
        print(results)
        all_jobs=[]
        for row in results:
            job = cls(row)
            print(job,'line 70')
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
                'company_id' : row['users.company_id']
            }
            job.user = user_model.User(user_data)
            all_jobs.append(job)
        # print(job)
        return all_jobs
    #view one job and user info
    @classmethod
    def view_one_job(cls,data):
        query='SELECT * FROM jobs LEFT JOIN users ON users.id = jobs.user_id WHERE jobs.id=%(id)s'
        results= MySQLConnection(cls.db).query_db(query, data)
        job=cls(results[0])
        user_data={
            'id': results[0]['users.id'],
            'first_name': results[0]['first_name'],
            'last_name': results[0]['last_name'],
            'email': results[0]['email'],
            'company_id': results[0]['company_id'],
            'password': results[0]['password'],
            'created_at': results[0]['users.created_at'],
            'updated_at': results[0]['users.updated_at'],
        }
        job.user=user_model.User(user_data)
        return job

    @classmethod
    def update_job(cls,data):
        query='UPDATE jobs SET name = %(name)s, address=%(address)s, total_cost = %(total_cost)s, updated_at = NOW(), bedrooms = %(bedrooms)s, kitchen = %(kitchen)s, bathrooms = %(bathrooms)s, dinning_room = %(dinning_room)s, customer_request = %(customer_request)s, material_cost = %(material_cost)s, labor_cost = %(labor_cost)s, material_supplier = %(material_supplier)s, order_date_material = %(order_date_material)s, pick_up_material = %(pick_up_material)s, material_ordered_list = %(material_ordered_list)s, total_square_foot = %(total_square_foot)s, address_city = %(address_city)s, address_state = %(address_state)s, address_zip = %(address_zip)s, file = %(file)s  WHERE id=%(id)s;'
        return MySQLConnection(cls.db).query_db(query, data)

    @classmethod
    def delete_job(cls,data):
        query='DELETE FROM jobs WHERE id=%(id)s'
        return MySQLConnection(cls.db).query_db(query,data)


    