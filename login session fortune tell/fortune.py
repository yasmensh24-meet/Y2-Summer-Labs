from flask import Flask, render_template,url_for,redirect,request

from flask import session as login_session

app=Flask(__name__)

app.config['SECRET_KEY'] = "Your_secret_string"

@app.route("/", methods=["GET","POST"])
def far():
	if request.method=="GET":
		return render_template("login.html")
	else:
		login_session["name"]=request.form["name"]
		login_session["birthm"]=request.form["birthm"]
		return redirect(url_for("home"))


@app.route("/home",methods=["GET","POST"])
def home():
		return render_template("home.html")
		




@app.route("/fortune")
def fortune():
	fate=["you are passing cs","you are not passing cs","your stand is winning today","you are not winning today","stay hungry","eat iasa food","not sleep bc of cs","just be happy","life is good","heyyyy you are lucky"]
	index = len(login_session["birthm"])
	if index < 10:
		finalFate=fate[index]
		return render_template("fortune.html",fortune=finalFate)
	else:
		finalFate=fate[9]
		return render_template("fortune.html",fortune=finalFate)




if __name__ == '__main__':
    app.run(debug=True)
