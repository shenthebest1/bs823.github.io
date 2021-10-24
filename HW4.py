#!/usr/bin/env python
# coding: utf-8

# In[4]:




import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
#import matplotlib.pyplot as plt


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


# In[33]:


st.sidebar.title("Visualization Selector")


# In[34]:





df1 = pd.read_excel('sed17-sr-tab001.xlsx')


# In[35]:


df1.columns = ['Year', 'Doctorate_recipients', 'percentage_change']
df1


# In[36]:


df1 = df1.iloc[3:]
#Remove the first three rows from the df1
df1


# In[37]:


st.title("Number of Doctorate recipients from 1958 to 2017 Dashboard")
#st.markdown("The dashboard will help a researcher to get to know \
#more about the given datasets and it's output")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")




# In[38]:


chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))


# In[42]:


fig = go.Figure()
  
    

    
if chart_visual == 'Line Chart':

    fig.add_trace(go.Scatter(x = df1.Year, y = df1.Doctorate_recipients,
                             mode = 'lines',
                             ))

elif chart_visual == 'Bar Chart':
    
    fig.add_trace(go.Bar(x = df1.Year, y = df1.Doctorate_recipients,
                             ))

elif chart_visual == 'Bubble Chart':
  
    fig.add_trace(go.Scatter(x=df1.Year, 
                             y=df1.Doctorate_recipients,
                             mode='markers',
                             marker_size=[40, 60, 80, 60, 40, 50],
                            ))
        
        
st.plotly_chart(fig, use_container_width=True)


# In[46]:


st.title("Percentage change of total number of Doctorate recipients from 1958 to 2017 Dashboard")
#st.markdown("The dashboard will help a researcher to get to know \
#more about the given datasets and it's output")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")


# In[49]:


chart_visual1 = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))


# In[50]:




fig1 = go.Figure()
  
    

    
if chart_visual1 == 'Line Chart':

    fig.add_trace(go.Scatter(x = df1.Year, y = df1.percentage_change,
                             mode = 'lines',
                             ))

elif chart_visual1 == 'Bar Chart':
    
    fig.add_trace(go.Bar(x = df1.Year, y = df1.percentage_change,
                             ))

elif chart_visual1 == 'Bubble Chart':
  
    fig.add_trace(go.Scatter(x=df1.Year, 
                             y=df1.percentage_change,
                             mode='markers',
                             marker_size=[40, 60, 80, 60, 40, 50],
                            ))
        
        
st.plotly_chart(fig1, use_container_width=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




