
#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np   
import streamlit as st 
import pickle as p     

p_out = open("C:/Users/HP/final_model.pkl", "rb")
model = p.load(p_out)

def welcome():
    return "Welcome All"
def run():
    #st.sidebar.header('User Input Paramaters')
        #Region
    region_display = ('North','East','West','South','North East','North West','South East','South West')
    region_options = list(range(len(region_display)))
    Region = st.selectbox("Region",region_options, format_func=lambda x:region_display[x])
        
    if Region=='North':
            region_n=1
            region_nw=0
            region_sw=0
    elif Region=='North West':
            region_n=0
            region_nw=1
            region_sw=0
    elif Region=='South West':
            region_n=0
            region_nw=0
            region_sw=1
            
        ## State
    state_display = ('Karnataka', 'Haryana', 'Tamil Nadu', 'Jharkhand', 'Kerala',
                         'Andhra Pradesh', 'Bihar', 'Gujarat', 'Delhi', 'Maharashtra',
                         'West Bengal', 'Goa', 'Jammu and Kashmir', 'Assam', 'Rajasthan',
                         'Madhya Pradesh', 'Uttar Pradesh', 'Tripura', 'Himachal Pradesh',
                         'Orissa')
    state_options = list(range(len(state_display)))
    State = st.selectbox("State",state_options, format_func=lambda x: state_display[x])
    
    
        ## Consumer Profile
    cp_display = ('Business', 'Personal')
    cp_options = list(range(len(cp_display)))
    Consumer_profile = st.selectbox("Consumer Profile",cp_options, format_func=lambda x: cp_display[x])
        
    if Consumer_profile=='Business':
            Consumer_profile=0
    else:
            Consumer_profile=1
    
        ## Product Category
    pc_display = ('Entertainment', 'Household')
    pc_options = list(range(len(pc_display)))
    Product_category = st.selectbox("Product Category",pc_options, format_func=lambda x: pc_display[x])
        
        ## Area
    area_display = ('Urban', 'Rural')
    area_options = list(range(len(area_display)))
    Area = st.selectbox("Area",area_options, format_func=lambda x: area_display[x])
    
     ## City
    city_display = ('Bangalore', 'Chandigarh', 'Chennai', 'Ranchi', 'Kochi',
                        'Hyderabad', 'Patna', 'Purnea', 'Vadodara', 'New Delhi', 'Mumbai',
                        'Ahmedabad', 'Pune', 'Kolkata', 'Vizag', 'Panaji', 'Srinagar',
                        'Guwhati', 'Jaipur', 'Bhopal', 'Meerut', 'Delhi', 'Agartala',
                        'Shimla', 'Bhubaneswar', 'Vijayawada', 'Lucknow')
    city_options = list(range(len(city_display)))
    City = st.selectbox("City",city_options, format_func=lambda x: city_display[x])
     
        
        ## Product Type
    pt_display = ('AC','TV')
    pt_options = list(range(len(pt_display)))
    Product_type = st.selectbox("Product Type",pt_options, format_func=lambda x: pt_display[x])
    

    
         ## AC_1001_Issue
    AC_1001_Issue_display = ('No Issue','Repair','Replacement')
    AC_1001_Issue_options = list(range(len(AC_1001_Issue_display)))
    AC_1001_Issue = st.selectbox("AC 1001 Issue",AC_1001_Issue_options, format_func=lambda x: AC_1001_Issue_display[x])
        
    if AC_1001_Issue=='No Issue':
            AC_1001_Issue=0
    elif AC_1001_Issue=='Repair':
            AC_1001_Issue=0.5
    elif AC_1001_Issue=='Replacement':
            AC_1001_Issue=1
        
        ## AC_1003_Issue
    AC_1003_Issue_display = ('No Issue','Repair','Replacement')
    AC_1003_Issue_options = list(range(len(AC_1003_Issue_display)))
    AC_1003_Issue = st.selectbox("AC 1003 Issue",AC_1003_Issue_options, format_func=lambda x: AC_1003_Issue_display[x])
        
    
            

         ## AC_1002_Issue
    AC_1002_Issue_display = ('No Issue','Repair','Replacement')
    AC_1002_Issue_options = list(range(len(AC_1002_Issue_display)))
    AC_1002_Issue = st.selectbox("AC 1002 Issue",AC_1002_Issue_options, format_func=lambda x: AC_1002_Issue_display[x])
     
    if AC_1002_Issue=='No Issue':
            AC_1002_Issue=0
    elif AC_1002_Issue=='Repair':
            AC_1002_Issue=0.5
    elif AC_1002_Issue=='Replacement':
            AC_1002_Issue=1
            
        ## TV_2001_Issue
    TV_2001_Issue_display = ('No Issue','Repair','Replacement')
    TV_2001_Issue_options = list(range(len(TV_2001_Issue_display)))
    TV_2001_Issue = st.selectbox("TV 2001 Issue",TV_2001_Issue_options, format_func=lambda x: TV_2001_Issue_display[x])
        
    if TV_2001_Issue=='No Issue':
            TV_2001_Issue=0
    elif TV_2001_Issue=='Repair':
            TV_2001_Issue=0.5
    elif TV_2001_Issue=='Replacement':
            TV_2001_Issue=1
            
        ## TV_2003_Issue
    TV_2003_Issue_display = ('No Issue','Repair','Replacement')
    TV_2003_Issue_options = list(range(len(TV_2003_Issue_display)))
    TV_2003_Issue = st.selectbox("TV 2003 Issue",TV_2003_Issue_options, format_func=lambda x: TV_2003_Issue_display[x])
    
        
        ## TV_2002_Issue
    TV_2002_Issue_display = ('No Issue','Repair','Replacement')
    TV_2002_Issue_options = list(range(len(TV_2002_Issue_display)))
    TV_2002_Issue = st.selectbox("TV 2002 Issue",TV_2002_Issue_options, format_func=lambda x: TV_2002_Issue_display[x])
    
    if TV_2002_Issue=='No Issue':
        TV_2002_Issue=0
    elif TV_2002_Issue=='Repair':
        TV_2002_Issue=0.5
    elif TV_2002_Issue=='Replacement':
        TV_2002_Issue=1
    

       ## Service Centre Code
    service_centre_display = [10, 12, 14, 16, 15, 13, 11]
    service_centre_options = list(range(len(service_centre_display)))
    Service_Centre= st.selectbox("Service Centre Code",service_centre_options, format_func=lambda x: service_centre_display[x]) 

       ## Product Age
    product_Age = st.text_input("Product Age (in Days)",value=0)
       
       ## Claim Value
    Claim_Value = st.text_input("Claim Value (in INR)",value=0)
        
      ## Purchased from  
    purchased_from_display = ['Manufacturer', 'Dealer', 'Internet']
    purchased_from_options = list(range(len(purchased_from_display)))
    Purchased_from= st.selectbox("Mode of Purchase",purchased_from_options, format_func=lambda x: purchased_from_display[x])
    
    if Purchased_from == 'Manufacturer':
        Purchased_from = 2
    elif Purchased_from == 'Dealer':
        Purchased_from = 1
    else:
        Purchased_from = 0
    

        ## Call Details
    Call_details = st.text_input("Call Duration (in Minutes)")
       
        ## Purpose    
    purpose_display = ['Complaint', 'Claim', 'Other']
    purpose_options = list(range(len(purpose_display)))
    Purpose= st.selectbox("Purpose",purpose_options, format_func=lambda x: purpose_display[x])
    
    if Purpose == 'Claim':
        Purpose = 2
    elif Purpose == 'Complaint':
        Purpose = 1
    else:
        Purpose = 0
    
    
        
    Data = {'Area':Area,
            'Consumer_profile':Consumer_profile,
            'Product_category':Product_category,
            'Product_type':Product_type,
            'AC_1001_Issue':AC_1001_Issue,
            'AC_1002_Issue':AC_1002_Issue,
            'AC_1003_Issue':AC_1003_Issue,
            'TV_2001_Issue':TV_2001_Issue,
            'TV_2002_Issue':TV_2002_Issue,
            'TV_2003_Issue':TV_2003_Issue,
            'Claim_Value':Claim_Value,
            'product_Age':product_Age,
            'Purchased_from':Purchased_from,
            'Call_Details':Call_details,
            'Purpose':Purpose,
            'Service_Centre':Service_Centre
            }

                                     
    features = pd.DataFrame(Data,index=[0])
    return features

def main():
    st.sidebar.title("**About**")
   
    st.sidebar.subheader("Warranty Claim- Fraud Detection")
    st.sidebar.write("**Hello There! **")
    st.sidebar.write("This is a Machine Learning model")
    st.sidebar.write("Curious..? Want to try this..? Follow this Steps")
    st.sidebar.write("1.Input Values ")
    st.sidebar.write("2.Hit **Predict!** ")
    st.sidebar.write("After it will go directly to Machine Learning Model and It will Predict the ** Fraud Detection!!**")
    st.sidebar.title("Made With Streamlit")
    st.title("User Input parameters")
    df=run()  
    st.write(df)
    prediction = ""
    if st.button("Submit"):
        prediction = model.predict(df)
        #lc = [str(i) for i in prediction]
        #ans = int("".join(lc))
        if prediction == 0:
            st.success("This is genuine claim")   
        else:
            st.success("This is fraud claim") 
        

if __name__=='__main__':
    main()