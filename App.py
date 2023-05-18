import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

st.set_page_config(layout= 'wide')
data = pd.read_csv('Clean_Customer.csv')
 
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Shop Customer Dataset Analysis')
with row0_2:
    st.text("")
    st.subheader('App by [Merna Mamdoh](https://www.linkedin.com/in/merna-mamdouh-8958b523a/)')
row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown("You can find the source code in the [Ecommerce of Customer Churn GitHub Repository](https://github.com/ahmedsaeed620/Ecommerce-of-Customer-Churn-Mid-Project-.git)")

### Understanding Data ###
row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.markdown("This is the sample of dataframe after clean:")
    sample=st.dataframe(data.sample(10))
    btn=st.button("Display another sample")
    if btn:
        print(sample)
### Univariate Categorical variables ###
row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
with row4_1:
    st.subheader('Analysis Univariate For Categorical Variables ')
row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row5_1:
    st.markdown('What is the greatest value (Gender / Profession)?')    
    option = st.selectbox('selsect an option' , ['Gender','Profession'],key ="option_sec1")   
with row5_2:
    fig = px.bar(data_frame= data[option].value_counts() , y = option  ,  text_auto='0.3s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)

### Univariate Numerical Variables ###
row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
with row6_1:
    st.subheader('Analysis Univariate Numerical Variables')
row7_spacer1, row7_1, row7_spacer2, row7_2, row7_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row7_1:
    st.markdown('What is the highest (national income) and higher (spending score) and The highest years of (experience) and The most age group in this data ?')    
    option1 = st.selectbox('selsect an option' , ['Annual Income ($)', 'Age', 'Spending Score (1-100)', 'Work Experience','Family Size'],key = "tap_sec2")   
with row7_2:
    fig = px.histogram(data_frame= data , x = option1 )
    st.plotly_chart(fig)


### Target ###
row8_spacer1, row8_1, row8_spacer2 = st.columns((.2, 7.1, .2))
with row8_1:
 st.subheader('Analysis Bivariate  Categorical (Gender Value)')
row9_spacer1, row9_1, row9_spacer2, row9_2, row9_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row9_1:
    st.markdown('Most category earns higher income and has more years of experience And they spend more?')    
    option = st.selectbox('selsect an option' , ['Annual Income ($)', 'Age', 'Spending Score (1-100)', 'Work Experience','Family Size'],key = "tap_sec3")
with row9_2:
    fig = px.bar(data_frame=data.groupby('Gender').mean()
    [option].reset_index() 
    , x = 'Gender', y = option  ,  text_auto='0.2s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)
### Analysis Bivariate Categorical Variables ###
row9_spacer1, row9_1, row9_spacer2 = st.columns((.2, 7.1, .2))
with row9_1:
    st.subheader('Analysis Bivariate  Categorical (Profession Value)')
row10_spacer1, row10_1, row10_spacer2, row10_2, row10_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row10_1:
    st.markdown('The most job has the highest national income, the most group works in this job, and they have the highest number of years of experience?')    
    option = st.selectbox('selsect an option' , ['Annual Income ($)', 'Age', 'Spending Score (1-100)', 'Work Experience','Family Size'],key = "tap_sec4")
with row10_2:
    fig = px.bar(data_frame=data.groupby('Profession').mean()
    [option].reset_index() 
    , x = 'Profession', y = option  ,  text_auto='0.2s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)



### Analysis Bivariate Numerical Variables ###
row10_spacer1, row10_1, row10_spacer2 = st.columns((.2, 7.1, .2))
with row10_1:
    st.subheader('Maltivariate Variables')
row11_spacer1, row11_1, row11_spacer2, row11_2, row11_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row11_1:
    st.markdown('What is the average (Numircal value) for each of male and female in each profession ?')    
    option = st.selectbox('selsect an option' , ['Annual Income ($)', 'Age', 'Spending Score (1-100)', 'Work Experience','Family Size'],key = "tap_sec5")
with row11_2:
    fig = px.bar(data_frame=data.groupby(['Profession','Gender']).mean()
    [option].reset_index() 
    , x = 'Gender', y = option  ,color =  'Profession',   text_auto='0.2s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)
