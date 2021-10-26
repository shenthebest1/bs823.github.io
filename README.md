# Biostat 823
<br />
Name: Jiajie Shen
<br />

`blog information`: This blog is the property of Jiajie Shen and the blog contains the homework solution and explanation for the class of Biostatistics 823 of Fall 2021.

<br />

# HW1
# Question 1 (Euler problem 9)


### Question: There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
<br />
<br />

Solution code:
```
def special(s):

"""
The first for loop sets the shortest side's range
"""
    for a in range(1,s):
        for b in range(a+1, s-a):
        """
        The second for loop sets the second longest side's range
        """
            c = s - a - b;
            if a**2 + b**2 == c**2:
                return a*b*c
            
special(1000)

```
<br />

### Explanation for my solution: 
firstly, I created a function named `speical` and we have a random variable `s` in the parenthesis mark. We need to use two for loop to find the special value for each side of this triangle, and all sides should satisfy the conditions we have set. 

The first for loop is looking for the shortest side `a` which ranges from 1 to s, and the second for loop is looking for the second longest side `b` which ranges from a+1 to s-a, and the first for loop contains the second for loop because side a and side b are in the same triangle. 

It is obvious that `c = s - a - b ` and we set the Pythagorean theorem function. After finding the side `a`, `b`, `c` we finally let the function return the product of abc.

<br />

# Question 2 (Euler problem 16)

### Question: What is the sum of the digits of the number 2^1000?

<br />
<br />
solution code:

```
import math


def digit(num):

    total = 0
    while num >= 1:
    """
    Go through a while loop to in order to get every digit for the random variable num
    """

        mid = num % 10
        
        """
        get each digit from num as remainders.
        """
    
        total = total + mid
        num = num//10
    return total
    
digit(2**1000)

```

### Explanation for my solution: 
firstly, I created a function named `digit` and we have a random variable `num` in the parenthesis mark. I set the variable `total` eqaul to 0 to accumulate the sum of all the digits. If the input value `num` is greater or equal to 1 then it will keep the while loop running.

Inside of the while loop, we need to get the number on each digit so I use `mid = num % 10` to get remainder and then accumlate all the remainder which is the same as get the sum of digits of random variable `num`, at the end of each round of the while loop, I divide `num` by 10 so we can get the digits one by one.


<br />

# Question 3 (Euler Problem 76) 

### Question: How many different ways can one hundred be written as a sum of at least two positive integers?

<br />

part of solution code:
```
            if j == i:
                val = 1
            elif j > i:
                val = 0
            elif j == 0:
                val = par[i][j + 1]
                """
                if j equals to 0 here, I will do the partition as par[i][j+1]
                """
            else:
                val = par[i][j + 1] + par[i - j][j]
                """
                Otherwise, I will do the partition as 
                par[i][j + 1] + par[i - j][j]
                """
            par[i][j] = val
```

### Explanation for my solution: 
firstly, I created a function named `compute` and we have a random variable `limit` in the parenthesis mark. I set up an empty list for `par` at the beginning. The first for loop is to set random variable `i` from range 0 to `limit + 1`, and the second for loop to set `j` from range 0 to reversed `limit +1` 

And the above combination of if, elif, else is to make the partition algorithm. I will just use an example to illustrate how this code works.

`Example:` We can use number 6. 
We have the following 3 methods to get the result of 6 without using all the 1s.
<br />
5+1
<br />
4+2
<br />
3+3

If we use 1 to let the algorithm expand then have the following as our algorithms for number 6. Thus, 6 has 10 addition method in total. 
<br />
5+1
<br />
  4+1+1
  <br />
    3+1+1+1
    <br />
      2+1+1+1+1
      <br />
        1+1+1+1+1+1
        <br />
    2+2+1+1
    <br />
  3+2+1
  <br />
4+2
<br />
  2+2+2
  <br />
3+3

Finally, we use the same method to get the result of 100, so we get the result is 190569291. This is a very complex loop to get the result. 

<br />
<br />
<br />

# HW 2

### Question: 
Find the first 10-digit prime in the decimal expansion of 17π.

-Write a function to generate an arbitrary large expansion of a mathematical expression like π. Hint: You can use the standard library decimal or the 3rd party library sympy to do this
<br />
-Write a function to check if a number is prime. Hint: See Sieve of Eratosthenes
<br />
-Write a function to generate sliding windows of a specified width from a long iterable (e.g. a string representation of a number)

```
import numpy
import math
import sympy as sym

def prime(a):
    """First check number a through the following conditions  """

    if a == 2: return True
    if a % 2 == 0: return False
    if a < 2: return False
    i = 2
    """Set n = a^2 +1 for the following algortithms """
    
    n = math.sqrt(a) + 1
    
    """Run through the while loop here as consition i<n and check whether the input is a prime number"""

    while(i < n):
        if a % i == 0:
            return False
        i += 1
    return True

    """This function finishs to check the input number a is prime or not"""

```

### explanation: This is the first function I created to check a number is prime or not, since we need to find a 10 digits number inside of the 17pi decimal. So this function can help us to check whether the 10 digits number is prime or not.  

<br />
<br />

```

def expa(nu, dig):
    '''this function is to generate an arbitrary large expansion of a mathematical expression the nu should be a 
    mathematical expression and dig is number of digits we want'''

    if dig <= 0:
        return ValueError("dig must be larger than 0")

    """Use evalf to expand our mathematical expression to dig+1 digits """
   
    a = nu.evalf(dig+1)

   
    b = str(a)[0:dig+1]
    return b


```

### explantion: The second function I created is for the use of expanding mathematical expression that has large number of dights. Since we are dealing with pi in this problem, then we need to expand the digits for pi. This function can expand a mathematical expression with the desired digits we want. So it is very helpful for us to use it after. 

<br />
<br />

```
def prime_pi(p,dig):

"""We run though a for loop to go through the decimal number in 17*pi   """

    for i in range(len(expa(p,dig))):

    """Since we want a 10 digits number so we set the length of the expanded math expression as 10 """

        x = int(p[i:10+i])

        """Use the prime function that we have created before to check whether the 10 digits number is prime or not"""

        if prime(x):
            return  x

            """Finally, return the first 10-digit prime in the decimal expansion of 17π"""
```

### explantion: This function is combines all the function we have created before. We use the expa function to get the decimal expansion for the 17π; and then slide all the 10 digits number from the expansion and check if it is a prime number. We have set a for loop to run through all the 10 digits number. And the for loop will stop if it finds the first 10 digits number which is a prime number. 

<br />

### Answer: The first 10-digit prime in the decimal expansion of 17π is 8649375157 from my code. 

<br />
<br />





# HW3

### Question: Create 3 informative visualizations about malaria using Python in a Jupyter notebook, starting with the data sets at the website https://github.com/rfordatascience/tidytuesday/tree/master/data/2018/2018-11-13

<br />
<br />

First, I import all the packages that I will use for my plotting later. And then I read the 3 datasets by using pd.read_csv. On the GitHub, I click the raw option for each datasets, and then copied the website so pandas can read the data. 

`malaria_deaths.csv` will be named data1 here; `malaria_deaths_age.csv` will be named data2 here and finally `malaria_inc.csv` will be data3 here for easy distinguish. 

```
import pandas as pd
import io
import requests
from toolz import pipe
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.express as px
import plotly.offline as py
import altair as alt


url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_deaths.csv"

data1 = pd.read_csv(url, error_bad_lines=False)



url2 = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_deaths_age.csv"

data2 = pd.read_csv(url2, error_bad_lines=False)


url3 = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_inc.csv"

data3 = pd.read_csv(url3, error_bad_lines=False)
```

<br />

Next, I will generate plot for each of the dataset. The following code below is to generate a `scatterplot` of the first dataset `malaria_deaths.csv` and the illustration of the graph will be given. 



```
"""I use the px.scatter to generate the scatter plot """
fig = px.scatter(data1, 
                 x="Year", 
                 y="Entity", 
                 
                 """I put x-axis as all the years amd y-axis as all different countries"""
                 
                 size="Deaths - Malaria - Sex: Both - Age: Age-standardized (Rate) (per 100,000 people)",
                 
                 """I set the size is for the death rate of malaria so we can easily tell from the plot to determine the size of death rate from Malaria for each country"""
                 
                 color = "Entity")
                """I set the color is based on the countries, so each country can get a different color which make the 
                plot more reader friednly."""
fig

"""Output fig in the following """

```


![newplot](https://user-images.githubusercontent.com/78027134/135559223-bf2e8384-bec0-4d96-b884-57c621fc6f85.png)

<br />

### explanation to the graph: From the graph above, we can illustrate from the plot for valuable information. The graph shows that the death rate of Malaria of each country from year 1990 to year 2015. The size of circles represent the death rate in the countries so there are some countries have few deaths of malaria such as Afghanistan,Albania. And there are some countries have large death rate such as Namibia, Malawi. And it is very clear to see that the highest death rate among all the countries are from 2000 - 2005. Users can also put the mouse on the circle to see the details of each circle. 

<br />
<br />

This is code to generate the plot for the second dataset which is `malaria_deaths_age.csv`

```
gra = px.scatter(data2, 
"""I use the px.scatter function to generate scatterplot for data
2 """
                 x="entity", 
                 y="deaths", 
"""Use x-axis for all the countries, and y-axis for the dealth number in each country"""

                 color="age_group",
"""I set different age groups to different colors so we can use this plot to make some comparsion between different age groups"""                 
                )
gra

"""output the graph in the following"""
```

![data2](https://user-images.githubusercontent.com/78027134/135564778-fb4a40db-3b54-4dc5-a127-8814313970b3.png)

<br />

### explanation to the graph: It is very obvious that the people who are under age 5 and age between 5 -14 have a much higher death rate of malaria among the countries. My explnation for that is younger people have a less comprehansive immune system so that they have the larger probabilty to die because of malaria. Users can put the mouse on the points to see the details on each point.   

<br />
<br />


This following code is to generate the plot for the third dataset which is `malaria_inc.csv`

```
"""Use the alt.Chart to plot the point chart for the data3"""
alt.Chart(data=data3).mark_point().encode(
    x="Entity",
    y="Incidence of malaria (per 1,000 population at risk) (per 1,000 population at risk)",
"""Use x-axis as all the countries in the dataset, use y-axis for the incidence of malaria"""

    color = "Entity"
"""Here, I put different countries in different colors so that we can easily distinguish different countries. """        
)

```

![data3](https://user-images.githubusercontent.com/78027134/135564832-f2b24416-c946-4ed5-abff-901307bbb49c.png)

<br />

### explanation to the graph: From this graph, we can see that there are some countries have very low incidence of malaria such as Thailand, Vietnam, South Korea. There are also some countries have relatively high incidence of malaria such as Ethiopia, Liberia and Turky. And we can see there is a huge outlier in Turkey. The difference of incidence of malaria between countries is based on the measures they take or the spreadness of malaria to this country. 


<br />
<br />



# HW4

### Assignment task: Download data of Science and Engineering PhDs awarded in the US. Do some analysis in pandas. Make a dashboard visualization of a few interesting aspects of the data.

<br />

I used streamlit to generate the dashboard for the visulization. And the my result can be found through the following link:
https://share.streamlit.io/shenthebest1/bs823.github.io/main/HW4.py

<br />

The very first step is always to import all the packages that we will use for this project

```
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json
from plotly.subplots import make_subplots
import plotly.graph_objects as go

```



<br />

1 The first dashboard on my streamlit website is for Number of Doctorate recipients from 1958 to 2017 Dashboard. It is an interesting dashboard that can reproduce the dataset into three different plots including: Line chart, Bar chart and Bubble chart. There is a selection box on the streamlit website for users to choose from the three different plots. Users have the chance to make choice upon which charts they like the most so the dashboard will generate the plot they want. 

This dashboard will help a researcher to get to understand the trend of number of doctorate recipients from 1958 to 2017 in The USA, from the line chart of this dashboard. Also, when users point their mouse at any point of the line, the dashboard will show that what year is the specific point and how many doctorate recipients in that year. And it is the same thing for the other two types of charts. it is very clear to see that there is an increasing trend for number of Doctorate recipients from 1958 to 2017 in the USA. Especially from 1960s to 1970s, the number of doctorate recipients has even been tripled.

Thus, this dashboard helps us a lot to make the conclusion that there is an increasing trend for number of Doctorate recipients from 1958 to 2017 in the USA. This interactive dashboard is really user-friendly which make researchers have better efficiency to gain information. 

<br />

##### Load the dataset for the first dashboard named df1
```
#Load the first dataset and name it as df1

df1 = pd.read_excel('sed17-sr-tab001.xlsx')

```


```

"""Here is the code to set up the selection box for the first dashboard"""

chart_visual = st.selectbox(
    label="Select Charts/Plot type", options=['Line Chart', 'Bar Chart', 'Bubble Chart']
)


```

##### Explanation: This is the code to generate the selection box for the first dashboard, so the users can choose from Line chart, bar chart and bubble chart. And the following code is to actually generate each different plot. 

<br />

```
fig = go.Figure()
  
    

"""Set the if elseif function here to check whether the users choose Line Chart, Bar Chart or Bubble Chart, the first chunk
here is for the line chart"""    
if chart_visual == 'Line Chart':

    fig.add_trace(go.Scatter(x = df1.Year, y = df1.Doctorate_recipients,
                             mode = 'lines',
                             ))
    
    
"""Here is the chunk code for bar chart"""
elif chart_visual == 'Bar Chart':
    
    fig.add_trace(go.Bar(x = df1.Year, y = df1.Doctorate_recipients,
                             ))

"""Here is the chunk code for Bubble chart"""
elif chart_visual == 'Bubble Chart':
  
    fig.add_trace(go.Scatter(x=df1.Year, 
                             y=df1.Doctorate_recipients,
                             mode='markers',
                            ))
        
        
st.plotly_chart(fig, use_container_width=True)

```
##### Explanation: The above code is to generate the three different parts of the plots. If the user select line chart in the slection box, then the dashboard will generate a line chart; if the user select bar chart, the dashboard will generate bar chart; and if user select bubble chart it will genernate bubble chart. This dashboard can help users to detect Number of Doctorate recipients from 1958 to 2017 in the USA. 

<br />

![Dashboard1](https://user-images.githubusercontent.com/78027134/138784390-03e5012e-1168-45b7-833f-d34f9430c9a7.png)

<br />
<br />

2 The second dashboard on my streamlit website is for percentage change of Number of Doctorate recipients from 1958 to 2017. It is also an interesting dashboard that can reproduce the dataset into three different plots including: Line chart, Bar chart and Bubble chart. There is a selection box on the streamlit website so users can choose from different plots. Users have the chance to make choice that which charts they like the most so the dashboard will generate the plot they want. 


The dashboard will help a researcher to better understand how the percentage change of total number of Doctorate recipients through 1958 to 2017 in the USA. We can use the Bubble chart as an example, when users point their mouse at any bar of the plot, the dashboard will show that what year is the specific point and what is the percentage change of doctorate recipients in that year. And it is the same thing for the other two different types of charts. it is very clear to see that there is an increasing trend from 1960 to 1970. There are more and more people getting doctorate degrees at that time. And from 1970 to 1980; also during 2000 and 2010 it is obvious to see that the percentage change is negative. During that time, there are less people getting doctorate degrees. 


Thus, this dashboard helps researchers a lot to make the conclusion about specific time that the percentage change of number of Doctorate recipients from 1958 to 2017 in the USA. This interactive dashboard is really user-friendly which make researchers have better efficiency to gain information. And it is also an informative dashboard for students who want to get a doctorate degree in the future. 


```
"""Here is the code to set up the selection box for the second dashboard"""
chart_visual1 = st.selectbox(
    label="Select Charts type", options=['line Chart', 'bar Chart', 'Bubble Chart']
)
```

##### Explanation: The dataframe we use for second dashboard is the same as the first dashboard. And this is the code to generate the selection box for the second dashboard, so the users can choose from Line chart, bar chart and bubble chart. And the following code is to actually generate each different plot. 


```

fig1 = go.Figure()
  
    
"""Set the if elseif function here to check whether the users choose Line Chart, Bar Chart or Bubble Chart, the first chunk
here is for the line chart""" 
    
if chart_visual1 == 'line Chart':

    fig1.add_trace(go.Scatter(x = df1.Year, y = df1.percentage_change,
                             mode = 'lines',
                             ))

"""This chunk of code is for bar chart"""
elif chart_visual1 == 'bar Chart':
    
    fig1.add_trace(go.Bar(x = df1.Year, y = df1.percentage_change,
                             ))
    
    
"""This chun of code is for Bubble chart"""
elif chart_visual1 == 'Bubble Chart':
  
    fig1.add_trace(go.Scatter(x=df1.Year, 
                             y=df1.percentage_change,
                             mode='markers',
                            ))
        
        
st.plotly_chart(fig1, use_container_width=True)

```

##### Explanation: The above code is to generate the three different parts of the plots. If the user select line chart in the slection box, then the dashboard will generate a line chart; if the user select bar chart, the dashboard will generate bar chart; and if user select bubble chart it will genernate bubble chart. This dashboard can help users to better understand how the percentage change of total number of Doctorate recipients through 1958 to 2017 in the USA. It is also helpful for people to make decision on whether they want to get a doctorate degree.

<br />

![Dashboard2](https://user-images.githubusercontent.com/78027134/138798133-d6e4533a-0f01-484e-9b7c-6d0d52e3c85e.png)

<br />
<br />
<br />

3 The third dashboard on my streamlit website is an US map showing the number of doctorate recipients of each state in 2017. The US map is with all states in different colors. When the user point his mouse on the state, then there will shown the number of doctorate recipients in each state in the year of 2017. For example, if we put our mouse on the state of Texas, then we have the number of 4068 for this state. This is a very straightforward dashboard for us to see that how many doctorate recipients in each state in the year of 2017. so users can have a basic idea that which is state has the most people getting Phd degrees. 


Thus, this dashboard helps researchers a lot to make the conclusion about the total number of Doctorate recipients from each state is different from each other in 2017. This interactive dashboard is really user-friendly which make researchers have better efficiency to gain information. And it is also an informative dashboard for students and professors to do research about the number of doctorate recipients in each state through the years. 

<br />

##### I load the the second dataset that will generate the third dashboard
```
#Load the second dataset
df2 = pd.read_excel('sed17-sr-tab005.xlsx')

```



```
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
```

##### Explanation: The above code is to select the USA map and then combine the dataframe inside of the map to reflect the number of doctorate recipients in each of the state. And we use function to distinguish the different states so we use different colors on different states. And the code that can have the function that when user point mouse on each state, the interative dashboard can reflect the information of each state in the year of 2017. This dashboarrd is very user-friendly to make users have more convenience. 


<br />

![Dashboard3](https://user-images.githubusercontent.com/78027134/138798346-ed320d27-fe4f-4bc6-a0ce-018c748a864c.png)





<br />
<br />

4 The last dashboard on my streamlit website is a pie chart showing the number of doctorate recipients in the field of life sciences of top 20 Institution in 2017. It is an interactive pie chart for user to have fun with it. If you are the people who are very interested in the field of life science and would like to get a dcotorate degree in this filed then this plot is very important to you. It is showing the top list of the institutions that have the most doctorare recipients in the field of life science.

When users point their mouse upon each slice of the pie chart. For example, We have 244 doctorate recipiencet in life sicence field from Johns Hopkins University. If you are interested in a specific institution, you can point on the slice and see the number. This result may help your doctorate applictaion on that institution. 


This interactive pie chart dashboard is very user-friendly which can let both researchers and students efficiently gain information. The information can help people make better decision on their research!


##### I load the third dataset that will be used for the last dashboard
```
#Load the third dataset
df3 = pd.read_excel('sed17-sr-tab004.xlsx')
```

```

"""This code is to remove the first 5 rows from the dataframe and change the column names for the dataframe"""

df3 = df3.iloc[5:]
df3.columns = ['Top20_Institution', 'Rank', 'Doctorate_recipients']
df3 = df3.head(20)

```

##### Explanation: The above code is to make edition to the dataframe df3 in order to extract the data we want. The dashboard I will create is based on the dataframe that I extracted from here. 


```

"""This is the important code that can generate the pie chart dashboard"""


fig3 = px.pie(df3, values=df3.Doctorate_recipients, names=df3.Top20_Institution, color=df3.Top20_Institution,
              

             )


"""Add the plot title here to make the dashboard clear to users"""
fig3.update_layout(
    
title="<b>Top 20 Institutions in the life sciences field</b>")


st.plotly_chart(fig3)
```

##### Explanation: The code above is to generate the pie chart dashboard, and this is the dashboard to help a researcher to better understand how the total number of Doctorate recipients in the field of life sciences of each institution from the top 20 institutions is different from each other in 2017. This dashboard is also informative for student who want to apply for a doctorate degree in the field of life science. 


<br />

![Dashboard4](https://user-images.githubusercontent.com/78027134/138800856-d3dadc24-72b3-4159-abe8-34644867e9a6.png)


<br />
<br />