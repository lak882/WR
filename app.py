from flask import Flask, render_template
import os
import csv

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"]

# get path to runs file
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(THIS_FOLDER, 'runs.csv')

# make runs into big list
with open(path, 'r') as file:
    file = csv.DictReader(file)
    RUNS = [ run for run in file ]
    # turn miles to floats
    for run in RUNS:
        run['miles'] = float(run['miles'])
    # sort by miles
    RUNS = sorted(RUNS, key=lambda run: run['miles'])

@app.route("/", methods=["GET"])
def index():
    """Let user search different runs"""
    return render_template("index.html", runs=RUNS)
