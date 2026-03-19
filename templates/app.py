1
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", method = [ "GET" , "POST"])
def index():
    return("Hi")

if __name__ == "_main_":
    app.run()