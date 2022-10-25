from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
     return render_template("sideBubbleAnimation.html")

@app.route("/sp")
def sp():
     return render_template("sponsor_pm.html")



app.run(debug=True)