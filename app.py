import streamlit as st
from OAM_1 import data_pel, grouped_data

st.title("Welcome to STREAM OAM")
st.bar_chart(data_pel)
st.bar_chart(grouped_data)