#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Import the modules 

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ### Importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[13]:


data = pd.read_csv('covid19_Confirmed_dataset.csv')
data.head(20)


# #### Shape of the dataframe

# In[3]:


data.shape


# ### Delete the useless columns

# In[14]:


data.drop(['Lat','Long'],axis=1,inplace=True)


# In[15]:


data.head(10)


# ### Aggregating the rows by the country

# In[17]:


aggregated_data = data.groupby("Country/Region").sum()


# In[25]:


aggregated_data.head(10)


# In[27]:


aggregated_data.shape


# ### Visualizing data related to a country for example India
# visualization always helps for better understanding of our data.

# In[30]:


aggregated_data.loc['India'].plot()
aggregated_data.loc['Afghanistan'].plot()
aggregated_data.loc['China'].plot()
plt.legend()


# ### Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[32]:


aggregated_data.loc['India'].plot()


# ### Calculating the first derivative of the curve

# In[33]:


aggregated_data.loc['India'].diff().plot()


# ### Find maxmimum infection rate for India

# In[36]:


aggregated_data.loc['India'].diff().max()


# In[40]:


aggregated_data.loc['Spain'].diff().max()


# ### Find maximum infection rate for all of the countries. 

# In[42]:


countries = list(aggregated_data.index)
max_infection_rate = []
for country in countries:
    max_infection_rate.append(aggregated_data.loc[country].diff().max())
    
aggregated_data['Max Infection Rate'] = max_infection_rate


# In[45]:


aggregated_data.head(10)


# ### Create a new dataframe with only needed column 

# In[47]:


corona_infection_data = pd.DataFrame(aggregated_data['Max Infection Rate'])


# In[48]:


corona_infection_data


# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Importing the dataset

# In[49]:


world_happiness_report = pd.read_csv('worldwide_happiness_report.csv')


# In[50]:


world_happiness_report.head(10)


# ### Drop the useless columns 

# In[52]:


world_happiness_report.drop(['Overall rank','Score','Generosity','Perceptions of corruption'],axis=1,inplace=True)


# In[53]:


world_happiness_report.head()


# ### Changing the indices of the dataframe

# In[59]:


world_happiness_report.set_index(['Country or region'],inplace=True)


# In[60]:


world_happiness_report.head()


# ### Join two dataset we have prepared  

# #### Corona Dataset :

# In[62]:


corona_infection_data.head()


# #### world happiness report Dataset :

# In[63]:


world_happiness_report.head()


# In[66]:


main_data = world_happiness_report.join(corona_infection_data).copy()


# In[67]:


main_data.head()


# ### correlation matrix 

# In[68]:


main_data.corr()


# ### Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[69]:


main_data.head()


# ### Plotting GDP vs maximum Infection rate

# In[80]:


x = main_data['GDP per capita']
sns.scatterplot(x,np.log(y))


# In[73]:


sns.regplot(x,np.log(y))


# ### Plotting Social support vs maximum Infection rate

# In[79]:


x = main_data['Social support']
y = main_data['Max Infection Rate']
sns.scatterplot(x,np.log(y))


# In[76]:


sns.regplot(x,np.log(y))


# ### Plotting Healthy life expectancy vs maximum Infection rate

# In[78]:


x = main_data['Healthy life expectancy']
y = main_data['Max Infection Rate']
sns.scatterplot(x,np.log(y))


# In[81]:


sns.regplot(x,np.log(y))


# ### Plotting Freedom to make life choices vs maximum Infection rate

# In[83]:


x = main_data['Healthy life expectancy']
y = main_data['Max Infection Rate']
sns.scatterplot(x,np.log(y))


# In[84]:


sns.regplot(x,np.log(y))

