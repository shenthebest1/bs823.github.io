#!/usr/bin/env python
# coding: utf-8

# In[67]:




import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
#from plotly.subplots import make_subplots
import plotly.graph_objects as go
#import matplotlib.pyplot as plt


# In[51]:


#pip install plotly


# In[52]:


#pip install streamlit


# In[53]:


#df = pd.read_excel("sed17-sr-tab046.xlsx")


# In[54]:


#df


# In[55]:


#df.dropna()


# In[57]:


#df = df.rename(columns={'Unnamed: 1': 'Total', 'Unnamed: 2': 'Life sciences', 'Unnamed: 3': 'Physical sciences and earth sciences','Unnamed: 4': 'Mathematics and computer sciences',
#                        'Unnamed: 5': 'Psychology and social sciences','Unnamed: 6': 'Engineering','Unnamed: 7': 'Education','Unnamed: 8': 'Humanities and arts',
#                        'Unnamed: 9': 'others'})
#df


# In[58]:


#df = df.iloc[1: , :]
#df


# In[59]:


#df = df.iloc[1: , :]
#df


# In[60]:


#df = df.iloc[1: , :]
#df


# In[17]:


st.sidebar.title("Visualization Selector")


# In[61]:





df1 = pd.read_excel('sed17-sr-tab001.xlsx')
df1


# In[62]:


df1 = df1.rename(columns={'Unnamed: 1': 'Doctorate_recipients', 'Unnamed: 2': 'percentage_change'})
df1


# In[63]:


df1 = df1.iloc[3:]
#Remove the first three rows from the df1
df1


# In[64]:


st.title("Number of Doctorate recipients from 1958 to 2017 Dashboard")
#st.markdown("The dashboard will help a researcher to get to know \
#more about the given datasets and it's output")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")




# In[65]:


chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))


# In[66]:


fig = go.Figure()
  
    

    
if chart_visual == 'Line Chart':

    fig.add_trace(go.Scatter(x = df1.Doctorate_recipients, y = df1.percentage_change,
                             mode = 'lines',
                             ))

        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




