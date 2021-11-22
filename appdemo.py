import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as data
import streamlit as st 

from datetime import datetime

sns.set_style('whitegrid')
plt.style.use('fivethirtyeight')

start_date = '2020-10-28'
end_date = '2021-10-28'

st.title('Stock Market Analysis')

user_input1 = st.text_input('Enter Stock Ticker1', 'AAPL')
df_a1 = data.DataReader(user_input1,'yahoo', start_date, end_date)
df_a1.head()

user_input2 = st.text_input('Enter Stock Ticker2', 'GOOG')
df_a2 = data.DataReader(user_input2,'yahoo', start_date, end_date)
df_a2.head()

user_input3 = st.text_input('Enter Stock Ticker3', 'MSFT')
df_a3 = data.DataReader(user_input3,'yahoo', start_date, end_date)
df_a3.head()

user_input4 = st.text_input('Enter Stock Ticker4', 'AMZN')
df_a4 = data.DataReader(user_input4,'yahoo', start_date, end_date)
df_a4.head()

company_list = [df_a1, df_a2, df_a3, df_a4]
company_name = [user_input1,user_input2, user_input3, user_input4]

for company, com_name in zip(company_list, company_name):
    company["company_name"] = com_name
    
df = pd.concat(company_list, axis=0)
df.head()

st.subheader('Data from 2020 - 2021')
st.write(df.describe())

tech_list = [user_input1,user_input2, user_input3, user_input4]

st.subheader('Closing price of all companies')
fig2 = plt.figure(figsize=(15,6))
plt.subplots_adjust(top =1.25, bottom =1.2)

for i, company in enumerate(company_list,1):
    plt.subplot(2, 2, i)
    company['Adj Close'].plot()
    plt.ylabel('Adj Close')
    plt.xlabel('Date')
    plt.title(f"Closing Price of {tech_list[i - 1]}")
    
plt.tight_layout()
st.pyplot(fig2)

st.subheader('Sales volume of all companies')
fig3 = plt.figure(figsize = (15,7))
plt.subplots_adjust(top =1.25, bottom =1.2)

for i, company in enumerate(company_list,1):
    plt.subplot(2,2,i)
    company['Volume'].plot()
    plt.ylabel("Volume")
    plt.xlabel ("date")
    plt.title(f"Sales Volume for {tech_list[i-1]}")
    
plt.tight_layout()
st.pyplot(fig3)

start_date = '2020-10-28'
end_date = '2021-10-28'

ticker = tech_list
df_closing = data.DataReader(ticker,'yahoo', start_date, end_date)['Adj Close']
tech_rets = df_closing.pct_change()

user_input5 = st.text_input(f'Enter any one of {tech_list}', 'GOOG')
user_input6 = st.text_input(f'Enter any one of {tech_list}', 'MSFT')

st.subheader('Joinplot of companies')
fig4 = sns.jointplot(user_input5 ,user_input6 , tech_rets, kind ='scatter', color = 'red')
st.pyplot(fig4)

st.subheader('Pairplot of companies')
fig5 = sns.pairplot(tech_rets, kind='reg')
st.pyplot(fig5)

st.subheader('PairGrid of companies')
fig6 = return_fig = sns.PairGrid(tech_rets.dropna())
return_fig.map_lower(plt.scatter, color='red')
return_fig.map_upper(sns.kdeplot, cmap='cool_d')
return_fig.map_diag(plt.hist, bins=30)
st.pyplot(fig6)