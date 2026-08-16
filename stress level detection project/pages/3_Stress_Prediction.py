import streamlit as st
import pandas as pd
import plotly.express as px

from utils import *


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Stress Prediction",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# LOAD CSS
# =========================================================

load_css()


# =========================================================
# EXTRA CSS FOR PREDICTION PAGE
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       INPUT LABELS
       ===================================================== */

    .stNumberInput label,
    .stSelectbox label,
    .stSlider label {

        color: #FFFFFF !important;

        font-size: 18px !important;

        font-weight: 800 !important;

        opacity: 1 !important;

        line-height: 1.5 !important;
    }


    /* =====================================================
       NUMBER INPUT BOX
       ===================================================== */

    .stNumberInput input {

        color: #000000 !important;

        background-color: #FFFFFF !important;

        font-size: 17px !important;

        font-weight: 800 !important;

        opacity: 1 !important;
    }


    /* =====================================================
       SELECT BOX
       ===================================================== */

    .stSelectbox div[data-baseweb="select"] {

        background-color: #FFFFFF !important;

        border: 1px solid #CBD5E1 !important;

        border-radius: 10px !important;
    }


    .stSelectbox div[data-baseweb="select"] * {

        color: #000000 !important;

        font-size: 17px !important;

        font-weight: 800 !important;
    }


    /* =====================================================
       DROPDOWN MENU
       ===================================================== */

    div[data-baseweb="popover"] {

        background-color: #FFFFFF !important;
    }


    div[data-baseweb="popover"] * {

        color: #000000 !important;

        font-size: 16px !important;

        font-weight: 700 !important;
    }


    /* =====================================================
       SLIDER CURRENT VALUE
       ===================================================== */

    .stSlider [data-testid="stThumbValue"] {

        color: #FFFFFF !important;

        font-size: 17px !important;

        font-weight: 900 !important;
    }


    /* =====================================================
       SLIDER MINIMUM / MAXIMUM VALUES
       ===================================================== */

    .stSlider div[data-testid="stTickBarMin"],
    .stSlider div[data-testid="stTickBarMax"] {

        color: #FFFFFF !important;

        font-size: 15px !important;

        font-weight: 700 !important;
    }


    /* =====================================================
       HEADINGS
       ===================================================== */

    h1,
    h2,
    h3,
    h4 {

        color: #FFFFFF !important;

        font-weight: 900 !important;

        opacity: 1 !important;
    }


    /* =====================================================
       CAPTION
       ===================================================== */

    .stCaption {

        color: #FFFFFF !important;

        font-size: 15px !important;

        font-weight: 600 !important;
    }


    /* =====================================================
       BMI METRIC
       ===================================================== */

    div[data-testid="stMetric"] {

        background-color: rgba(
            37,
            99,
            235,
            0.25
        );

        border: 2px solid rgba(
            147,
            197,
            253,
            0.50
        );

        border-radius: 15px;

        padding: 15px;
    }


    div[data-testid="stMetricLabel"] {

        color: #FFFFFF !important;

        font-size: 17px !important;

        font-weight: 800 !important;
    }


    div[data-testid="stMetricValue"] {

        color: #FFFFFF !important;

        font-size: 32px !important;

        font-weight: 900 !important;
    }


    /* =====================================================
       BUTTONS
       ===================================================== */

    .stButton > button {

        color: #FFFFFF !important;

        font-size: 17px !important;

        font-weight: 800 !important;

        border-radius: 12px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PAGE TITLE
# =========================================================

st.title(
    "🧠 AI Stress Prediction Dashboard"
)

st.caption(
    "Predict stress levels and receive personalized recommendations."
)

st.divider()


# =========================================================
# PERSONAL INFORMATION
# =========================================================

st.subheader(
    "👤 Personal Information"
)

col1, col2 = st.columns(2)


# =========================================================
# LEFT COLUMN
# =========================================================

with col1:

    # -----------------------------------------------------
    # AGE
    # -----------------------------------------------------

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25,
        step=1
    )


    # -----------------------------------------------------
    # GENDER
    # -----------------------------------------------------

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )


    # -----------------------------------------------------
    # HEART RATE
    # -----------------------------------------------------

    heart = st.number_input(
        "Heart Rate",
        min_value=40,
        max_value=180,
        value=80,
        step=1
    )


    # -----------------------------------------------------
    # BLOOD PRESSURE
    # -----------------------------------------------------

    bp = st.number_input(
        "Blood Pressure",
        min_value=80,
        max_value=200,
        value=120,
        step=1
    )


# =========================================================
# RIGHT COLUMN
# =========================================================

with col2:

    # -----------------------------------------------------
    # HEIGHT
    # -----------------------------------------------------

    height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=165.0,
        step=0.5
    )


    # -----------------------------------------------------
    # WEIGHT
    # -----------------------------------------------------

    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=200.0,
        value=60.0,
        step=0.5
    )


    # =====================================================
    # AUTOMATIC BMI CALCULATION
    # =====================================================

    height_m = height / 100

    bmi = weight / (height_m ** 2)


    # =====================================================
    # DISPLAY BMI
    # =====================================================

    st.markdown(
        "### 🧮 Calculated BMI"
    )

    st.metric(
        label="BMI",
        value=f"{bmi:.2f}"
    )

    st.caption(
        "Automatically calculated from your height and weight."
    )


    # -----------------------------------------------------
    # SMOKING
    # -----------------------------------------------------

    smoking = st.selectbox(
        "Smoking",
        [
            "No",
            "Yes"
        ]
    )


    # -----------------------------------------------------
    # ALCOHOL
    # -----------------------------------------------------

    alcohol = st.selectbox(
        "Alcohol Consumption",
        [
            "No",
            "Yes"
        ]
    )


st.divider()


# =========================================================
# LIFESTYLE FACTORS
# =========================================================

st.subheader(
    "🌙 Lifestyle Factors"
)

col1, col2 = st.columns(2)


# =========================================================
# LIFESTYLE - LEFT
# =========================================================

with col1:

    # -----------------------------------------------------
    # SLEEP
    # -----------------------------------------------------

    sleep = st.slider(
        "Sleep Hours",
        min_value=0.0,
        max_value=12.0,
        value=7.0,
        step=0.5
    )


    # -----------------------------------------------------
    # WORK HOURS
    # -----------------------------------------------------

    work = st.slider(
        "Work Hours",
        min_value=0.0,
        max_value=16.0,
        value=8.0,
        step=0.5
    )


    # -----------------------------------------------------
    # SCREEN TIME
    # -----------------------------------------------------

    screen = st.slider(
        "Screen Time",
        min_value=0.0,
        max_value=15.0,
        value=5.0,
        step=0.5
    )


# =========================================================
# LIFESTYLE - RIGHT
# =========================================================

with col2:

    # -----------------------------------------------------
    # PHYSICAL ACTIVITY
    # -----------------------------------------------------

    physical = st.slider(
        "Physical Activity",
        min_value=0.0,
        max_value=5.0,
        value=2.0,
        step=0.5
    )


    # -----------------------------------------------------
    # CAFFEINE
    # -----------------------------------------------------

    caffeine = st.slider(
        "Caffeine Intake",
        min_value=0,
        max_value=10,
        value=2,
        step=1
    )


    # -----------------------------------------------------
    # MEDITATION
    # -----------------------------------------------------

    meditation = st.slider(
        "Meditation Hours",
        min_value=0.0,
        max_value=5.0,
        value=1.0,
        step=0.5
    )


st.divider()


# =========================================================
# MENTAL HEALTH FACTORS
# =========================================================

st.subheader(
    "🧠 Mental Health Factors"
)

col1, col2 = st.columns(2)


# =========================================================
# MENTAL HEALTH - LEFT
# =========================================================

with col1:

    # -----------------------------------------------------
    # ANXIETY
    # -----------------------------------------------------

    anxiety = st.slider(
        "Anxiety Score",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )


    # -----------------------------------------------------
    # DEPRESSION
    # -----------------------------------------------------

    depression = st.slider(
        "Depression Score",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )


    # -----------------------------------------------------
    # ACADEMIC PRESSURE
    # -----------------------------------------------------

    academic = st.slider(
        "Academic Pressure",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )


# =========================================================
# MENTAL HEALTH - RIGHT
# =========================================================

with col2:

    # -----------------------------------------------------
    # SOCIAL INTERACTION
    # -----------------------------------------------------

    social = st.slider(
        "Social Interaction",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )


    # -----------------------------------------------------
    # FINANCIAL STRESS
    # -----------------------------------------------------

    financial = st.slider(
        "Financial Stress",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )


    # -----------------------------------------------------
    # FAMILY PRESSURE
    # -----------------------------------------------------

    family = st.slider(
        "Family Pressure",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )


st.divider()


# =========================================================
# PREDICT BUTTON
# =========================================================

predict = st.button(
    "🚀 Predict Stress Level",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict:

    # -----------------------------------------------------
    # INITIAL STRESS SCORE
    # -----------------------------------------------------

    stress_score = 0


    # -----------------------------------------------------
    # STRESS FACTORS
    # -----------------------------------------------------

    stress_score += anxiety * 3

    stress_score += depression * 3

    stress_score += financial * 2

    stress_score += academic * 2

    stress_score += family * 2


    # -----------------------------------------------------
    # HEALTHY FACTORS
    # -----------------------------------------------------

    stress_score -= sleep * 2

    stress_score -= physical * 2

    stress_score -= meditation * 3

    stress_score -= social


    # -----------------------------------------------------
    # SMOKING
    # -----------------------------------------------------

    if smoking == "Yes":

        stress_score += 5


    # -----------------------------------------------------
    # ALCOHOL
    # -----------------------------------------------------

    if alcohol == "Yes":

        stress_score += 5


    # -----------------------------------------------------
    # CAFFEINE
    # -----------------------------------------------------

    if caffeine >= 7:

        stress_score += 5


    # -----------------------------------------------------
    # SCREEN TIME
    # -----------------------------------------------------

    if screen >= 8:

        stress_score += 5


    # =====================================================
    # STRESS LEVEL
    # =====================================================

    if stress_score < 20:

        result = "Low Stress"

        probs = [
            90,
            8,
            2
        ]


    elif stress_score < 45:

        result = "Medium Stress"

        probs = [
            15,
            75,
            10
        ]


    else:

        result = "High Stress"

        probs = [
            2,
            8,
            90
        ]


    st.divider()


    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    if result == "Low Stress":

        st.success(
            f"## 🟢 {result}"
        )


    elif result == "Medium Stress":

        st.warning(
            f"## 🟡 {result}"
        )


    else:

        st.error(
            f"## 🔴 {result}"
        )


    # =====================================================
    # PREDICTION CONFIDENCE
    # =====================================================

    st.subheader(
        "📊 Prediction Confidence"
    )


    prob_df = pd.DataFrame(
        {
            "Stress Level": [
                "Low",
                "Medium",
                "High"
            ],

            "Probability (%)": probs
        }
    )


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


    fig.update_layout(
        height=450
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # RISK ANALYSIS
    # =====================================================

    st.subheader(
        "⚠ Risk Analysis"
    )


    risks = []


    if anxiety >= 8:

        risks.append(
            "High Anxiety Score"
        )


    if depression >= 8:

        risks.append(
            "High Depression Score"
        )


    if sleep <= 5:

        risks.append(
            "Poor Sleep Pattern"
        )


    if financial >= 8:

        risks.append(
            "High Financial Stress"
        )


    if academic >= 8:

        risks.append(
            "High Academic Pressure"
        )


    if family >= 8:

        risks.append(
            "High Family Pressure"
        )


    if not risks:

        st.success(
            "No major stress risk factors detected."
        )


    else:

        for risk in risks:

            st.warning(
                risk
            )


    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    st.subheader(
        "💡 Personalized Recommendations"
    )


    if result == "Low Stress":

        st.success(
            """
            ✅ Maintain healthy sleep schedule

            ✅ Continue regular exercise

            ✅ Practice meditation

            ✅ Maintain work-life balance
            """
        )


    elif result == "Medium Stress":

        st.warning(
            """
            ⚡ Improve sleep quality

            ⚡ Reduce screen time

            ⚡ Increase physical activity

            ⚡ Practice meditation daily
            """
        )


    else:

        st.error(
            """
            🚨 Improve sleep schedule

            🚨 Reduce caffeine intake

            🚨 Exercise regularly

            🚨 Take regular breaks

            🚨 Consider professional counseling
            """
        )


# =========================================================
# NAVIGATION
# =========================================================

st.divider()


c1, c2, c3 = st.columns(3)


with c1:

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_Home.py"
        )


with c2:

    if st.button(
        "📊 Dataset Insights",
        use_container_width=True
    ):

        st.switch_page(
            "pages/2_Dataset_Insights.py"
        )


with c3:

    if st.button(
        "ℹ About Project",
        use_container_width=True
    ):

        st.switch_page(
            "pages/4_About_Project.py"
        )


# =========================================================
# FOOTER
# =========================================================

footer()
