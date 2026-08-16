import streamlit as st
import pandas as pd
import plotly.express as px

from utils import *

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Stress Prediction",
    page_icon="🧠",
    layout="wide"
)

load_css()

# =====================================
# TITLE
# =====================================

st.title("🧠 AI Stress Prediction Dashboard")
st.caption(
    "Predict stress levels and receive personalized recommendations."
)

st.divider()

# =====================================
# PERSONAL INFORMATION
# =====================================

st.subheader("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        18,
        100,
        25
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    heart = st.number_input(
        "Heart Rate",
        40,
        180,
        80
    )

    bp = st.number_input(
        "Blood Pressure",
        80,
        200,
        120
    )

with col2:

    bmi = st.number_input(
        "BMI",
        10.0,
        50.0,
        24.0
    )

    smoking = st.selectbox(
        "Smoking",
        ["No", "Yes"]
    )

    alcohol = st.selectbox(
        "Alcohol Consumption",
        ["No", "Yes"]
    )

st.divider()

# =====================================
# LIFESTYLE FACTORS
# =====================================

st.subheader("🌙 Lifestyle Factors")

col1, col2 = st.columns(2)

with col1:

    sleep = st.slider(
        "Sleep Hours",
        0.0,
        12.0,
        7.0
    )

    work = st.slider(
        "Work Hours",
        0.0,
        16.0,
        8.0
    )

    screen = st.slider(
        "Screen Time",
        0.0,
        15.0,
        5.0
    )

with col2:

    physical = st.slider(
        "Physical Activity",
        0.0,
        5.0,
        2.0
    )

    caffeine = st.slider(
        "Caffeine Intake",
        0,
        10,
        2
    )

    meditation = st.slider(
        "Meditation Hours",
        0.0,
        5.0,
        1.0
    )

st.divider()

# =====================================
# MENTAL HEALTH FACTORS
# =====================================

st.subheader("🧠 Mental Health Factors")

col1, col2 = st.columns(2)

with col1:

    anxiety = st.slider(
        "Anxiety Score",
        0,
        10,
        5
    )

    depression = st.slider(
        "Depression Score",
        0,
        10,
        5
    )

    academic = st.slider(
        "Academic Pressure",
        0,
        10,
        5
    )

with col2:

    social = st.slider(
        "Social Interaction",
        0,
        10,
        5
    )

    financial = st.slider(
        "Financial Stress",
        0,
        10,
        5
    )

    family = st.slider(
        "Family Pressure",
        0,
        10,
        5
    )

st.divider()

# =====================================
# PREDICT BUTTON
# =====================================

predict = st.button(
    "🚀 Predict Stress Level",
    use_container_width=True
)

# =====================================
# PREDICTION LOGIC
# =====================================

if predict:

    stress_score = 0

    stress_score += anxiety * 3
    stress_score += depression * 3
    stress_score += financial * 2
    stress_score += academic * 2
    stress_score += family * 2

    stress_score -= sleep * 2
    stress_score -= physical * 2
    stress_score -= meditation * 3
    stress_score -= social

    if smoking == "Yes":
        stress_score += 5

    if alcohol == "Yes":
        stress_score += 5

    if caffeine >= 7:
        stress_score += 5

    if screen >= 8:
        stress_score += 5

    if stress_score < 20:

        result = "Low Stress"
        probs = [90, 8, 2]

    elif stress_score < 45:

        result = "Medium Stress"
        probs = [15, 75, 10]

    else:

        result = "High Stress"
        probs = [2, 8, 90]

    st.divider()

    if result == "Low Stress":
        st.success(f"## 🟢 {result}")

    elif result == "Medium Stress":
        st.warning(f"## 🟡 {result}")

    else:
        st.error(f"## 🔴 {result}")

    st.subheader("📊 Prediction Confidence")

    prob_df = pd.DataFrame({
        "Stress Level": [
            "Low",
            "Medium",
            "High"
        ],
        "Probability (%)": probs
    })

    fig = px.bar(
        prob_df,
        x="Stress Level",
        y="Probability (%)",
        text="Probability (%)",
        color="Stress Level",
        color_discrete_map={
            "Low": "#00D084",
            "Medium": "#FFB000",
            "High": "#FF4D6D"
        }
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("⚠ Risk Analysis")

    risks = []

    if anxiety >= 8:
        risks.append("High Anxiety Score")

    if depression >= 8:
        risks.append("High Depression Score")

    if sleep <= 5:
        risks.append("Poor Sleep Pattern")

    if financial >= 8:
        risks.append("High Financial Stress")

    if academic >= 8:
        risks.append("High Academic Pressure")

    if family >= 8:
        risks.append("High Family Pressure")

    if not risks:
        st.success(
            "No major stress risk factors detected."
        )
    else:
        for risk in risks:
            st.warning(risk)

    st.subheader("💡 Personalized Recommendations")

    if result == "Low Stress":

        st.success("""
✅ Maintain healthy sleep schedule

✅ Continue regular exercise

✅ Practice meditation

✅ Maintain work-life balance
""")

    elif result == "Medium Stress":

        st.warning("""
⚡ Improve sleep quality

⚡ Reduce screen time

⚡ Increase physical activity

⚡ Practice meditation daily
""")

    else:

        st.error("""
🚨 Improve sleep schedule

🚨 Reduce caffeine intake

🚨 Exercise regularly

🚨 Take regular breaks

🚨 Consider professional counseling
""")

# =====================================
# NAVIGATION
# =====================================

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("pages/1_Home.py")

with c2:
    if st.button("📊 Dataset Insights", use_container_width=True):
        st.switch_page("pages/2_Dataset_Insights.py")

with c3:
    if st.button("ℹ About Project", use_container_width=True):
        st.switch_page("pages/4_About_Project.py")

footer()