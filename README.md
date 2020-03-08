![1](https://github.com/hbostanchi/Fima_Flod_Payout/blob/master/pic/Screen%20Shot%202020-03-03%20at%202.44.54%20PM.png)

# FEMA Flood Payout
Fema Flood Payout Prediction
The prediction model proposed helps the user determine the potential Fema payout for their property incase of a flooding.

The model also explores climate change . It will help the user get a better understanding of insurance costs and their implications on their property. The model will focus on a US wide coverage as different regions of the country as affected by different types of flooding. For instance the West coast is more prone to flooding through rising sea levels, while Central can face damages due to flash flooding. East cost is also more susceptible to hurricanes.

The data is collected from the Fema website. The data set will cover payouts dated as far back as 19xx.

Using this model, we hope to be able to predict the Fema payout for a user's property provided their zip code, flood zone and year their property was constructed in.

# Payout Trends

![](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Halleh/pic/Screen%20Shot%202020-03-06%20at%203.59.13%20PM.png)

![](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Halleh/pic/Screen%20Shot%202020-03-06%20at%203.59.54%20PM.png)

![](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Halleh/pic/Screen%20Shot%202020-03-06%20at%203.59.20%20PM.png)

![](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Halleh/pic/Screen%20Shot%202020-03-06%20at%204.00.09%20PM.png)

![](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Halleh/pic/Screen%20Shot%202020-03-06%20at%204.00.37%20PM.png)

![](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Halleh/pic/Screen%20Shot%202020-03-06%20at%204.35.03%20PM.png)

![](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Halleh/pic/Screen%20Shot%202020-03-06%20at%204.28.01%20PM.png)



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

----------------------------------------------------------------------------------------------------------------------------------------
# Data:
the data has been stored in amazon s3 bucket https://s3.console.aws.amazon.com/s3/buckets/fimaproject/?region=us-east-2&tab=overview

----------------------------------------------------------------------------------------------------------------------------------------
# Dashboard:
The user will input 3 values in order to get an evaluation of their potential payout:
  - Year their property was built in (yyyy-mm-dd)
  - Zip code (5 digit numeric value)
  - Flood zone for their propety

![Fema_Graphics_Rev1](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Wish/Fema_Graphics_Rev1.PNG)

![Fema_dashboard](https://github.com/hbostanchi/Fima_Flood_Payout/blob/Halleh/pic/Screen%20Shot%202020-03-06%20at%203.55.29%20PM.png)
