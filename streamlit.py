# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 23:19:43 2023

@author: Suman
"""
def slicer(stri,leng):
    #return str[0:leng+2]
    x=float(stri)
    if(x!=0):
        xr=(round(x,leng))
    elif(x<=0.1):
        xr=0.0000
        #xr=(round(x,leng))
    return str(xr)

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

cgpa_model = pickle.load(open(r"/Users/sumankumarsahu/Desktop/Workspace/PROJECT/GIET STUDENT_S  MARK PRED/SAVED MODELS/cgpa_model.sav", 'rb'))
vst_model = pickle.load(open(r"/Users/sumankumarsahu/Desktop/Workspace/PROJECT/GIET STUDENT_S  MARK PRED/SAVED MODELS/vst_model.sav",'rb'))
cycle_model = pickle.load(open(r"/Users/sumankumarsahu/Desktop/Workspace/PROJECT/GIET STUDENT_S  MARK PRED/SAVED MODELS/cycle_model.sav",'rb'))
main_bg = "C:/Users/Suman/Desktop/GIET STUDENT'S  MARK PRED/5.jpg"
main_bg_ext = "jpg"
def load_custom_css():
    with open("/Users/sumankumarsahu/Desktop/Workspace/PROJECT/GIET STUDENT_S  MARK PRED/CSS FILE/css_.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load custom CSS
load_custom_css()

with st.sidebar:
    selected=option_menu("GIETU STUDENT'S GRADE PREDICTION", ["HOME PAGE","SGPA PREDICTION", "VST PREDICTION", "CYCLE TEST PREDICTION", "ABOUT US"],default_index=0)
    
if(selected=='HOME PAGE'):
    
     st.title("GIETU STUDENTS GRADE PREDICTION MODEL",)
     st.markdown("<h3>SGPA PREDICTION MODEL</h3>",unsafe_allow_html=True)
     st.markdown("~ This <b>SGPA  PREDICTION MODEL </b>' predicts the SGPA of your upcoming semester based on the historical data.<br>~ A Semester Grade Point Average (SGPA) prediction system is a software application or model that uses historical data and various input factors to predict a student's SGPA for an upcoming semester or term.<br>~ For the prediction purpose you have to fill all the fields that had been asked , then the model will predict the SGPA of your upcoming Semester.<br>~ This model consists of 4 inputs which are necessary to be filled by the Users. ",unsafe_allow_html=True)
     st.markdown("<h3>VST PREDICTION MODEL</h3>",unsafe_allow_html=True)
     st.markdown("~ This <b>VST PREDICTION MODEL</b>' predicts the VST of your upcoming VST based on the historical data.<br>~ A VST 'model prediction system' is a software application or tool that predicts the outcomes or results of class tests or assessments for students<br>~ For the prediction purpose you have to fill all the fields that had been asked , then the model will predict the VST of your upcoming Semester ",unsafe_allow_html=True)
     st.markdown("<h3>CYCLE TEST  PREDICTION MODEL</h3>",unsafe_allow_html=True)
     st.markdown("~ This <b>CYCLE TEST  PREDICTION MODEL</b>' predicts the Cycle Test mark of your upcoming Cycle-Test based on the historical data.<br>~ A 'Cycle Test Prediction Model' is a specialized software or analytical system designed to predict the outcomes or scores of cycle tests taken by students<br>~ Such prediction models can be valuable tools for both educators and students to anticipate performance and make informed decisions regarding their studies<br>~ For the prediction purpose you have to fill all the fields that had been asked , then the model will predict the VST of your upcoming Semester ",unsafe_allow_html=True)
     
#CGPA Prediction
if(selected=='SGPA PREDICTION'):
    st.title("GIETU STUDENTS SGPA PREDICTION")
    sem1 = st.number_input("Enter Semester 1 Grade", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
    sem2 = st.number_input("Enter Semester 2 Grade", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
    sem3 = st.number_input("Enter Semester 3 Grade", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
    sem4 = st.number_input("Enter Semester 4 Grade", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
    
    if st.button('PREDICT SGPA'):
        sgpa_prediction =cgpa_model.predict([[sem1,sem2,sem3,sem4]])
        cycle_pred_value=str(float(sgpa_prediction))
        st.title("The Predicted CGPA value is "+slicer(cycle_pred_value,2))
    
#for vst TEST Prediction
if (selected=='VST PREDICTION'):
    st.title("GIETU STUDENTS VST TEST Prediction")
    vst1sem1 = st.number_input("Enter VST Test 1 Mark of SEM 1 ", min_value=0.0, max_value=120.0, step=0.1, value=0.0)
    vst2sem1= st.number_input("Enter VST Test 2 Mark of SEM 1", min_value=0.0, max_value=120.0, step=0.1, value=0.0)
    vst1sem2 = st.number_input("Enter VST Test 1 Mark of SEM 2", min_value=0.0, max_value=120.0, step=0.1, value=0.0)
    vst2sem2= st.number_input("Enter VST Test 2 Mark of SEM 2", min_value=0.0, max_value=120.0, step=0.1, value=0.0)
    vst1sem3 = st.number_input("Enter VST Test 1 Mark of SEM 3", min_value=0.0, max_value=120.0, step=0.1, value=0.0)
    vst2sem3= st.number_input("Enter VST Test 2 Mark of SEM 3", min_value=0.0, max_value=120.0, step=0.1, value=0.0)
    vst1sem4 = st.number_input("Enter VST Test 1 Mark of SEM 4", min_value=0.0, max_value=120.0, step=0.1, value=0.0)
    vst2sem4= st.number_input("Enter VST Test 2 Mark of SEM 4", min_value=0.0, max_value=120.0, step=0.1, value=0.0)
    
    
    
    
    vst_predict = ''
    if st.button('PREDICT VST MARK'):
        vst_prediction =vst_model.predict([[vst1sem1,vst2sem1,vst1sem2,vst2sem2,vst1sem3,vst2sem3,vst1sem4,vst2sem4]])
        vst_pred=str(float(vst_prediction))
        st.title("The Predicted VST value is "+slicer(vst_pred,0))

    
    
    
#for CYCLE TEST Prediction
if (selected=='CYCLE TEST PREDICTION'):
    st.title("GIETU STUDENTS CYCLE TEST Prediction")
    c1s1 = st.number_input("Enter Mark of Cycle Test 1 SEM 1 ", min_value=0.0, max_value=180.0, step=0.1, value=0.0)
    c2s1= st.number_input("Enter Mark of Cycle Test 2 SEM 1", min_value=0.0, max_value=180.0, step=0.1, value=0.0)
    c1s2 = st.number_input("Enter Mark of Cycle Test 1 SEM 2", min_value=0.0, max_value=180.0, step=0.1, value=0.0)
    c2s2= st.number_input("Enter Mark of Cycle Test 2 SEM 2", min_value=0.0, max_value=180.0, step=0.1, value=0.0)
    c1s3 = st.number_input("Enter Mark of Cycle Test 1 SEM 3", min_value=0.0, max_value=180.0, step=0.1, value=0.0)
    c2s3= st.number_input("Enter Mark of Cycle Test 2 SEM 3", min_value=0.0, max_value=180.0, step=0.1, value=0.0)
    c1s4 = st.number_input("Enter Mark of Cycle Test 1 SEM 4", min_value=0.0, max_value=180.0, step=0.1, value=0.0)
    c2s4= st.number_input("Enter Mark of Cycle Test2 SEM 4", min_value=0.0, max_value=180.0, step=0.1, value=0.0)
    
    
    
    
    cycle_predict = ''
    if st.button('PREDICT CYCLE TEST MARK'):
        cycle_prediction =cycle_model.predict([[c1s1,c2s1,c1s2,c2s2,c1s3,c2s3,c1s4,c2s4]])
        cycle_pred_value=str(float(cycle_prediction))
        st.title("The Predicted Cycle Test value is " +slicer(cycle_pred_value, 0))
        
        
#ABOUT US:
if(selected=='ABOUT US'):
    st.title("ABOUT US")
    st.markdown(
        """
        Welcome to our About Us page! We are a dedicated team of professionals passionate about our work.In this project we have worked on machine learning model, in which the model will be able to predicting the Grade of SGPA , Mark of upcoming VST and The Cycle Test's Mark based on the past records according to the user's input. This is a real-world based machine learning model which will help students in order to predict their respective exam grades.
        The mission of a Student Result Prediction System is to leverage data-driven insights and predictive analytics to enhance the educational experience and outcomes of students to empower educational institutions and students by harnessing the power of data and predictive analytics, personalize education,improve decision-making,enhance efficiency,foster accountability.
        A Student's Result Prediction System offers several benefits to educational institutions, students, teachers, and administrators in early intervention,personalized learning,improved academic planning.
        """
    )
    st.title('OUR TEAM')
    img_url1=Image.open("/Users/sumankumarsahu/Desktop/Workspace/PROJECT/GIET STUDENT_S  MARK PRED/IMAGES/5 (1).jpg")
    img_url2=Image.open("/Users/sumankumarsahu/Desktop/Workspace/PROJECT/GIET STUDENT_S  MARK PRED/IMAGES/5 (1).jpg")
    img_url3=Image.open("/Users/sumankumarsahu/Desktop/Workspace/PROJECT/GIET STUDENT_S  MARK PRED/IMAGES/5 (1).jpg")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(img_url1, use_column_width=True)
        st.markdown("<center><b>SUMAN KUMAR SAHU <br>SECTION- DS('A')<br>21CSEDS031</b></center>", unsafe_allow_html=True)
    with col2:
        st.image(img_url2, use_column_width= True)
        st.markdown("<center><b>SUMAN KUMAR SAHU <br>SECTION- DS('A')<br>21CSEDS035</center></b>", unsafe_allow_html=True)
    with col3:
        st.image(img_url3, use_column_width=True)
        st.markdown("<center><b>SUMAN KUMAR SAHU <br>SECTION- DS('A')<br>21CSEDS03</b></center>", unsafe_allow_html=True)
        
    
        
    

