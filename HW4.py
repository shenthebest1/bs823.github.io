#!/usr/bin/env python
# coding: utf-8

# In[2]:




import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
#import matplotlib.pyplot as plt


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



chart_visual = st.selectbox(
    label="Select Charts/Plot type", options=['Line Chart', 'Bar Chart', 'Bubble Chart']
)


# In[8]:


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
                            ))
        
        
st.plotly_chart(fig, use_container_width=True)


# In[9]:


#Code for second dashboard

st.title("Percentage change of total number of Doctorate recipients from 1958 to 2017 Dashboard")
st.markdown("The dashboard will help a researcher to better understandhow the percentage change of total number of Doctorate recipients through 1958 to 2017 ")


# In[10]:


chart_visual1 = st.selectbox(
    label="Select Charts type", options=['line Chart', 'bar Chart', 'Bubble Chart']
)


# In[11]:




fig1 = go.Figure()
  
    

    
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





# In[14]:


#Load the second dataset
df2 = pd.read_excel('sed17-sr-tab005.xlsx')


# In[16]:


df2 = df2.iloc[3:]


# In[17]:


df2.columns = ['State', 'Rank', 'Doctorate recipients']


# In[ ]:


#Code for third dashboard

st.title("A US map dashboard showing the number of doctorate recipients of each state in 2017")
st.markdown("The dashboard will help a researcher to better understandhow the total number of Doctorate recipients from each state is different from each other in 2017 ")


# In[20]:


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

df2['U'] = df2['State'].map(state)
fig2 = px.choropleth(df2,
                    locations='U',
                    color='State',
                    #color_continuous_scale='spectral_r',
                    hover_name='State',
                    locationmode='USA-states',
                    scope='usa')

fig2.add_scattergeo(
    locations=df2['U'],
    locationmode='USA-states',
    text=df2['U'],
    mode='text')

fig2.update_layout(
    title={'text':'Fig 2. An USA map of Number of doctorate recipients by State',
           'xanchor':'center',
           'yanchor':'top',
           'x':0.5})

st.plotly_chart(fig2, use_container_width=True)


# In[ ]:





# In[ ]:





# In[50]:


#Load the third dataset
df3 = pd.read_excel('sed17-sr-tab004.xlsx')


# In[51]:





df3 = df3.iloc[5:]
df3.columns = ['Top20_Institution', 'Rank', 'Doctorate_recipients']
df3 = df3.head(20)


# In[52]:


#Code for third dashboard

st.title("A pie chart dashboard showing the number of doctorate recipients in the field of life sciences of top 20 Institution in 2017")
st.markdown("This dashboard will help a researcher to better understandhow the total number of Doctorate recipients in the field of life sciences of each institution from the top 20 institutions is different from each other in 2017 ")


# In[53]:






fig3 = px.pie(df3, values=df3.Doctorate_recipients, names=df3.Top20_Institution, color=df3.Top20_Institution,
              

             )


# In[54]:


fig3.update_layout(
    
title="<b>Top 20 Institutions in the life sciences field</b>")


st.plotly_chart(fig3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




