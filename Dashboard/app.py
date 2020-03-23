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
# @app.route("/")
# def index():
#     mars = mongo.db.mars.find_one()
#     return render_template("index.html", mars=mars)



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