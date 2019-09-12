import pandas as pd
from app_functions import fill_df, queryString, splitSearch, threeBeers
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc, inspect

from sklearn.cluster import KMeans

import os
import pickle
import joblib
import json

from flask import Flask, jsonify, render_template, session
from flask import Flask, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# Flask Setup ----------------------------
app = Flask(__name__)

app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'

# Hack to deal w/ relative references
dir_path = os.path.dirname(os.path.realpath(__file__))
abs_db_path = os.path.join(dir_path,"database", "db.sqlite")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("postgres://tehryzcjezrkao:6c98b6e74921f14d014bbb6d99b2837143ee23f0131f36aeac19c746adb6b6a3@ec2-174-129-226-232.compute-1.amazonaws.com:5432/d3jeg8foflomm7", "") or f"sqlite:///{abs_db_path}"

db = SQLAlchemy(app)

inspector = inspect(db.engine)
print("Check db table name: ")
print(inspector.get_table_names())

# Routes ----------------------------
@app.route("/",endpoint ="new")
def index():
    """Return the homepage."""
    return redirect('/find')

@app.route("/find")
def find():
    """Return the homepage."""
    return render_template("home.html")

@app.route("/beers")
def beers():
    results = pd.read_sql(f"""SELECT * FROM {inspector.get_table_names()[0]} """, con=db.engine)
    beers = results.to_json(orient='records')
    """Return the all beers for autocomplete."""
    return beers
    
@app.route("/list", methods=['GET'])
def handle_data2():
    print("MADE IT")

    """Handles inputs."""
    beers = []
    beers.append(request.args.get("beer1"))
    beers.append(request.args.get("beer2"))
    beers.append(request.args.get("beer3"))

    new_beers = []
    beer_names = []
    for beer in beers:
        if beer:
            new_beers.append(splitSearch(beer))
            beer_names.append(beer.split(' | ')[0])
        print(beer)

    print(len(new_beers))

    """Runs the model."""
    if len(new_beers) == 0:
        cluster = [0]
        beer_names = ['null', 'null', 'null']
    else:
        loaded_model = pickle.load(open('model.sav', 'rb'))
        cluster = loaded_model.predict(fill_df(new_beers))

        new_beers = threeBeers(new_beers)
        beer_names = threeBeers(beer_names)
    print(beer_names)

    print(cluster[0])
    prediction = cluster[0]
    session['prediction'] = f'{prediction}'
    
    return render_template("list.html", prediction = prediction, beer1 = beer_names[0], beer2 = beer_names[1], beer3 = beer_names[2])

@app.route("/run")
def run():
    """Runs query with cluster prediction."""
    cluster_no = session['prediction']
    print(f'Now: {int(cluster_no)}')

    results = pd.read_sql(queryString(cluster_no, inspector.get_table_names()[1]), con=db.engine)
    dict_results = results.to_json(orient='records')
    session.clear()

    """Returns the json results."""
    return dict_results

@app.route("/group")
def group():
    """Return the group page."""
    return  render_template("group.html")

@app.route("/top")
def top():
    results2 = pd.read_sql(f"""SELECT * FROM {inspector.get_table_names()[1]} """, con=db.engine)
    beers = results2.to_json(orient='records')

    """Return the top beers."""
    return beers

@app.route("/model")
def model():
    """Return the model page."""
    return render_template("model.html")

if __name__ == "__main__":
    app.run(debug=False)