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
  "databaseURL": ""
}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'







@app.route('/',methods=["GET","POST"])
def main():
  if request.method == "POST":
    email= request.form ["email"]
    passw = request.form["password"]

    try:
      session['user'] = auth.create_user_with_email_and_password(email, passw)
      session["quotes"]=[]

      return render_template("home2.html")
    except:

      print("error try again")
    return redirect(url_for('home'))
      
  else:
    return render_template("signup.html")





@app.route('/home', methods=["GET","POST"])
def home():
  if request.method == "POST":
    quote=request.form['quote']
    session["quotes"]=quote
    return redirect(url_for('thanks'))
  else:
    return render_template("home2.html")    




@app.route('/signin', methods=["GET","POST"])
def signin():
  if request.method == "POST":
    email= request.form ["email"]
    passw = request.form["password"]

    try:
      session['user'] = auth.create_user_with_email_and_password(email, passw)
      session["quotes"]=[]

      return render_template("home2.html")
    except:

      print("error try again")
    return redirect(url_for('home'))
      
  else:
    return render_template("signin.html")

  
@app.route('/signout')
def signout():
    # session.pop('user')
    session['user']=None
    auth.current_user = None
    print("signed out user")
    return redirect(url_for('signin'))




@app.route('/display')
def display():
  return render_template("display.html") 


@app.route('/thanks')
def thanks():
  return render_template("thanks.html") 




if __name__ == '__main__':
 
    app.run( debug=True)