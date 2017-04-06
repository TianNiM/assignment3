
# coding: utf-8

# ## q3
# - Use ‘cricket_matches’ data set.
# - Calculate the average score for each team which host the game and win the game.
# - Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# - Display a few rows of the output use df.head()
# - Generate a csv output

# In[1]:

import os
from pathlib import Path
from pandas import Series, DataFrame
import pandas as pd

##get the data path
p = Path(os.getcwd())
csv_path=str(p.parent)+'/Data/cricket_matches.csv'
print(csv_path)


# In[2]:

data=pd.read_csv(csv_path)
##print(data)
frame=DataFrame(data)
frame.head(10)


# In[27]:

##select the columns useful
frame_new=frame[['home','winner','innings1_runs','innings2_runs']]
frame_new.head(10)


# In[28]:

##get winning team
import numpy as np
frame_new=frame_new.loc[frame_new['home']==frame_new['winner']]
frame_new['score'] = np.where(frame_new['innings1_runs'] > frame_new['innings2_runs'], frame_new['innings1_runs'], frame_new['innings2_runs'])
frame_new.head(10)

final_frame=frame_new.drop(['home','innings1_runs','innings2_runs'],axis=1)
final_frame.head(10)


# In[26]:

## generate csv file
final_frame.to_csv('q3.csv',sep='\t')


# In[ ]:



