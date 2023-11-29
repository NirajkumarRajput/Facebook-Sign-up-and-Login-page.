from flask import Flask,render_template,request
from models.Model import DB
db = DB()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/forget')
def forget():
    return render_template("forget.html")

@app.route('/perform_registration',methods=['post'])
def perform_registration():
   email_id = str(request.form.get('email_id'))
   password = str(request.form.get('password'))
   first_name =  str(request.form.get('first_name'))
   sur_name = str(request.form.get('sur_name'))
   gender = str(request.form.get('gender'))
   day = str(request.form.get('day'))
   month = str(request.form.get('month'))
   year = str(request.form.get('year'))
  
   response = db.insert_data(email_id,password,first_name,sur_name,gender,day,month,year)
   if response:
       return render_template("index.html",message='Sign up Successful')
   else:
       return render_template("register.html",message="Email already exists")

@app.route("/perform_login",methods=['post'])
def perform_login():
    email_id = str(request.form.get('combinedInput'))
    password = str(request.form.get('passwordInput'))
    response = db.search(email_id,password)
    if response:
        return render_template("index.html",message="Login Succesfull")
    else:
        return render_template("index.html",message="Email / password dose not exists")

    
@app.route("/perform_delete",methods=['post'])
def perform_delete():
    old_email = str(request.form.get('old_email'))
    response = db.delete_account(old_email)
    if response:
        return render_template('forget.html',message='Your account has been deleted')
    else:
        return render_template('forget.html',message='Your account dose not exists')


app.run(debug=True)


   

