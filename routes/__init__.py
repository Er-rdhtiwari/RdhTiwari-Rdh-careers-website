from flask import Flask, request, render_template
import os
app = Flask(__name__)


@app.route("/")
def helo_world():
    print(os.getcwd())
    return render_template('test/home.html')

@app.route("/about")
def about():
    print(os.getcwd())
    return render_template('test/about.html')