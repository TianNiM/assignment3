
# coding: utf-8

# ## QUESTION2 P2
# - Use 'employee_compensation' data set.
# - Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# - Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# - For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# - Display the top 5 Job Families according to this percentage value using df.head().
# - Write the output (jobs and percentage value) to a csv.

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


# In[5]:

##select the columns and filter the year type
frame_new=frame[['Year Type','Employee Identifier','Job Family','Total Benefits','Total Compensation','Salaries','Overtime']]
frame_new=frame_new.loc[frame_new['Year Type']=='Calendar']
frame_new.head(10)


# In[15]:

## find Average of Total Benefits, Average of total compensation  for every employee.
average_frame=frame_new.groupby(['Employee Identifier'])['Total Compensation','Total Benefits','Salaries','Overtime'].mean()
DataFrame(average_frame).head(10)


# In[22]:

##people whose overtime salary is greater than 5% of salaries
overtime_frame=DataFrame(average_frame)

overtime_frame['rate'] = overtime_frame['Overtime']/overtime_frame['Salaries']
overtime_frame.head(10)

mask = (overtime_frame['rate'] >= 0.05) 
outcome_frame=overtime_frame.loc[mask]
outcome_frame


# In[26]:

## get the percent of total benefits
overtime_frame['percent_total_benefits'] = overtime_frame['Total Benefits']/overtime_frame['Total Compensation']
overtime_frame.head(10)


# In[29]:

##sort the percent_total_benefits
overtime_frame.sort_values(by='percent_total_benefits', ascending=0).head(10)


# In[30]:

##generate csv file
overtime_frame.to_csv('q2p2.csv',sep='\t')


# In[ ]:



