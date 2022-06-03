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



@app.route('/login_success_tech', methods=['post'])
def login_success_user():
    if not User.get_by_email_user (request.form):
        flash("You must enter a valid username and password")
        return redirect('/')
    data = {'email' : request.form["email"] }
    user_in_db = User.get_by_email_user(data)
    # print(user_in_db.password[0])
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['company_id'] = user_in_db.company_id
    print(session)
    return redirect('/success_tech')

@app.route('/register_tech')
def register_user():
    return render_template('registration_user.html')

@app.route('/process_register_tech', methods=['post'])
def process_register_user():
    if not User.validate_registration(request.form):
        return redirect('/register_tech')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # print(pw_hash)
    data={
        'password': pw_hash,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'company_id': request.form['company_id'],
        'email': request.form['email']
        
    }
    user_id=User.register_user(data)
    # print(user_id)
    session['user_id']=user_id
    

    return redirect('/success_tech')

@app.route('/success_tech')
def success_user():
    check_user()
    company= Company.get_one_company({'id':session['company_id']})
    user= User.get_one_user({'id':session['user_id']})
    jobs=Job.get_all_jobs()
    return render_template('dashboard_tech.html',user= user, jobs=jobs, company=company)








@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')