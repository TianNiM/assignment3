
# coding: utf-8

# ## Question2 part1
# - Use 'employee_compensation' data set.
# - Find out the highest paid departments in each organization group by
#   calculating mean of total compensation for every department.
# - Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# - Display a few rows of the output use df.head().
# - Generate a csv output.

# In[1]:

import os
from pathlib import Path
from pandas import Series, DataFrame
import pandas as pd

##get the data path
p = Path(os.getcwd())
csv_path=str(p.parent)+'/Data/employee_compensation.csv'
print(csv_path)


# In[2]:

data=pd.read_csv(csv_path)
##print(data)
frame=DataFrame(data)
frame.head(10)


# In[14]:

##select the columns
frame_new=frame[['Organization Group','Department','Total Compensation']]
frame_new.head(10)


# In[8]:

##combine compensation and get mean and sort


# In[28]:

final_frame=frame_new.groupby(['Organization Group','Department'])['Total Compensation'].mean()
##final_frame.sort_values(by='Total Compensation', ascending=0)
DataFrame(final_frame)
DataFrame(final_frame).sort_values(by='Total Compensation', ascending=0).head(10)


# In[20]:

##genertate csv
DataFrame(final_frame).to_csv('q2p1.csv',sep='\t')


# In[ ]:



