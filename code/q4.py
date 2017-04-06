
# coding: utf-8

# ## Question4
# - Use ‘movies_awards’ data set.
# - You are supposed to extract data from the awards column in this dataset and split it into several
# columns. An example is given below.
# - The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# - You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award.
# - If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated).
# - Create two separate columns for each award category (won and nominated).
# - Write your output to a csv file. (Sample output is given in next page)

# In[1]:

import os
from pathlib import Path
from pandas import Series, DataFrame
import pandas as pd

##get the data path
p = Path(os.getcwd())
csv_path=str(p.parent)+'/Data/movies_awards.csv'
print(csv_path)


# In[2]:

data=pd.read_csv(csv_path)
##print(data)
frame=DataFrame(data)
frame.head(10)


# In[4]:

frame_new=frame[['Title','Awards']]
frame_new.head(10)


# In[6]:

##replace nan to 0
frame_new.fillna(0).head(10)


# In[ ]:



