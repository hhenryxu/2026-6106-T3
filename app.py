1
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", method = [ "GET" , "POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()