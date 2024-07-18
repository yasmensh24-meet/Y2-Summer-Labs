from flask import Flask,render_template

app = Flask(__name__) 

@app.route("/home")
def home():
	return render_template("home.html")

qadar=["you are passing cs","you are not passing cs","your stand is winning today","you are not winning today",]

@app.route("/fortune")
def fortune():
	return render_template("fortune.html",fate=qadar)





if __name__ == '__main__':
    app.run(debug=True)
