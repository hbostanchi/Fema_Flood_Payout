<<<<<<< HEAD
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
import calendar
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import pickle
from flask import Flask, render_template, request
# engine = create_engine("sqlite:///hawaii.sqlite")
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# Measurement = Base.classes.measurement
# Station = Base.classes.station
# session = Session(engine)
from flask import Flask
app = Flask(__name__)

model = pickle.load(open('payout_range_model.pkl', 'rb'))


@app.route("/", methods=["GET", "POST"])
def welcome():
        print("in welcome")
        if request.method == "POST":
                floodzone=request.form["floodzone"]
                occupancytype=request.form["occupancytype"]
                state=request.form["state"]
                zipcode=request.form["zipcode"]
                lossmonth=request.form["Lossmonth"]
                built=request.form["datetime"]                
                test = [[0]*79]
                #Floodzone
                floodzone = floodzone.upper()
                floodzone_index = column_map.index("floodzone_"+floodzone)
                test[0][floodzone_index] = 1
                #occupancytype
                occupancytype= int(occupancytype)
                occupancytype_index = column_map.index("occupancytype_"+str(occupancytype))
                test[0][occupancytype_index] = 1
                #state
                state_index = column_map.index("state_"+state)
                test[0][state_index] = 1
                #zipcode
                zipcode_index = 0
                test[0][zipcode_index] = zipcode                
                #Lossmonth
                lossmonth_index = column_map.index("lossmonth_"+lossmonth+".0")
                test[0][lossmonth_index] = 1                
                #built
                propertyage = int(built)
                buildyear_index = 2
                test[0][buildyear_index] = propertyage
                print(propertyage)
                prediction = model.predict(test)[0]
                print(prediction)
                # prediction= "$"+str(round(prediction, 2))
                return render_template("index.html", prediction=prediction)
        return render_template("index.html")
# Floodzone --[A, B, C, D, V, X]
# Occupancytype --[1, 2, 3, 4, 6]
# State --[2 letters]
# Reportedzipcode
# Lossmonth --[1-12]
# Propertyage --[numerical value (no decimals)]

column_map = ['reportedzipcode', 'propertyage', 'floodzone_B', 'floodzone_C',
       'floodzone_D', 'floodzone_X', 'lossmonth_1.0', 'lossmonth_2.0',
       'lossmonth_3.0', 'lossmonth_4.0', 'lossmonth_5.0', 'lossmonth_6.0',
       'lossmonth_7.0', 'lossmonth_8.0', 'lossmonth_9.0', 'lossmonth_10.0',
       'lossmonth_11.0', 'lossmonth_12.0', 'occupancytype_1',
       'occupancytype_2', 'occupancytype_3', 'occupancytype_4',
       'occupancytype_6', 'state_AK', 'state_AL', 'state_AR', 'state_AZ',
       'state_CA', 'state_CO', 'state_CT', 'state_DC', 'state_DE', 'state_FL',
       'state_GA', 'state_GU', 'state_HI', 'state_IA', 'state_ID', 'state_IL',
       'state_IN', 'state_KS', 'state_KY', 'state_LA', 'state_MA', 'state_MD',
       'state_ME', 'state_MI', 'state_MN', 'state_MO', 'state_MS', 'state_MT',
       'state_NC', 'state_ND', 'state_NE', 'state_NH', 'state_NJ', 'state_NM',
       'state_NV', 'state_NY', 'state_OH', 'state_OK', 'state_OR', 'state_PA',
       'state_PR', 'state_RI', 'state_SC', 'state_SD', 'state_TN', 'state_TX',
       'state_UT', 'state_VA', 'state_VI', 'state_VT', 'state_WA', 'state_WI',
       'state_WV', 'state_WY', 'floodzone_A', 'floodzone_V']

# @app.route("/payout/<built>/<zipcode>/<floodzone>")
# def payout(built=None,zipcode=None, floodzone=None):
#         test=[[0]*80]
#         floodzone=floodzone.upper()
#         floodzone_index=column_map.index("floodzone_"+floodzone)
#         test[0][floodzone_index]=1
#         propertyage=2020-int(built)
#         buildyear_index=2
#         test[0][buildyear_index]=propertyage
#         print(propertyage)
#         prediction= model.predict(test)[0]
#         print(prediction)
#         return str(prediction)

if __name__ == '__main__':
    app.run(debug=True)


# @app.route("/api/v1.0/precipitation")
# def precipitation():
#         prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#         precipitation = session.query(Measurement.date, Measurement.prcp).\
#         filter(Measurement.date >= prev_year).all()
#         precip = {date: prcp for date, prcp in precipitation}
#         return jsonify(precip)

# @app.route("/api/v1.0/stations")
# def stations():
#         results = session.query(Station.station).all()
#         stations = list(np.ravel(results))
#         return jsonify(stations)

# @app.route("/api/v1.0/tobs")
# def temp_monthly():
#         prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#         results = session.query(Measurement.tobs).\
#                 filter(Measurement.station == 'USC00519281').\
#                 filter(Measurement.date >= prev_year).all()
#         temps = list(np.ravel(results))
#         return jsonify(temps)

# @app.route("/api/v1.0/temp/<start>")
# @app.route("/api/v1.0/temp/<start>/<end>")
# def stats():
#         sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs),              func.max(Measurement.tobs)]
#         if not end:
#                 results = session.query(*sel).\
#                 filter(Measurement.date >= start).\
#                 filter(Measurement.date <= end).all()
#                 temps = list(np.ravel(results))
#      return jsonify(temps)
#                 results = session.query(*sel).\
#                 filter(Measurement.date >= start).\
#                 filter(Measurement.date <= end).all()
#                 temps = list(np.ravel(results))
#      return jsonify(temps)
# built index
=======
from flask import Flask, render_template
from flask_pymongo import PyMongo
import pickle 
#import scraping

# Set up Flask
app = Flask(__name__)
model=pickle.load(open("model.pkl", "rb"))

# # Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

# # Define the route for the HTML page
@app.route("/")
def index():
    #mars = mongo.db.mars.find_one()

    return render_template("index.html")#, mars=mars)



#built index
column_map= ['numberoffloorsintheinsuredbuilding', 'rolling_7days_obs',
       'propertyage', 'floodzone_B', 'floodzone_C', 'floodzone_D',
       'floodzone_X', 'occupancytype_1', 'occupancytype_2', 'occupancytype_3',
       'occupancytype_4', 'occupancytype_6', 'lossmonth_1.0', 'lossmonth_2.0',
       'lossmonth_3.0', 'lossmonth_4.0', 'lossmonth_5.0', 'lossmonth_6.0',
       'lossmonth_7.0', 'lossmonth_8.0', 'lossmonth_9.0', 'lossmonth_10.0',
       'lossmonth_11.0', 'lossmonth_12.0', 'state_AK', 'state_AL', 'state_AR',
       'state_AZ', 'state_CA', 'state_CO', 'state_CT', 'state_DC', 'state_DE',
       'state_FL', 'state_GA', 'state_GU', 'state_HI', 'state_IA', 'state_ID',
       'state_IL', 'state_IN', 'state_KS', 'state_KY', 'state_LA', 'state_MA',
       'state_MD', 'state_ME', 'state_MI', 'state_MN', 'state_MO', 'state_MS',
       'state_MT', 'state_NC', 'state_ND', 'state_NE', 'state_NH', 'state_NJ',
       'state_NM', 'state_NV', 'state_NY', 'state_OH', 'state_OK', 'state_OR',
       'state_PA', 'state_PR', 'state_RI', 'state_SC', 'state_SD', 'state_TN',
       'state_TX', 'state_UT', 'state_VA', 'state_VI', 'state_VT', 'state_WA',
       'state_WI', 'state_WV', 'state_WY', 'floodzone_A', 'floodzone_V']
@app.route("/payout/<built>/<zipcode>/<floodzone>")
def payout(built=None,floodzone= None, zipcode=None):
        test=[[0]*80]
        floodzone=floodzone.upper()
        floodzone_index = column_map.index("floodzone_"+floodzone)
        test[0][floodzone_index]=1 
        print(test)
        prediction=model.predict(test)
        print(prediction)
        return str(prediction)
    
    
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> Halleh
