from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
import pyrebase



Config = {
  'apiKey': "AIzaSyB-8eDx782PDnYe5Ov1FTC-VzqIhplVehI",
  'authDomain': "auth-lab-2be2b.firebaseapp.com",
  'projectId': "auth-lab-2be2b",
  'storageBucket': "auth-lab-2be2b.appspot.com",
  'messagingSenderId': "1089979688553",
  'appId': "1:1089979688553:web:a359b771e15614f5efe4f8",
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
    user = { "em": email,"fullname" :fulln,"username":usern} 
    
    try:
      session['user'] = auth.create_user_with_email_and_password(email, passw)
      uid =session['user']['localId']

      db.child("Users").child(uid).set(user)

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
      uid =session['user']['localId']

      db.child('booked').child(uid).push(date)

      return redirect(url_for('final'))

    except:
      print("error try again")
      return render_template('booking.html')

  
  #return render_template("booking.html") 





@app.route('/final')
def final():
  return render_template("final.html") 




if __name__ == '__main__':
 
    app.run( debug=True)