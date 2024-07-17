from flask import Flask, render_template,url_for,redirect,request

app=Flask(__name__)

@app.route("/home",methods=["GET","POST"])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		month=request.form["birthm"]
		return redirect(url_for("fortune",birthMonth = month))




@app.route("/fortune/<birthMonth>")
def fortune(birthMonth):
	fate=["you are passing cs","you are not passing cs","your stand is winning today","you are not winning today","stay hungry","eat iasa food","not sleep bc of cs","just be happy","life is good","heyyyy you are lucky"]
	index = len(birthMonth)
	finalFate=fate[9]
	if index < 10:
		finalFate=fate[index]
	return render_template("fortune.html",fortune=finalFate)




if __name__ == '__main__':
    app.run(debug=True)
