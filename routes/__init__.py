from flask import Flask, request, render_template, jsonify
import os
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':"Data Analyst",
        'location': 'Bengaluru',
        'Salary':"10K"
    },
    {
            'id': 2,
            'title':"Python Developer",
            'location': 'Remote',
        },
    {
            'id': 3,
            'title':"DevOps Engineer",
            'location': 'Bengaluru',
            'Salary':"10K"
        },
    {
            'id': 4,
            'title':"Data Scientist",
            'location': 'Bengaluru',
            'Salary':"10K"
        },
]

@app.route("/")
def helo_world():
    print(os.getcwd())
    return render_template('test/home.html')

@app.route("/about")
def about():
    print(os.getcwd())
    return render_template('test/about.html',
                           jobs=JOBS,
                           company_name= "Pichain Innovation Labs")

@app.route("/jobs")
def jobs():
    print(os.getcwd())
    return render_template('test/job.html',
                           jobs=JOBS,
                           company_name= "Pichain Innovation Labs")

@app.route("/listjob")
def listjob():

    return jsonify(JOBS)