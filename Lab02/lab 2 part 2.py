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
