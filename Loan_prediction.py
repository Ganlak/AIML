#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st


# In[3]:


df = pd.read_csv("E:\Analytic Vidya\Hackathon\submission.csv")


# In[2]:


st.header("Loan Prediction")
Loan_id = st.text_area("Please enter the loan id here:", placeholder='Loan id', height = 100)


# In[ ]:


if st.button("Submit"):
    
    output = df[df["Loan_ID"] == Loan_id]["Loan_Status"].values[0]
    Loan_status = pd.DataFrame()
    Loan_status["Loan_status"] = [output]
    st.title('output')
    st.dataframe(Loan_status)

