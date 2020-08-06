import streamlit as st
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
import pickle5 as pickle

# import the machine learning algorithm
pickle_in = open("LogReg.pk1", "rb")
classifier = pickle.load(pickle_in)


def predict(age,gender,air_pollution,alcohol_use,dust_allergy,occupational_hazards,genetic_risk,wheezing,chronic_lung_disease,balanced_dietobesity,smoking,passive_smoker,chest_pain,coughing_of_blood,fatigue,weight_loss,shortness_of_breath,swallowing_difficulty,clubbing_of_finger_nails,frequent_cold,dry_cough,snoring,level):
    listT = [[int(age), int(gender), int(air_pollution), int(alcohol_use), int(dust_allergy), int(occupational_hazards), int(genetic_risk), int(wheezing), int(chronic_lung_disease), int(balanced_dietobesity), int(smoking), int(passive_smoker), int(chest_pain), int(coughing_of_blood), int(fatigue), int(weight_loss), int(shortness_of_breath), int(swallowing_difficulty), int(clubbing_of_finger_nails), int(frequent_cold), int(dry_cough), int(snoring), int(level)]]
    prediction = classifier.predict(listT)
    return prediction

def main():
    """ Lung Cancer Detector """


    html_temp = """
    <body style="background-color: red;"></body>
    <div style="background-color:green;padding:10px;margin-bottom:30px;">
    <h2 style="color:white;text-align:center;"><em>Lung Cancer Detector</em></h2>
    </div>
    </body>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("What is your age? (Age)")
    gender = st.selectbox(label='Choose gender', options=['', 'male', 'female'])
    air_pollution = st.text_input("On a scale of 1-10 how exposed are you to air pollution (1 - 10)")
    alcohol_use = st.text_input("On a scale of 1-10 how high is your intake of alcohol")
    dust_allergy = st.text_input("In what ratio are you allergic to dust?(1 - 10)")
    occupational_hazards = st.text_input("What is the frequency of occupational hazards where you work?(1 -10)")
    genetic_risk = st.text_input("do you have genetic issues(yes or no)")
    wheezing = st.text_input("On a scale of 1-10 how often do you wheeze?")
    chronic_lung_disease = st.text_input("Signs of lung cancer? 1 - 10")
    balanced_dietobesity = st.text_input("On a scale of 1-10 how  exposed are you balanced dietobesity")
    smoking = st.text_input("On a scale of 1-10 how much do you smoke")
    passive_smoker = st.text_input("On a scale of 1-10 how exposed are you to smokers")
    chest_pain = st.text_input("Do you have a chest pains?(1 - 10)")
    coughing_of_blood = st.text_input("On a scale of 1-10 how   would you grade if you have coughing of blood")
    fatigue = st.text_input("On a scale of 1-10 how often fatigued are you?")
    weight_loss = st.text_input("On a scale of 1-10 how  exposed are you weight loss")
    shortness_of_breath = st.text_input( "Signs of shortness of breathe?(1 - 10)")
    swallowing_difficulty = st.text_input("Do you have difficulties swallowing? scale of 1 - 10")
    clubbing_of_finger_nails = st.text_input("On a scale of 1-10 how often do you have clubs on your fingers",)
    frequent_cold = st.text_input("On a scale of 1-10 how frequent do you have cold")
    dry_cough = st.text_input("Do you have dry cough often? scale of 1 -10")
    snoring = st.text_input("Do you snore often?(1-10)")
    level = st.text_input("On a scale of 1-10 how levelled is your feeding")


    if gender.lower() == "male":
        gender = 1
    elif gender.lower() == "female":
        gender = 2


    result  = ""

    if st.button("Predict"):
        result=predict(age,gender,air_pollution,alcohol_use,dust_allergy,occupational_hazards,genetic_risk,wheezing,chronic_lung_disease,balanced_dietobesity,smoking,passive_smoker,chest_pain,coughing_of_blood,fatigue,weight_loss,shortness_of_breath,swallowing_difficulty,clubbing_of_finger_nails,frequent_cold,dry_cough,snoring, level)
    if result == 0:
        st.success('You have no chances or symptons of a lung cancer')
    elif result == 1:
        st.success('Sadly, You have chances of getting lung cancer, try visiting the Hospital')
    elif result == 2:
        st.success("Hello, you have lung cancer, Go to the Hospital now!")

    if st.button("About"):
        st.text("Learn more about Lung cancer")
        st.text("Built with Streamlit By Oluwafemi")


if __name__ == '__main__':
	main()
