import streamlit as st
import pandas as pd

st.title("📘 About Project")

comparison = pd.DataFrame({
    "Model":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy":[
        "96%",
        "XX%",
        "XX%"
    ]
})

st.subheader("Objective")

st.write("""
To detect stress levels using
machine learning algorithms.
""")

st.subheader(
    "Algorithms Used"
)

st.dataframe(comparison)

st.subheader(
    "Technologies Used"
)

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit
""")

st.subheader(
    "Conclusion"
)

st.write("""
Logistic Regression achieved the
highest accuracy and was selected
as the final model for predicting
stress levels.
""")