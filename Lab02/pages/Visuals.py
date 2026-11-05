# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import altair as alt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
with open('data.json','r') as file:
    food_data = json.load(file)

st.subheader('My favorite foods')
ratings = pd.DataFrame(food_data['data_points'])
st.bar_chart(ratings,x = 'Food', y = 'Rating')

if "min_rating" not in st.session_state:
    st.session_state["min_rating"] = 1

st.slider("Minimum food rating", 1, 10, key="min_rating")

foodList = []
for food in food_data['data_points']:
    if food['Rating']>=st.session_state['min_rating']:
        foodList.append(food)
filtered_ratings = pd.DataFrame(foodList)

st.subheader('My favorite foods chart')
piechart = alt.Chart(filtered_ratings).mark_arc().encode(theta='Rating:Q', color ='Food:N')

st.altair_chart(piechart)

survey_data = pd.read_csv("data.csv")

st.bar_chart(survey_data, x="Category", y="Value")

if "csv_min_rating" not in st.session_state:
    st.session_state["csv_min_rating"] = 1

st.slider("Minimum survey rating", 1, 10, key="csv_min_rating")

filtered_survey = survey_data[survey_data["Value"] >= st.session_state["csv_min_rating"]]

st.subheader('Survey Food Ratings')
survey_pie = alt.Chart(filtered_survey).mark_arc().encode(theta="Value:Q",color="Category:N")

st.altair_chart(survey_pie)

# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
