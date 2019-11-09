
# import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite://hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

stations = Base.classes.hawaii_stations.csv
measurements=Base.classes.hawaii_measurements.csv

app = Flask(__name__)

# # @app.route("/")
# # def welcome():
# #     """List all available api routes."""
# #     return (
# #         f"Available Routes:<br/>"
# #     f"api/v1.0/precipitation"
# #     f"api/v1.0/stations"
# #     f"api/v1.0/tobs"
# #     f"api/v1.0/<start>"
# #     f"api/v1.0/<start>/<end>")

# # @app.route("/api/v1.0/measurements")
# # def precipitation():
# #     # Create our session (link) from Python to the DB
# #     session = Session(engine)
# #     # Query all passengers
# #     results = session.query(precipitation.date, precipitation.prcp).all()
# #     session.close()
# #     # Convert list of tuples into normal list
# #     all_precipitation = []
# #     for date, prcp in results:
# #         prcp_dict = {}
# #         prcp_dict["date"] = date
# #         prcp_dict["prcp"] = prcp
# #         all_precipitation.append(prcp_dict)


# #     return jsonify( all_precipitation)


if __name__ == "__main__":
    app.run(debug=True,port=5006)
