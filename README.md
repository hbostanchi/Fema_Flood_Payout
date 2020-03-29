![1](https://github.com/hbostanchi/Fima_Flod_Payout/blob/master/pic/Screen%20Shot%202020-03-03%20at%202.44.54%20PM.png)

# FEMA Flood Payout Prediction

## Project Overview
The prediction model proposed helps the user determine the potential Fema payout for their property incase of a flooding.

### Reason why topic selected

The model also explores climate change . It will help the user get a better understanding of insurance costs and their implications on their property. The model will focus on a US wide coverage as different regions of the country as affected by different types of flooding. For instance the West coast is more prone to flooding through rising sea levels, while Central can face damages due to flash flooding. East cost is also more susceptible to hurricanes.

The data is collected from the Fema website. The data set will cover payouts dated as far back as 19xx.

### Question the team hope to answer

Using this model, we hope to be able to predict the Fema payout for a user's property provided their zip code, flood zone and year their property was constructed in.
- Precipitation values affected payouts [merged NASA data with FEMA]
- Predict if user is eligible for a payout
- Predict payout range based on property age, location and flood zone



## Technology 
-	Software: Jupyter Notebook, SQLAlchemy , Visual Studio Code ,Flask
-	Languages: Python , Javascript, SQL
-	Dependencies: Pandas, Matplotlib, Scipy, Seaborn
-	Machine Learning Libraries: scikit-learn ,TensorFlow.
-	Data Sources:  the data has been stored in amazon RDS from postgres and s3 bucket (https://s3.console.aws.amazon.com/s3/buckets/fimaproject/?region=us-east-2&tab=overview)

## Summery
-	Description of the data exploration
 	-  Data Selection
 	-  Data processing
 	-  Data transformation
-	Machine Learnign model
-	Database Integeration
-	Deploy a Flask app from amazon RDS or postgress

## Visualization:
-Seasonal payout to see if there was a relationship between payouts and certain months
![Seasonal payout](https://github.com/hbostanchi/Fema_Flood_Payout/blob/master/pic/Screen%20Shot%202020-03-06%20at%203.59.13%20PM.png)
![montly payout](https://github.com/hbostanchi/Fema_Flood_Payout/blob/master/pic/Screen%20Shot%202020-03-06%20at%203.59.20%20PM.png)
-USA map that shows areas that did receive a payout (size of the payout dot would be the magnitude relative to all the other dots)
![dot map](https://github.com/hbostanchi/Fema_Flood_Payout/blob/master/pic/Screen%20Shot%202020-03-06%20at%204.35.03%20PM.png)



# Machine Learning Model

### Data Pre-processing
The original data was cleaned up to align useful columns. Refining data types and eleminating null values from the data.

### Feature selection and process of elimination
The features were selected by process of elimination using the coorelation matrix and the effect each feature had on the accuracy score of the linear model. The final result was the following 5 features:
  - Flood zone (encoded with dummy variables)
  - Occupancytype  (encoded with dummy variables)
	- State (encoded with dummies)
	- Loss month (extracted month from the dateofloss column (encoded with dummy variables)
  - Propertyage (lossyear - builtyear)

### Train vs Test sets
Using the linear regression model, we used the standard 70/30 split - where 70% of the data was used as train set and 30% of the data was used as test.

### Choice of model and Pros/Cons
Since we are predicting the estimated FEMA payouts for property damages, a linear regression model was chosen to best predict paterns and find the line of best fit. The linear regression model helps ----- however it tends to over simplify the problem.
Additionally logistical regression was used to predict the likelyhood of getting a payout not.

## Nural Network Model
we also work with Nueral Network Model in [Jupyter Notebook](https://github.com/hbostanchi/Fema_Flood_Payout/blob/master/model_tests/Nueral%20Network%20model.ipynb) 
- Used Sklearn and Keras
- binary classification model
- one hidden layers was used as the second one increased the loss
- kernel_initializer:Normal
- Activation functions: Relu
- loss:calculated by mean squared error
- Optimizer: adam
- Output layer was left with default settings

as a result the loss amount was hight and it would not be a good model to be used but as room for improvment it is possible to use time delay Nueral Network as the model is time series and might give us better rusult.


# Github Branches 
The Fema repository contains:
-	[Master branch](https://github.com/hbostanchi/Fema_Flood_Payout/tree/master)

 Active branches:
- Authored by Wish: [ Machine Learning Model](https://github.com/hbostanchi/Fema_Flood_Payout/tree/Wish)
- Authored by Hamed: [Joined Data](https://github.com/hbostanchi/Fema_Flood_Payout/tree/Hamed)
- Authored by Halleh:[Visualization and Dashboard](https://github.com/hbostanchi/Fema_Flood_Payout/tree/Halleh)


----------------------------------------------------------------------------------------------------------------------------------------
# Data:
the data has been stored in [amazon s3 bucket](https://s3.console.aws.amazon.com/s3/buckets/fimaproject/?region=us-east-2&tab=overview)

# Database Integration
-	Store the static data for project on amazon bucket and postgres
-	Include tables for data
-	We include connection string using SQLALchemy

  we used the SQLALchemy connection for the local conection to postgres and build on the connection to Amazon RDS and the data has transfred by a for loop and 1000 by 1000 that the make it easier to transfer.there is the tables joined on [postgres](https://github.com/hbostanchi/Fema_Flood_Payout/blob/master/data_processing/Quaries/merge_clean.sql)

----------------------------------------------------------------------------------------------------------------------------------------
# Dashboard:
The user will input 6 values in order to get an evaluation of their potential payout using Flask:
  
  - Flood zone for their propety
  - Occupancy Type
  - State
  - Loss Month (yyyy-mm-dd)
  - Year their property was built in (yyyy-mm-dd)
  
  ## Payout Density Map: 
  is a Circle map that shows the amount payout divided by $20000 and it has a popup for each payment.
  ![payoutmap](https://github.com/hbostanchi/Fema_Flood_Payout/blob/master/pic/Screen%20Shot%202020-03-25%20at%206.02.02%20PM.png)
  ## Heat map: 
  used the parcipitation and there is a drop down botton for user to choose seaing it or not.
  the mapping code could be found under the app.js file and index1.html.
  ![heatmap](https://github.com/hbostanchi/Fema_Flood_Payout/blob/master/pic/Screen%20Shot%202020-03-24%20at%207.30.18%20PM.png)
  
  

![Fema_Graphics_Rev1](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Wish/Fema_Graphics_Rev1.PNG)

The current dashboard is running localy as the image and will run on Flask later.

![Fema_dashboard](https://github.com/hbostanchi/Fema_Flood_Payout/blob/master/pic/Screen%20Shot%202020-03-29%20at%202.16.39%20PM.png)

## Presentation
[Google Slides](https://docs.google.com/presentation/d/1fE7-nOoyuoM_UTe4v-I7Vsrvtd1XgjYGy3O17S0AxRw/edit#slide=id.p)
