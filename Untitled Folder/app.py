from flask import Flask, render_template
import random


app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@app.route("/s/<name>")
def ribhy (name):
	return render_template("hh.html", name=name)


@app.route('/milk')

def milk():
	a =["It is legal because I wish it"," Read more at: https://www.brainyquote.com/ nice ,minymoh, amin,"]
	return (random.choice(a))

if __name__ == "__main__":
    app.run()