# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 17:16:58 2022

@author: chaitu
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/chaitu/Desktop/Miniproject/homeloan_prediction.sav','rb'))

#creating function for prediction

def Homeloan_prediction(input_data):
    
    numpy_array=np.asarray(input_data)
    numpy_array=np.delete(numpy_array,0)
    numpy_array=np.char.replace(numpy_array,'Not-Graduate','0')
    numpy_array=np.char.replace(numpy_array,'Graduate','1')
    numpy_array=np.char.replace(numpy_array,'Male','1')
    numpy_array=np.char.replace(numpy_array,'Female','0')
    numpy_array=np.char.replace(numpy_array,'Yes','1')
    numpy_array=np.char.replace(numpy_array,'No','0')
    numpy_array=np.char.replace(numpy_array,'3+','4')
    numpy_array=np.char.replace(numpy_array,'Rural','0')
    numpy_array=np.char.replace(numpy_array,'Urban','2')
    numpy_array=np.char.replace(numpy_array,'Semiurban','1')


    input_data_reshape=numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshape)
    if(prediction[0]==1):
      return 'Loan Approved'
    else:
      return 'Loan Disapproved'


def main():
    
    #giving a title
    st.title('Home Loan Prediction Web App')
    
    #getting the input data from the user
    
    
    Loan_ID=st.text_input('Loan ID')
    Gender=st.radio('Gender',['Male','Female'],index=0)
    Married=st.radio('Married',['Yes','No'],index=0)
    Dependents=st.selectbox('Number of Dependents',['0','1','2','3+'],index=0)
    Education=st.radio('Education',['Graduate','Not-Graduate'])
    Self_Employed=st.radio('Self Employed',['Yes','No'],index=0)
    ApplicantIncome=st.number_input('Applicant Income')
    CoapplicantIncome=st.number_input('Co-Applicant Income')
    LoanAmount=st.number_input('Loan Amount')
    Loan_Amount_Term=st.number_input('Loan Amount Term')
    Credit_History=st.number_input('Credit History')
    Property_Area=st.radio('Property Area',['Rural','Urban','Semiurban'],index=0)
    
    
    #code for prediction
    predict=''
    
    #creating a button for prediction
    
    if st.button('Home Loan Result'):
        predict=Homeloan_prediction([Loan_ID, Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area])
        
        
        
    st.success(predict)
    
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
