from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

from flask import render_template, request, redirect, session,flash

from flask_app.models.company_model import Company
from flask_app.models.job_model import Job
from flask_app.models.user_model import User

def check_company():
    if 'company_id' not in session:
        return redirect('/')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_success', methods=['post'])
def login_success():
    if not Company.get_by_email_company (request.form):
        flash("You must enter a valid companyname and password")
        return redirect('/')
    data = {'email' : request.form["email"] }
    company_in_db = Company.get_by_email_company(data)
    # print(company_in_db.password[0])
    # company is not registered in the db
    if not company_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(company_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the company_id into session
    session['company_id'] = company_in_db.id
    # print(session)
    return redirect('/success')

@app.route('/register_company')
def register():
    return render_template('registration_company.html')

@app.route('/process_register_company', methods=['post'])
def register_company():
    if not Company.validate_registration_company(request.form):
        return redirect('/register_company')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # print(pw_hash)
    data={
        'password': pw_hash,
        'name': request.form['name'],
        'email': request.form['email']
        
    }
    company_id=Company.register_company(data)
    # print(company_id)
    session['company_id']=company_id
    return redirect('/success')

@app.route('/success/')
def success():
    check_company()
    print(session['company_id'])
    company= Company.get_one_company({'id':session['company_id']})
    jobs=Job.get_all_jobs()
    return render_template('dashboard_admin.html',company= company, jobs=jobs)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')