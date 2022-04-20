# SETUP

import streamlit as st
import pandas as pd
import datetime


#-------------------
# CREATE DATA

# Simple dataframe
df = pd.DataFrame({
    'A': [1, 4, 3, 2],
    'B': [10, 20, 30, 40]
    })

#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app
st.title("Meine erste App")
# Add header
st.header("Greatest Of All Time")
# Add a gif from https://giphy.com/
st.markdown("![Goat](https://media.giphy.com/media/41cZekVQWbG8ZcghDU/giphy.gif)")

#st.image("hdm-logo.jpg")
#-------------------
# BODY

#-------------------
# Show static DataFrame
st.dataframe(df)

#-------------------
# Bar chart
st.bar_chart (df)

#Sidebar erstellen
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

#Slider Beispiel
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

#Date importieren (das sidebar im ersten Code sorgt dafür, dass es bei der sidebar angezeigt wird)
d = st.sidebar.date_input(
     "When's your birthday",
     datetime.date(1997, 9, 2))
st.write('Your birthday is:', d)