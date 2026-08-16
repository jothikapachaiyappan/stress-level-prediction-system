import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

from utils import *


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Dataset Insights",
    page_icon="📊",
    layout="wide"
)

load_css()


# =====================================
# TITLE
# =====================================

st.title("📊 Dataset Insights Dashboard")

st.caption(
    "Explore and understand the stress level dataset through interactive analytics."
)


# =====================================
# LOAD DATA
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "stress_level.csv"

df = pd.read_csv(DATA_PATH)


# =====================================
# KPI SECTION
# =====================================

rows = df.shape[0]

cols = df.shape[1]

missing = df.isnull().sum().sum()

duplicates = df.duplicated().sum()


c1, c2, c3, c4 = st.columns(4)


with c1:

    st.success(
        f"""
        📄 Total Records

        ### {rows:,}
        """
    )


with c2:

    st.info(
        f"""
        📊 Features

        ### {cols}
        """
    )


with c3:

    st.warning(
        f"""
        ⚠ Missing Values

        ### {missing:,}
        """
    )


with c4:

    st.error(
        f"""
        🔁 Duplicate Records

        ### {duplicates:,}
        """
    )


st.divider()


# =====================================
# DATASET PREVIEW
# =====================================

with st.expander("🔍 View Dataset Sample"):

    st.dataframe(
        df.head(20),
        use_container_width=True
    )


st.divider()


# =====================================
# STRESS ANALYSIS
# =====================================

st.subheader("🧠 Stress Level Analytics")


col1, col2 = st.columns(2)


# =====================================
# DONUT CHART
# =====================================

with col1:

    fig = px.pie(
        df,
        names="Stress_Level",
        hole=0.65,
        title="Stress Level Distribution",
        color="Stress_Level",
        color_discrete_map={
            "Low": "#06D6A0",
            "Medium": "#FFD166",
            "High": "#EF476F"
        }
    )

    fig.update_traces(
        textinfo="percent+label",
        pull=[0.02, 0.02, 0.08]
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================
# GENDER VS STRESS
# =====================================

with col2:

    gender_stress = pd.crosstab(
        df["Gender"],
        df["Stress_Level"]
    )

    fig = px.bar(
        gender_stress,
        barmode="stack",
        title="Gender vs Stress Level",
        color_discrete_sequence=[
            "#4361EE",
            "#F72585",
            "#F8961E"
        ]
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Gender",
        yaxis_title="Count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


st.divider()


# =====================================
# MISSING VALUES ANALYSIS
# =====================================

st.subheader("⚠ Dataset Health Analysis")


missing_df = (
    df.isnull()
    .sum()
    .reset_index()
)


missing_df.columns = [
    "Feature",
    "Missing Values"
]


fig = px.bar(
    missing_df,
    x="Feature",
    y="Missing Values",
    color="Missing Values",
    title="Missing Values by Feature",
    color_continuous_scale=[
        "#00F5D4",
        "#4EA8DE",
        "#5A189A",
        "#F72585"
    ]
)


fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Features",
    yaxis_title="Missing Count"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# =====================================
# CORRELATION HEATMAP
# =====================================

st.subheader("🔥 Feature Correlation Heatmap")


numeric_df = df.select_dtypes(
    include="number"
)


fig, ax = plt.subplots(
    figsize=(12, 8)
)


sns.heatmap(
    numeric_df.corr(),
    cmap="magma",
    linewidths=0.5,
    annot=False,
    ax=ax
)


st.pyplot(fig)


st.divider()


# =====================================
# KEY INSIGHTS
# =====================================

st.subheader("📌 Key Insights")


col1, col2 = st.columns(2)


with col1:

    st.success(
        """
        ✅ Dataset contains sufficient records for machine learning.

        ✅ Missing values are available for preprocessing demonstration.

        ✅ Duplicate records can be used for data cleaning demonstrations.
        """
    )


with col2:

    st.info(
        """
        📈 Stress levels are influenced by multiple lifestyle factors.

        📈 Dataset supports classification models.

        📈 Suitable for Decision Tree, Random Forest, SVM and XGBoost.
        """
    )


st.divider()


# =====================================
# NAVIGATION
# =====================================

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_Home.py"
        )


with col2:

    if st.button(
        "🤖 Go to Stress Prediction",
        use_container_width=True
    ):

        st.switch_page(
            "pages/3_Stress_Prediction.py"
        )


# =====================================
# FOOTER
# =====================================

footer()
