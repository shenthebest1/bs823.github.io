#!/usr/bin/env python
# coding: utf-8

# In[12]:




import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[ ]:


st.write("""
# Biostatistics 823 HW4 
### by Jiajie Shen
""")


# In[21]:



#Load the first dataset and name it as df1

df1 = pd.read_excel('sed17-sr-tab001.xlsx')


# In[22]:


df1.columns = ['Year', 'Doctorate_recipients', 'percentage_change']


# In[23]:


df1 = df1.iloc[3:]
#Remove the first three rows from the df1


# In[24]:


st.title("Number of Doctorate recipients from 1958 to 2017 Dashboard")
st.markdown("The dashboard will help a researcher to get to understand the trend of number of doctorate recipients from 1958 to 2017 in The USA")


# In[7]:


"""Here is the code to set up the selection box for the first dashboard"""
chart_visual = st.selectbox(
    label="Select Charts/Plot type", options=['Line Chart', 'Bar Chart', 'Bubble Chart']
)


# In[8]:


fig = go.Figure()
  
    

"""Set the if elseif function here to check whether the users choose Line Chart, Bar Chart or Bubble Chart,
the first chunk here is for the line chart"""    
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
                            ))
        
        
st.plotly_chart(fig, use_container_width=True)


# In[9]:


"""Code for second dashboard start from here"""

st.title("Percentage change of total number of Doctorate recipients from 1958 to 2017 Dashboard")
st.markdown("The dashboard will help a researcher to better understand how the percentage change of total number of Doctorate recipients through 1958 to 2017 ")


# In[10]:


"""Here is the code to set up the selection box for the second dashboard"""
chart_visual1 = st.selectbox(
    label="Select Charts type", options=['line Chart', 'bar Chart', 'Bubble Chart']
)


# In[11]:




fig1 = go.Figure()
  
    
"""Set the if elseif function here to check whether the users choose Line Chart, Bar Chart or Bubble Chart, the first chunk
here is for the line chart""" 
    
if chart_visual1 == 'line Chart':

    fig1.add_trace(go.Scatter(x = df1.Year, y = df1.percentage_change,
                             mode = 'lines',
                             ))


elif chart_visual1 == 'bar Chart':
    
    fig1.add_trace(go.Bar(x = df1.Year, y = df1.percentage_change,
                             ))
    
    

elif chart_visual1 == 'Bubble Chart':
  
    fig1.add_trace(go.Scatter(x=df1.Year, 
                             y=df1.percentage_change,
                             mode='markers',
                            ))
        
        
st.plotly_chart(fig1, use_container_width=True)


# In[ ]:





# In[3]:


#Load the second dataset
df2 = pd.read_excel('sed17-sr-tab005.xlsx')


# In[4]:


"""Remove the first three rows of the dataframe"""
df2 = df2.iloc[3:]


# In[5]:


"""Rename the dataframe columns"""
df2.columns = ['State', 'Rank', 'Doctorate recipients']


# In[6]:


#Code for third dashboard is written below

st.title("A US map dashboard showing the number of doctorate recipients of each state in 2017")
st.markdown("The dashboard will help a researcher to better understand how the total number of Doctorate recipients from each state is different from each other in 2017 ")


# In[24]:


"""associate the abbreviation to each state"""
state = {'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'}

df2['S'] = df2['State'].map(state)


"""Use the px.choropleth function to use the US map and then insert df2 to make the US map reflect information about our
datadrame, use color to make each state has different color. """
fig2 = px.choropleth(df2,
                    locations='S',
                    locationmode='USA-states',
                    hover_name='State',
                    color='Doctorate recipients',
                    scope='usa')


"""Assign the abbreviation of each state on the map"""
fig2.add_scattergeo(
    text=df2['S'],
    locations=df2['S'],
    locationmode='USA-states',
    mode='text')


"""Assign a title for this dashboard"""
fig2.update_layout(
    
title="<b>An USA map of Number of doctorate recipients by State</b>")




st.plotly_chart(fig2, use_container_width=True)


# In[ ]:





# In[50]:


#Load the third dataset
df3 = pd.read_excel('sed17-sr-tab004.xlsx')


# In[51]:



"""This code is to remove the first 5 rows from the dataframe and change the column names for the dataframe"""

df3 = df3.iloc[5:]
df3.columns = ['Top20_Institution', 'Rank', 'Doctorate_recipients']
df3 = df3.head(20)


# In[52]:


#Code for third dashboard

st.title("A pie chart dashboard showing the number of doctorate recipients in the field of life sciences of top 20 Institution in 2017")
st.markdown("This dashboard will help a researcher to better understand how the total number of Doctorate recipients in the field of life sciences of each institution from the top 20 institutions is different from each other in 2017 ")


# In[53]:



"""This is the important code that can generate the pie chart dashboard"""


fig3 = px.pie(df3, values=df3.Doctorate_recipients, names=df3.Top20_Institution, color=df3.Top20_Institution,
              

             )


# In[54]:


"""Add the plot title here to make the dashboard clear to users"""

fig3.update_layout(
    
title="<b>Top 20 Institutions in the life sciences field</b>")


st.plotly_chart(fig3)


# In[ ]:





# In[ ]:





# In[ ]:




