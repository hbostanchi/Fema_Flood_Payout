#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import our dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import tensorflow as tf

# Import our input dataset
FEMA_df = pd.read_csv('FIMA_NFIP_Redacted_Claims_Data_Set/openFEMA_claims20190831.csv')
FEMA_df.head()


# In[2]:


FEMA_Clean_df=FEMA_df.drop(columns=["policycount","countycode","crsdiscount","condominiumindicator","agriculturestructureindicator",
                                    "basementenclosurecrawlspacetype",'asofdate',"amountpaidoncontentsclaim","obstructiontype",
                      'basefloodelevation',"elevationcertificateindicator","elevatedbuildingindicator","censustract",
                      "houseworship","locationofcontents","lowestadjacentgrade","postfirmconstructionindicator","yearofloss",
                      "lowestfloorelevation","nonprofitindicator","originalnbdate","amountpaidonincreasedcostofcomplianceclaim",
                      "smallbusinessindicatorbuilding","primaryresidence","ratemethod","totalbuildinginsurancecoverage","totalcontentsinsurancecoverage"])
FEMA_Clean_df.head(10)


# In[3]:


FEMA_Clean_df.shape


# In[4]:


FEMA_Clean_df.dtypes


# In[115]:


#Remove all Data that don’t have an City defined.
FEMA_Clean1_df=FEMA_Clean_df[FEMA_Clean_df["reportedcity"] != "N/A"]
FEMA_Clean1_df.dropna(subset=['reportedcity'], how='all', inplace=True)
print(FEMA_Clean1_df.shape)

FEMA_Clean2_df=FEMA_Clean1_df[FEMA_Clean1_df["amountpaidonbuildingclaim"] != "N/A"]
FEMA_Clean2_df.dropna(subset=['amountpaidonbuildingclaim'], how='all', inplace=True)
print(FEMA_Clean2_df.shape)

FEMA_Clean3_df=FEMA_Clean2_df[FEMA_Clean2_df["originalconstructiondate"] != "N/A"]
FEMA_Clean3_df.dropna(subset=['originalconstructiondate'], how='all', inplace=True)
print(FEMA_Clean3_df.shape)

FEMA_Clean4_df=FEMA_Clean3_df[FEMA_Clean3_df["floodzone"] != "N/A"]
FEMA_Clean4_df.dropna(subset=['floodzone'], how='all', inplace=True)
print(FEMA_Clean4_df.shape)

FEMA_Clean5_df=FEMA_Clean4_df[FEMA_Clean4_df["occupancytype"] != "N/A"]
FEMA_Clean5_df.dropna(subset=['occupancytype'], how='all', inplace=True)
print(FEMA_Clean5_df.shape)

FEMA_Clean6_df=FEMA_Clean5_df[FEMA_Clean5_df["numberoffloorsintheinsuredbuilding"] != "N/A"]
FEMA_Clean6_df.dropna(subset=['numberoffloorsintheinsuredbuilding'], how='all', inplace=True)
print(FEMA_Clean6_df.shape)

FEMA_Clean7_df=FEMA_Clean6_df[FEMA_Clean6_df["latitude"] != "N/A"]
FEMA_Clean7_df.dropna(subset=['latitude'], how='all', inplace=True)
print(FEMA_Clean7_df.shape)

FEMA_Clean8_df=FEMA_Clean7_df[FEMA_Clean7_df["occupancytype"] != "N/A"]
FEMA_Clean8_df.dropna(subset=['longitude'], how='all', inplace=True)
print(FEMA_Clean8_df.shape)

FEMA_Clean9_df=FEMA_Clean8_df[FEMA_Clean8_df["dateofloss"] != "N/A"]
FEMA_Clean9_df.dropna(subset=['dateofloss'], how='all', inplace=True)
print(FEMA_Clean9_df.shape)

FEMA_Clean10_df=FEMA_Clean9_df[FEMA_Clean9_df["reportedzipcode"] != "N/A"]
FEMA_Clean10_df.dropna(subset=['reportedzipcode'], how='all', inplace=True)
print(FEMA_Clean10_df.shape)

FEMA_Clean11_df=FEMA_Clean10_df[FEMA_Clean10_df["reportedzipcode"] != "N/A"]
FEMA_Clean11_df.dropna(subset=['reportedzipcode'], how='all', inplace=True)
print(FEMA_Clean11_df.shape)

FEMA_Clean12_df=FEMA_Clean11_df[FEMA_Clean11_df["elevationdifference"] != "N/A"]
FEMA_Clean12_df.dropna(subset=['elevationdifference'], how='all', inplace=True)
print(FEMA_Clean12_df.shape)

FEMA_Clean13_df=FEMA_Clean12_df[FEMA_Clean12_df["state"] != "N/A"]
FEMA_Clean13_df.dropna(subset=['state'], how='all', inplace=True)
print(FEMA_Clean13_df.shape)

FEMA_Clean13_df.head(5)

# Drop rows with any empty cells
# FEMA_Clean_df=FEMA_Clean_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)


# In[130]:


# Drop rows with any empty cells, check
FEMA_Clean14_df=FEMA_Clean13_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
print(FEMA_Clean14_df.shape)
FEMA_Clean14_df


# In[131]:


FEMA_Clean14_df.dtypes


# In[132]:


#convert dateofloss type to datetime
FEMA_Clean14_df['dateofloss'] =  pd.to_datetime(FEMA_Clean14_df['dateofloss'], format='%Y-%m-%d')
FEMA_Clean14_df.dtypes


# In[133]:


#Identify which row makes error on originalconstructiondate and doesnt let to change the type to date
FEMA_Clean14_df['originalconstructiondate'] =  pd.to_datetime(FEMA_Clean14_df['originalconstructiondate'], errors='coerce')
FEMA_Clean14_df.sort_values('originalconstructiondate')


# In[134]:


#Remove the row in originalconstructiondate that causes error
FEMA_Clean14_df=FEMA_Clean14_df.drop(549916)


# In[137]:


FEMA_Clean14_df['originalconstructiondate'] =  pd.to_datetime(FEMA_Clean14_df['originalconstructiondate'], format='%Y-%m-%d', errors='ignore')
FEMA_Clean14_df.dtypes


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:


# FEMA_Clean15=FEMA_Clean14_df.originalconstructiondate.apply(type)
# FEMA_Clean15_df= pd.DataFrame(FEMA_Clean15)
# FEMA_Clean15_df["originalconstructiondate"].unique()


# In[47]:


# FEMA_Clean14_df[FEMA_Clean14_df['originalconstructiondate'].str.contains(" ")]


# In[50]:


# FEMA_Clean14_df['originalconstructiondate'].apply(len)


# In[86]:


# FEMA_Clean14_df['originalconstructiondate'].value_counts()


# In[102]:


# try:
#     print(FEMA_Clean14_df[FEMA_Clean14_df['originalconstructiondate'].str.len() > 10]['originalconstructiondate'])
# except TypeError:
#     print (TypeError)


# In[108]:


# FEMA_Clean14_df


# In[103]:


# import datetime as dt
# #from pandas.tslib import OutOfBoundsDatetime
# try:
#     FEMA_Clean14_df['originalconstructiondate'] = FEMA_Clean14_df['originalconstructiondate'].str[:10]
#     FEMA_Clean14_df['originalconstructiondate'] =  pd.to_datetime(FEMA_Clean14_df['originalconstructiondate'], format='%Y-%m-%d', errors='ignore')
# except:
#     print("Error")
#     raise


# In[ ]:




