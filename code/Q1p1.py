
# coding: utf-8

# ## Q1 PART 1:
# • Use ‘vehicle_collisions’ data set.
# • For each month in 2016, find out the percentage of collisions in
# Manhattan out of that year's total accidents in New York City.
# • Display a few rows of the output use df.head().
# • Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# In[3]:


import os
from pathlib import Path
from pandas import Series, DataFrame
import pandas as pd

##get the data path
p = Path(os.getcwd())
csv_path=str(p.parent)+'/Data/vehicle_collisions.csv'
print(csv_path)



# In[4]:

##read the csv file
##print( pd.read_csv(csv_path))
data=pd.read_csv(csv_path)
##print(data)
frame=DataFrame(data)
frame


# In[5]:

##conver date format to datetime
frame['DATE'] = pd.to_datetime(frame['DATE'])
frame


# In[6]:

##function that will return the number of accident in manhattan and nyt area in the 2016 
def getrows(startdate,enddate):
    mask = (frame['DATE'] >= startdate) & (frame['DATE'] <= enddate)

    frame_jau=frame.loc[mask]
    ##print(len(frame_jau.index))
    
##get manhattan 
    ##print(len(frame_jau.loc[frame_jau['BOROUGH'] == 'MANHATTAN'].index))
    return len(frame_jau.index),len(frame_jau.loc[frame_jau['BOROUGH'] == 'MANHATTAN'].index)


# In[7]:

JAU=getrows('2016-1-1','2016-1-31')


# In[8]:

FEB=getrows('2016-2-1','2016-2-29')
FEB


# In[9]:

MAR=getrows('2016-3-1','2016-3-31')


# In[10]:

APR=getrows('2016-4-1','2016-4-30')


# In[11]:

MAY=getrows('2016-5-1','2016-5-31')


# In[12]:

JUN=getrows('2016-6-1','2016-6-30')


# In[13]:

JUL=getrows('2016-7-1','2016-7-31')


# In[14]:


AUG=getrows('2016-8-1','2016-8-31')



# In[15]:

SEP=getrows('2016-9-1','2016-9-30')


# In[16]:

OCT=getrows('2016-10-1','2016-10-31')


# In[17]:

NOV=getrows('2016-11-1','2016-11-30')


# In[18]:

DEC=getrows('2016-12-1','2016-12-31')


# In[22]:

##build frame
finaldata={'MONTH':['JAU','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'],'NYC':[JAU[0],FEB[0],
                    MAR[0],APR[0],MAY[0],JUN[0],JUL[0],AUG[0],SEP[0],OCT[0],NOV[0],DEC[0]],'Manhattan':[JAU[1],FEB[1],
                    MAR[1],APR[1],MAY[1],JUN[1],JUL[1],AUG[1],SEP[1],OCT[1],NOV[1],DEC[1]],'Percentage':[JAU[1]/JAU[0],FEB[1]/FEB[0],
                    MAR[1]/MAR[0],APR[1]/APR[0],MAY[1]/MAY[0],JUN[1]/JUN[0],JUL[1]/JUL[0],AUG[1]/AUG[0],SEP[1]/SEP[0],OCT[1]/OCT[0],NOV[1]/NOV[0],DEC[1]/DEC[0]]}

##finalFrame=DataFrame(finaldata)
finalFrame=DataFrame(finaldata, columns=['MONTH', 'Manhattan', 'NYC','Percentage'])
##finalFrame
##DataFrame.head(10)
finalFrame.head(5)





# In[23]:

## generrate csv file

finalFrame.to_csv('q1p1.csv',sep='\t')


# In[ ]:



