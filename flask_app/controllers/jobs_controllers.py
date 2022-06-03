from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

from flask import render_template, request, redirect, session,flash

from flask_app.models.company_model import Company
from flask_app.models.job_model import Job
from flask_app.models.user_model import User

def check_user():
    if 'user_id' not in session:
        return redirect('/')

@app.route('/create_job')
def create_job():
    return render_template('create_job.html')

@app.route('/process_create_job', methods=['post'])
def process_create_job():

# bedrooms accordian

    bedroom1_length=int(request.form['bedroom1_length'])
    bedroom1_width=int(request.form['bedroom1_width'])
    bedroom1_results=bedroom1_width*bedroom1_length

    bedroom2_length=int(request.form['bedroom2_length'])
    bedroom2_width=int(request.form['bedroom2_width'])
    bedroom2_results=bedroom2_width*bedroom2_length

    bedroom3_length=int(request.form['bedroom3_length'])
    bedroom3_width=int(request.form['bedroom3_width'])
    bedroom3_results=bedroom3_width*bedroom3_length

    bedroom4_length=int(request.form['bedroom4_length'])
    bedroom4_width=int(request.form['bedroom4_width'])
    bedroom4_results=bedroom4_width*bedroom4_length

    bedroom5_length=int(request.form['bedroom5_length'])
    bedroom5_width=int(request.form['bedroom5_width'])
    bedroom5_results=bedroom5_width*bedroom5_length

    bedroom6_length=int(request.form['bedroom6_length'])
    bedroom6_width=int(request.form['bedroom6_width'])
    bedroom6_results=bedroom6_width*bedroom6_length

    bedroom7_length=int(request.form['bedroom7_length'])
    bedroom7_width=int(request.form['bedroom7_width'])
    bedroom7_results=bedroom7_width*bedroom7_length

    bedroom8_length=int(request.form['bedroom8_length'])
    bedroom8_width=int(request.form['bedroom8_width'])
    bedroom8_results=bedroom8_width*bedroom8_length

    bedroom9_length=int(request.form['bedroom9_length'])
    bedroom9_width=int(request.form['bedroom9_width'])
    bedroom9_results=bedroom9_width*bedroom9_length

    bedroom10_length=int(request.form['bedroom10_length'])
    bedroom10_width=int(request.form['bedroom10_width'])
    bedroom10_results=bedroom10_width*bedroom10_length

    bedroom = bedroom1_results+bedroom2_results+bedroom3_results+bedroom4_results+bedroom5_results+bedroom6_results+bedroom7_results+bedroom8_results+bedroom9_results+bedroom10_results
# bedrooms accordian
# living areas accordian
    living_areas1_length= int(request.form['living_areas1_length'])
    living_areas1_width = int(request.form['living_areas1_width'])
    living_areas1_results= living_areas1_width*living_areas1_length

    living_areas2_length= int(request.form['living_areas2_length'])
    living_areas2_width = int(request.form['living_areas2_width'])
    living_areas2_results= living_areas2_width*living_areas2_length

    living_areas3_length= int(request.form['living_areas3_length'])
    living_areas3_width = int(request.form['living_areas3_width'])
    living_areas3_results= living_areas3_width*living_areas3_length

    living_areas4_length= int(request.form['living_areas4_length'])
    living_areas4_width = int(request.form['living_areas4_width'])
    living_areas4_results= living_areas4_width*living_areas4_length

    living_areas5_length= int(request.form['living_areas5_length'])
    living_areas5_width = int(request.form['living_areas5_width'])
    living_areas5_results= living_areas5_width*living_areas5_length

    livingareas= living_areas1_results+living_areas2_results+living_areas3_results+living_areas4_results+living_areas5_results
# living areas accordian
#kitchen accordian 
    kitchen1_length= int(request.form['kitchen1_length'])
    kitchen1_width = int(request.form['kitchen1_width'])
    kitchen1_results= kitchen1_width*kitchen1_length

    kitchen2_length=  int(request.form['kitchen2_length'])
    kitchen2_width = int(request.form['kitchen2_width'])
    kitchen2_results= kitchen2_width*kitchen2_length

    kitchen3_length=  int(request.form['kitchen3_length'])
    kitchen3_width = int(request.form['kitchen3_width'])
    kitchen3_results= kitchen3_width*kitchen3_length

    kitchen4_length=  int(request.form['kitchen4_length'])
    kitchen4_width = int(request.form['kitchen4_width'])
    kitchen4_results= kitchen4_width*kitchen4_length

    kitchen5_length=  int(request.form['kitchen5_length'])
    kitchen5_width = int(request.form['kitchen5_width'])
    kitchen5_results= kitchen5_width*kitchen5_length

    kitchen = kitchen1_results+kitchen2_results+kitchen3_results+kitchen4_results+kitchen5_results
#kitchen accordian

# bathroom accordian 
    bathroom1_length = int(request.form['bathroom1_length'])
    bathroom1_width = int(request.form['bathroom1_width'])
    bathroom1_result = bathroom1_length*bathroom1_width

    bathroom2_length = int(request.form['bathroom2_length'])
    bathroom2_width = int(request.form['bathroom2_width'])
    bathroom2_result = bathroom2_length*bathroom2_width

    bathroom3_length = int(request.form['bathroom3_length'])
    bathroom3_width = int(request.form['bathroom3_width'])
    bathroom3_result = bathroom3_length*bathroom3_width

    bathroom4_length = int(request.form['bathroom4_length'])
    bathroom4_width = int(request.form['bathroom4_width'])
    bathroom4_result = bathroom4_length*bathroom4_width

    bathroom5_length = int(request.form['bathroom5_length'])
    bathroom5_width = int(request.form['bathroom5_width'])
    bathroom5_result = bathroom5_length*bathroom5_width

    bathroom6_length = int(request.form['bathroom6_length'])
    bathroom6_width = int(request.form['bathroom6_width'])
    bathroom6_result = bathroom6_length*bathroom6_width

    bathroom7_length = int(request.form['bathroom7_length'])
    bathroom7_width = int(request.form['bathroom7_width'])
    bathroom7_result = bathroom7_length*bathroom7_width

    bathroom8_length = int(request.form['bathroom8_length'])
    bathroom8_width = int(request.form['bathroom8_width'])
    bathroom8_result = bathroom8_length*bathroom8_width

    bathroom9_length = int(request.form['bathroom9_length'])
    bathroom9_width = int(request.form['bathroom9_width'])
    bathroom9_result = bathroom9_length*bathroom9_width

    bathroom10_length = int(request.form['bathroom10_length'])
    bathroom10_width = int(request.form['bathroom10_width'])
    bathroom10_result = bathroom10_length*bathroom10_width

    bathroom= bathroom1_result+bathroom2_result+bathroom3_result+bathroom4_result+bathroom5_result+bathroom6_result+bathroom7_result+bathroom8_result+bathroom9_result+bathroom10_result
# bathroom accordian
#dining room accordian
    dining_room1_length= int(request.form['dining_room1_length'])
    dining_room1_width = int(request.form['dining_room1_width'])
    dining_room1_results= dining_room1_width*dining_room1_length

    dining_room2_length= int(request.form['dining_room2_length'])
    dining_room2_width = int(request.form['dining_room2_width'])
    dining_room2_results= dining_room2_width*dining_room2_length

    dining_room3_length= int(request.form['dining_room3_length'])
    dining_room3_width = int(request.form['dining_room3_width'])
    dining_room3_results= dining_room3_width*dining_room3_length

    dining_room4_length= int(request.form['dining_room4_length'])
    dining_room4_width =int(request.form['dining_room4_width'])
    dining_room4_results= dining_room4_width*dining_room4_length

    dining_room5_length= int(request.form['dining_room5_length'])
    dining_room5_width = int(request.form['dining_room5_width'])
    dining_room5_results= dining_room5_width*dining_room5_length

    dinning_room = dining_room1_results+dining_room2_results+dining_room3_results+dining_room4_results+dining_room5_results
#dining room accordian

    total_square_foot = dinning_room+bathroom+kitchen+livingareas+bedroom

    
    
    data = {
        'user_id': session['user_id'],
        'company_id': session['company_id'],
        'name': request.form['name'],
        'address': request.form['address'],
        'address_city': request.form['address_city'],
        'address_state': request.form['address_state'],
        'address_zip': request.form['address_zip'],
        'total_cost': request.form['total_cost'],
        'bedrooms': bedroom,
        'livingareas': livingareas,
        'kitchen': kitchen,
        'bathrooms': bathroom,
        'dinning_room': dinning_room,
        'customer_request': request.form['customer_request'],
        'material_cost': request.form['material_cost'],
        'labor_cost': request.form['labor_cost'],
        'material_supplier': request.form['material_supplier'],
        'order_date_material': request.form['order_date_material'],
        'pick_up_material': request.form['pick_up_material'],
        'material_ordered_list': request.form['material_ordered_list'],
        'total_square_foot': total_square_foot,
        'file': request.form['file']
    }
    Job.create_job(data)
    return redirect('create_job')

@app.route('/delete_job/<int:id>')
def delete_job(id):
    check_user()
    data={
        'id': id
        }
    Job.delete_job(data)
    return redirect('/success_tech')

@app.route('/view_job/<int:id>')
def view_job(id):
    check_user()
    data={
        'id': id
        }
    job=Job.view_one_job(data)
    user= User.get_one_user({'id':session['user_id']})
    return render_template('view_job.html', user=user, job=job)

@app.route('/edit_job/<int:id>')
def edit_job(id):
    check_user()
    data={
        'id': id
        }
    job=Job.view_one_job(data)
    return render_template('edit_jobs.html', job=job)

@app.route('/update_job', methods=['post'])
def update_job():
    check_user()
    total_square_foot = int(request.form['bedrooms'])+int(request.form['livingareas'])+int(request.form['kitchen'])+int(request.form['bathrooms'])+int(request.form['dinning_room'])
    # if not Job.validate_create_job(request.form):
    #     return redirect(f"/edit_job/{request.form['job_id']}")
    data = {
        'id' : request.form['job_id'],
        'user_id': session['user_id'],
        'company_id': session['company_id'],
        'name': request.form['name'],
        'address': request.form['address'],
        'address_city': request.form['address_city'],
        'address_state': request.form['address_state'],
        'address_zip': request.form['address_zip'],
        'total_cost': request.form['total_cost'],
        'bedrooms': request.form['bedrooms'],
        'livingareas': request.form['livingareas'],
        'kitchen': request.form['kitchen'],
        'bathrooms': request.form['bathrooms'],
        'dinning_room': request.form['dinning_room'],
        'customer_request': request.form['customer_request'],
        'material_cost': request.form['material_cost'],
        'labor_cost': request.form['labor_cost'],
        'material_supplier': request.form['material_supplier'],
        'order_date_material': request.form['order_date_material'],
        'pick_up_material': request.form['pick_up_material'],
        'material_ordered_list': request.form['material_ordered_list'],
        'total_square_foot': total_square_foot,
        'file': request.form['file']
    }
    print (data)
    Job.update_job(data)
    return redirect('/success_tech')