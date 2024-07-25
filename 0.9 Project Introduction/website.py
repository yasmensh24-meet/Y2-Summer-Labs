from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
import pyrebase



Config = {
  "apiKey": "AIzaSyB1k-tV3uvtTnqGF1lGDdyX1Jn8o8RBHcU",
  "authDomain": "my-website-eb2f8.firebaseapp.com",
  "databaseURL": "https://my-website-eb2f8-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "my-website-eb2f8",
  "storageBucket": "my-website-eb2f8.appspot.com",
  "messagingSenderId": "1084054906475",
  "appId": "1:1084054906475:web:5a54c208318d4097c2332e",
  "databaseURL": "https://my-website-eb2f8-default-rtdb.europe-west1.firebasedatabase.app/"
}



firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'




@app.route('/',methods=["GET","POST"])
def main():
  if request.method == "POST":
    email= request.form ["email"]
    passw = request.form["password"]
    fulln= request.form["fullname"]
    usern= request.form["username"]
    user = { "em": email,"fullname" :fulln,"username":usern,"password":passw} 
    if email == ""  and passw == "":
      return render_template('error.html')

    
    try:
      session['user'] = auth.create_user_with_email_and_password(email, passw)
      uid =session['user']['localId']

      db.child("Users").child(uid).set(user)
      acc= db.child("Users").child(uid).get().val()
      email = acc['em']
      session['em'] = email

      return redirect(url_for('home'))
    except:

      print("error try again")
    session.modified=True
    return redirect(url_for('home'))
      
  else:
    return render_template("signup.html")





@app.route('/home', methods=["GET","POST"])
def home():
  if request.method=="GET":
    return render_template("home2.html")
  else:
    return redirect(url_for('booking'))
  
  



@app.route('/signin', methods=["GET","POST"])
def signin():
  if request.method == "POST":
    email= request.form ["email"]
    passw = request.form["password"]


    

    try:
      session['user'] = auth.sign_in_with_email_and_password(email, passw)
      if email == "yasmen@gmail.com":
        return redirect(url_for("admin"))

      return render_template("home2.html")
    except:

      print("error try again")
      session.modified=True
      return redirect(url_for('home'))
      
  else:
    return render_template("signin.html")

  
@app.route('/signout')
def signout():
    # session.pop('user')
    session['user']=None
    auth.current_user = None
    print("signed out user")
    return redirect(url_for('main'))


@app.route('/booking',  methods=["GET","POST"])
def booking():
  if request.method=="GET":
    return render_template('booking.html')


  else:
    date = request.form["daydate"]
    try:
      session['dates']=[]
      session['dates'].append(date)
      session.modified = True

      uid =session['user']['localId']
      print('uid')
      ref = db.child("Users").child(uid).get().val()
      print('reference')
      

      namee = ref['fullname']

      session['fullname'] = namee
      saved = {"date":date}
      db.child('booked').child(uid).set(saved)
      print('booking')
      session['date_apt'] = date

      return redirect(url_for('final'))

    except:
      print("error try again")
      return render_template('booking.html')

  
  #return render_template("booking.html") 


@app.route('/admin')
def admin():
  ref =db.child('Users').get().val()
  return render_template("admin.html", users = ref.items())


@app.route('/final')
def final():
  return render_template("final.html") 




if __name__ == '__main__':
 
    app.run( debug=True)