import numpy as np

import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#import simplejson

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the climate APIs please select your option below<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitations<br/>"
        f"     to get the last 12 months of the data set please use recent <br/>"
        f"/api/v1.0/precipitations/recent<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"  please use format YYYY-MM-DD"
        f"/api/v1.0/start_date/end_date<br/>"

    )

@app.route("/api/v1.0/precipitations")
def precipitations():
    """Return a list of all precipitations"""
    
    # Query all countries
    results = session.query(Measurement.date, Measurement.prcp).all()
    # Convert list of tuples into normal list
    session.close()
    precipitations_list=[]
    for date, prcp in results:
        precipitations_dict = {}
        precipitations_dict["date"] = date
        precipitations_dict["prcp"] = prcp
        precipitations_list.append(precipitations_dict)

    return jsonify(precipitations_list)

@app.route("/api/v1.0/precipitations/recent")
def recent_precipitations():
    """Return a list of precipitation of the last 12 months"""
    # Query all countries
    

    last_12months = dt.date(2017,8,23) - dt.timedelta(days=365)

    # Query all countries
    results_recent = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_12months).order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    precipitations_recent_list=[]
    for date, prcp in results_recent:
        precipitations_recent_dict = {}
        precipitations_recent_dict["date"] = date
        precipitations_recent_dict["prcp"] = prcp
        precipitations_recent_list.append(precipitations_recent_dict)

    return jsonify(precipitations_recent_list)

@app.route("/api/v1.0/stations")
def stations_api():
    
    results_stations = session.query(Station.id,
       Station.station, 
       Station.name, 
      Station.latitude,
      Station.longitude,
      Station.elevation).all()
    session.close()

    # Convert list of tuples into normal list
    stations_all = list(np.ravel(results_stations))

    return jsonify(stations_all)

@app.route("/api/v1.0/tobs")
def tobs():

    last_12months = dt.date(2017,8,23) - dt.timedelta(days=365)
    sel3 = [Measurement.id,Measurement.station,Measurement.date, 
        Measurement.prcp, Measurement.tobs]

    
    results_tobs = session.query(*sel3).\
        filter(Measurement.date >= last_12months).all()
    session.close()

    # Convert list of tuples into normal list
    tobs_all = list(np.ravel(results_tobs))

    return jsonify(tobs_all)


@app.route("/api/v1.0/<start>")
def analysis_from_start(start):

    year, month, day = start.split('-')


    start_date = dt.date(int(year), int(month), int(day))
    
    if start_date > dt.date(2017,8,23):
        session.close()
        return jsonify({"error": "Date out of range "}), 404

    else:    
        results_dates = session.query(Measurement.date,Measurement.station, func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).group_by(Measurement.date).\
            order_by(Measurement.date).all()


        dates_list=[]
        for date, station, avg, min1, max1 in results_dates:
            dates_dict={}
            dates_dict['date'] = date
            dates_dict['station'] = station
            dates_dict['TAVG'] = avg
            dates_dict['TMIN'] = min1
            dates_dict['TMAX'] = max1
            dates_list.append(dates_dict)
        session.close()

        return jsonify(dates_list) 


@app.route("/api/v1.0/<start>/<end>")
def analysis_start_to_end(start, end):

    year, month, day = start.split('-')
    year_e, month_e, day_e = end.split('-')


    start_date = dt.date(int(year), int(month), int(day))
    end_date = dt.date(int(year_e), int(month_e), int(day_e))
       
    if start_date > dt.date(2017,8,23) or end_date<dt.date(2010,1,1):
        session.close()
        return jsonify({"error": "Date out of range "}), 404

    else:    
        results_dates = session.query(Measurement.date,Measurement.station, func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).\
            filter(Measurement.date <= end_date).group_by(Measurement.date).\
            order_by(Measurement.date).all()


        dates_list=[]
        for date, station, avg, min1, max1 in results_dates:
            dates_dict={}
            dates_dict['date'] = date
            dates_dict['station'] = station
            dates_dict['TAVG'] = avg
            dates_dict['TMIN'] = min1
            dates_dict['TMAX'] = max1
            dates_list.append(dates_dict)
        session.close()

        return jsonify(dates_list) 
if __name__ == '__main__':
    app.run(debug=True)