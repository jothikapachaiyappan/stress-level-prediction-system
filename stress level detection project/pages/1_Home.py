import streamlit as st
from utils import *

st.set_page_config(
    page_title="Stress Level Detection",
    page_icon="🧠",
    layout="wide"
)

load_css()

hero_banner()

st.success(
    "Welcome to the Stress Level Detection Dashboard."
)

kpi_cards()

st.divider()

st.subheader("📌 Project Overview")

st.write("""
This project predicts stress levels using Machine Learning algorithms.

The system helps users:

• Analyze stress factors

• Predict stress levels

• Understand risk patterns

• Generate recommendations
""")

feature_section()

navigation_buttons()

footer()