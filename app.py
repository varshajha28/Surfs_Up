import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
import json
import app
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#Set up the Database
## Access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")
# Access & query SQLite database file
Base = automap_base()
# Reflect tables
Base.prepare(engine, reflect=True)
# Save references by creating tables
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create session link from Python to our database
session = Session(engine)
# Set up Flask
app = Flask(__name__)
# Route -Welcome main page
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
# Route2 - Percipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
# Route3 - Stations
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations)
# Route4 - Monthly temperature
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return json.dumps(temps)
# Route5 - Statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    
    results = session.query(*sel).filter(Measurement.date >=start).filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
