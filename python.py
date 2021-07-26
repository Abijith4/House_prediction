import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

from PIL import Image
import json
pickle_in = open('C:\\Users\\91944\\Desktop\\Chennai_house_price_final\\Chennai_home_prices_models.pickle','rb')
classifier = pickle.load(pickle_in)

def Welcome():
    return 'WELCOME ALL!'

def get_location_names():
    return Locations

global Locations
with open("C:\\Users\\91944\\Desktop\\Chennai_house_price_final\\columns1.json",'r')as f:
    data_columns=json.load(f)['data_columns']
    Locations=data_columns[3:]

def predict_price(location,sqft,bath,bhk):
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: location
        in: query
        type: text
        required: true
      - name: sqft
        in: query
        type: number
        required: true
      - name: bath
        in: query
        type: number
        required: true
      - name: bhk
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    #loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(77)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    #if loc_index >= 0:
        #   x[loc_index] = 1

    return classifier.predict([x])[0]

def main():
    st.title("Chennai House Rate Prediction")
    html_temp = """
    <h2 style="color:black;text-align:left;"> Streamlit House prediction ML App </h2>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    st.subheader('Please enter the required details:')
    #all_columns=x.columns.tolist()
    location = st.multiselect("Location",Locations)
    sqft = st.text_input("Sq-ft area","")
    bath = st.text_input("Number of Bathroom","")
    bhk = st.text_input("Number of BHK","")

    result=""

    if st.button("House Price in Lakhs"):
        result=predict_price(location,sqft,bath,bhk)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Please find the code at")
        st.text("https://github.com/Abijith4")

if __name__=='__main__':
    main()
