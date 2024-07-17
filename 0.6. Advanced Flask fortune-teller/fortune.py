from flask import Flask,render_template
import random
app = Flask(__name__) 

@app.route("/home")
def home():
	return render_template("home.html")




@app.route("/fortune")
def fortune():
	fate=["you are passing cs","you are not passing cs","your stand is winning today","you are not winning today","stay hungry","eat iasa food","not sleep bc of cs "]
	lol=random.choice(fate)
	return render_template("fortune.html",lol=lol)




if __name__ == '__main__':
    app.run(debug=True)
