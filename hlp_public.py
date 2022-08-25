# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 17:16:58 2022

@author: chaitu
"""

import numpy as np
import pickle
import streamlit as st
import base64

#loading the saved model
loaded_model=pickle.load(open('homeloan_prediction.sav','rb'))
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
      return 'Loan has been Approved'
    else:
      return 'Loan has been Rejected'
  
#adding background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


def main():
    
    add_bg_from_local('Home.jpg')  
    #giving a title
    st.markdown("<h1 style='text-align: center;'>Home Loan Prediction</h1>", unsafe_allow_html=True)
    
    #getting the input data from the user
    
    Loan_ID=st.text_input("Enter Loan ID(required)")
    if not Loan_ID:
            st.warning("Please Enter Loan ID")
    Gender=st.radio('Gender',['Male','Female'],index=0)
    Married=st.radio('Married',['Yes','No'],index=0)
    Dependents=st.selectbox('Number of Dependents',['0','1','2','3+'],index=0)
    Education=st.radio('Education',['Graduate','Not-Graduate'])
    Self_Employed=st.radio('Self Employed',['Yes','No'],index=0)
    ApplicantIncome=st.number_input('Applicant Income',min_value=0)
    CoapplicantIncome=st.number_input('Co-Applicant Income',min_value=0)
    LoanAmount=st.number_input('Loan Amount',min_value=0)
    if not LoanAmount:
            st.warning("Please Enter Loan Amount")
    Loan_Amount_Term=st.number_input('Loan Amount Term',min_value=0)
    if not Loan_Amount_Term:
            st.warning("Please Ener Loan Amount Term")
    Credit_History=st.number_input('Credit History',min_value=0.00,max_value=1.00,step=0.01,)
    Property_Area=st.radio('Property Area',['Rural','Urban','Semiurban'],index=0)
    
    
    #code for prediction
    predict=''
    
    #creating a button for prediction
    
    if st.button('Home Loan Result'):
        if not Loan_ID or not LoanAmount or not Loan_Amount_Term:
                st.error("Please Enter required fields")
        else:
            predict=Homeloan_prediction([Loan_ID, Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area])

        
        
    st.success(predict)
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
