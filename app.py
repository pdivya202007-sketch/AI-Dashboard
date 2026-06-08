import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Dashboard")

df = pd.read_csv("students.csv")

st.write(df)

st.write("Total Students:", len(df))

fig1 = px.bar(df, x="Name", y="Marks")
st.plotly_chart(fig1)

fig2 = px.pie(df, names="Name", values="Marks")
st.plotly_chart(fig2)

fig3 = px.scatter(df, x="Age", y="Marks")
st.plotly_chart(fig3)

df = pd.read_csv("students.csv")