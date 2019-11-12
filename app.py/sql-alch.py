
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

engine = create_engine("sqlite:///Homework/Instructions/Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Station = Base.classes.station
Measurement=Base.classes.measurement

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"api/v1.0/precipitation<br/>"
        f"api/v1.0/station<br/>"
        f"api/v1.0/tobs<br/>"
        f"api/v1.0/start<br/>"
        f"api/v1.0/start/end<br/>")

@app.route("/api/v1.0/measurements")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query all passengers
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    # Convert list of tuples into normal list
    all_precipitation = []
    for date, prcp in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        all_precipitation.append(measurement_dict)
    return jsonify( all_precipitation)

@app.route("/api/v1.0/station")
def weather():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query all passengers
    results1 = session.query(Station.station, Station.name).all()
    session.close()
    # Convert list of tuples into normal list
    all_weather= []
    for station, name in results1:
        station_dict = {}
        station_dict["name"] = name
        station_dict["station"] = station
        all_weather.append(station_dict)
    return jsonify(all_weather)

@app.route("/api/v1.0/tobs")
def temp():
    session = Session(engine)
    results2 = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date>= '2010-01-01').filter(Measurement.date<= '2010-12-31').order_by(Measurement.date).all()
    session.close()
    all_temp=[]
    for date, tobs in results2:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["tobs"] = tobs
        all_temp.append(measurement_dict)
    return jsonify(all_temp)



if __name__ == "__main__":
    app.run(debug=True,port=5006)
