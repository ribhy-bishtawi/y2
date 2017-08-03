from flask import Flask, render_template, request
import dataset
db = dataset.connect ("postgres://xbiddflolwaaoz:6eed176810d5f3851cfa15092ffc204bbeaf9e6e874df9c7e392e6b004d23a28@ec2-23-21-96-159.compute-1.amazonaws.com:5432/d3o0183tk3rslh")
app = Flask(__name__)


@app.route('/login' ,methods=['POST',"get"])
def homepage():
    form = request.form
    password = form["password-l"]
    email = form["email-l"]
    loginTable = db["login-n"]
    entry = {"password": password, "email": email}
    loginTable.insert(entry)
    print list(loginTable.all())
    return render_template("index.html" , email=email ,password=password)
@app.route("/helo")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()