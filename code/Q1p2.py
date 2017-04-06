
# coding: utf-8

# ## Question 1 part2
# • Use ‘vehicle_collisions’ data set.
# • For each borough, find out distribution of each collision scale. (One car
# involved? Two? Three? or more?) (From 2015 to present)
# • Display a few rows of the output use df.head().
# • Generate a csv output with five columns ('borough', 'one-vehicle', 'two- vehicles', 'three-vehicles', 'more-vehicles')

# In[1]:

import os
from pathlib import Path
from pandas import Series, DataFrame
import pandas as pd

##get the data path
p = Path(os.getcwd())
csv_path=str(p.parent)+'/Data/vehicle_collisions.csv'
print(csv_path)


# In[2]:

##read the csv file
##print( pd.read_csv(csv_path))
data=pd.read_csv(csv_path)
##print(data)
frame=DataFrame(data)
frame


# In[3]:

##conver date format to datetime
frame['DATE'] = pd.to_datetime(frame['DATE'])
frame.head(10)


# In[74]:

#fiflter after 2015
mask = (frame['DATE'] >= '2015-1-1')
frame=frame.loc[mask]
print(len(frame))
frame.head(10)


# In[5]:

borough_frame = frame.groupby(['BOROUGH']).size().reset_index().rename(columns={0:'count'})
print(len(frame['BOROUGH']))
borough_frame


# In[33]:

## Vehicle 1 type nan count
import math
print(len(frame['VEHICLE 1 TYPE']))

print(frame['VEHICLE 1 TYPE'].isnull().sum())




one_vehicle=len(frame['VEHICLE 1 TYPE'])-frame['VEHICLE 1 TYPE'].isnull().sum()
one_vehicle


# In[34]:

## vehicle 2 type nan count
print(len(frame['VEHICLE 2 TYPE']))

print(frame['VEHICLE 2 TYPE'].isnull().sum())
two_vehicle=len(frame['VEHICLE 2 TYPE'])-frame['VEHICLE 2 TYPE'].isnull().sum()
two_vehicle


# In[14]:

## vehicle 3 type nan count
print(len(frame['VEHICLE 3 TYPE']))

print(frame['VEHICLE 3 TYPE'].isnull().sum())
three_vehicle=len(frame['VEHICLE 3 TYPE'])-frame['VEHICLE 3 TYPE'].isnull().sum()
three_vehicle


# In[15]:

## vehicle 4 type nan count
print(len(frame['VEHICLE 4 TYPE']))

print(frame['VEHICLE 4 TYPE'].isnull().sum())
four_vehicle=len(frame['VEHICLE 4 TYPE'])-frame['VEHICLE 4 TYPE'].isnull().sum()
four_vehicle


# In[16]:

## vehicle 5 type nan count
print(len(frame['VEHICLE 5 TYPE']))

print(frame['VEHICLE 5 TYPE'].isnull().sum())
five_vehicle=len(frame['VEHICLE 5 TYPE'])-frame['VEHICLE 5 TYPE'].isnull().sum()
five_vehicle


# In[79]:

##mask=(frame['BOROUGH']=='QUEENS' &frame['VEHICLE 1 TYPE'].notnull()==True) 
##frame1=frame.loc[mask]
##print(len(frame1.index))
frame_new=frame[['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
frame_new.head(5)

##frame_new.dropna(thresh=6)

##frame1=frame[frame['VEHICLE 1 TYPE','VEHICLE 2 TYPE''VEHICLE 3 TYPE''VEHICLE 4 TYPE''VEHICLE 5 TYPE'].isnull()]
##frame1.head(10)
##mask=(frame1['BOROUGH']=='QUEENS') 
#frame2=frame1.loc[mask]
#print(len(frame2.index))


# In[98]:

##function get number of vehicle involved in different areas
def getVehicle(location,vn):
    ##frame_new.dropna(thresh=vehicle_num)
    mask=(frame_new['BOROUGH']==location)
    frame2=frame_new.loc[mask]
    return len(frame2.dropna(thresh=vn).index)


# In[105]:

print(getVehicle('QUEENS',2),getVehicle('QUEENS',3),getVehicle('QUEENS',4),getVehicle('QUEENS',5),getVehicle('QUEENS',6))

##frame2.dropna(thresh=4)


# In[107]:

##get final data
finaldata={'BOROUGH':['BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND'],'ONE-VEHICLE-ENVOLOV':[getVehicle('BROOKLYN',2)-getVehicle('BROOKLYN',3)    
                                                                                             ,getVehicle('MANHATTAN',2)-getVehicle('MANHATTAN',3)
                                                                                             ,getVehicle('QUEENS',2)-getVehicle('QUEENS',3)
                                                                                             ,getVehicle('STATEN ISLAND',2)-getVehicle('STATEN ISLAND',3)] 
          ,'TWO-VEHICLE-ENVOLOV':[getVehicle('BROOKLYN',3)-getVehicle('BROOKLYN',4)    
                                                                                             ,getVehicle('MANHATTAN',3)-getVehicle('MANHATTAN',4)
                                                                                             ,getVehicle('QUEENS',3)-getVehicle('QUEENS',4)
                                                                                             ,getVehicle('STATEN ISLAND',3)-getVehicle('STATEN ISLAND',4)]
           ,'THREE-VEHICLE-ENVOLOV':[getVehicle('BROOKLYN',4)-getVehicle('BROOKLYN',5)    
                                                                                             ,getVehicle('MANHATTAN',4)-getVehicle('MANHATTAN',5)
                                                                                             ,getVehicle('QUEENS',4)-getVehicle('QUEENS',5)
                                                                                             ,getVehicle('STATEN ISLAND',4)-getVehicle('STATEN ISLAND',5)]}

finalFrame=DataFrame(finaldata, columns=['BOROUGH', 'ONE-VEHICLE-ENVOLOV', 'TWO-VEHICLE-ENVOLOV','THREE-VEHICLE-ENVOLOV'])
finalFrame


# In[108]:

## generrate csv file

finalFrame.to_csv('q1p2.csv',sep='\t')


# In[ ]:



