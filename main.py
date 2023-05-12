import pandas as pd
import numpy as np
import streamlit as st
import time
import pickle as pkl
import skops.io as sio
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Calorie Calculator', page_icon=":wavy_dash:")


selected = option_menu(
    menu_title="Calorie Calculator",
    options=["Home", "Project", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon='calculator',
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#FFFFF"},
        "icon": {"font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#D0D0D0"},
        "nav-link-selected": {"background-color": "#9E7BFF"}
    }
)


# Home Tab:
if selected == "Home":
    st.write("    ")
    st.write("    ")

    # st.markdown(
    #     "<h2 style = 'text-align: center'> Calorie Calculator </h2>",
    #     unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('walk.png')
        st.write("   ")
        st.write("   ")
        st.write('**In this WebApp, you will be able to observe your `predicted calories burned` in your body.**')
        st.write("   ")
        st.write("   ")

        st.image('dumbbell.png')
    with col2:
        st.image('calculator.png')
        st.write("   ")
        st.write("   ")
        st.write("**You only have to pass your parameters like `Age`, `Gender`, `bmi`, etc into this WebApp.**")
        st.write("   ")
        st.write("   ")

        st.image('weight.png')
    with col3:
        st.image('heartrate.png')
        st.write("   ")
        st.write("   ")
        st.write(" **After you will be able to see the predicted value of `calories` that burned in your body.**")
        st.write("   ")
        st.write("   ")
        st.image('clock.png')


# Project Tab
if selected == "Project":
    st.markdown(
        "<h2 style = 'text-align: center'> Calories Burned Prediction </h2>",
        unsafe_allow_html=True)
    st.write("    ")
    st.write("    ")


    # st.image("https://assets.considerable.com/wp-content/uploads/2019/07/03093250/ExerciseRegimenPano.jpg" , use_column_width=True)

    def user_input_features():
        global gender, age, duration, heart_rate, body_temp, bmi
        gender_button = st.radio("Gender  ", ("Male", "Female"))

        if gender_button == 'Male':
            gender = 0
        else:
            gender = 1

        age = st.slider("Age (Year) ", 0, 100, 30)
        duration = st.slider("Activity Duration (min)  ", 0, 50, 15)
        heart_rate = st.slider("Heart Rate  ", 50, 150, 80)
        body_temp = st.slider("Body Temperature (C)  ", 35.0, 45.0, 40.38)
        bmi = st.slider("BMI  ", 15.0, 40.0, 20.20)

        data = {
            "Gender": ["Male" if gender_button == "Male" else "Female"],
            "Age": age,
            "Duration": duration,
            "Heart Rate": heart_rate,
            "Body Temp": body_temp,
            "BMI": bmi,

        }

        data_model = {
            "Gender": gender,
            "Age": age,
            "Duration": duration,
            "Heart Rate": heart_rate,
            "Body Temp": body_temp,
            "BMI": bmi,
        }

        features = pd.DataFrame(data_model, index=[0])
        data = pd.DataFrame(data, index=[0])
        return features, data


    df, data = user_input_features()

    st.write("---")
    st.header("Your Entries")
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        bar.progress(i + 1)
        time.sleep(0.01)
    st.write(data)

    st.write("---")
    st.header("Prediction")
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        # Update the progress bar with each iteration
        bar.progress(i + 1)
        time.sleep(0.01)

    model = pkl.load(open("Linear_Regressor.pkl", "rb"))

    x = np.round_(model.predict(np.array([[gender, age, duration, heart_rate, body_temp, bmi]]))[0], decimals=2)
    st.write("`{:.2f}`".format(x), " **Calories**")


# Contact Tab
if selected == "Contact":
    st.write("    ")
    st.markdown(
        "<h2 style = 'text-align: center'> Get in Touch </h2>", unsafe_allow_html=True)
    st.write("    ")
    st.write("    ")
    st.write("    ")
    st.write("    ")
    st.write("    ")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write("    ")

    with col2:
        st.image("github.png", width=60)
        st.write(":point_right: [GitHub](https://github.com/Swapnil2327)")
        st.write("    ")

    with col3:
        st.write("    ")

    with col4:
        st.image('linkdin.png', width=60)
        st.write(":point_right: [Linkedin](https://www.linkedin.com/in/swapnil-sawant-6a8840166)")
        st.markdown(
            "<h6 style = 'text-align: right; position: fixed; bottom: 0; right: 0;'> © 2022, Created by Swapnil Sawant </h6>",
            unsafe_allow_html=True)
    with col5:
        st.write("    ")


hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
