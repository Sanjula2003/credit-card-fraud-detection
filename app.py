import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🚨",
    layout="wide"
)

model = joblib.load("fraud_detection_model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
            
section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}
                     
h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}
div[data-baseweb="input"] input {
    background-color: #1E1E1E !important;
    color: white !important;
}
.stButton>button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}
.stButton>button:hover {
    background-color: #FF6B6B;
    color: white;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🚨 Fraud Detection AI")

    st.markdown("---")

    st.markdown("### System Features")

    st.markdown("""
    - Real-Time Fraud Detection
    - XGBoost ML Model
    - Risk-Based Decisioning
    - Probability Scoring
    - Business-Friendly Dashboard
    """)

    st.markdown("---")

    st.markdown("### Risk Levels")

    st.success("Low Risk")
    st.warning("Medium Risk")
    st.error("High Risk")

st.title("🚨 AI-Powered Credit Card Fraud Detection System")
st.markdown("### Real-Time Transaction Risk Analysis using Machine Learning")

st.divider()

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric("ML Model", "XGBoost")
kpi2.metric("Detection Type", "Real-Time")
kpi3.metric("System Status", "Active")

st.divider()

st.subheader("Transaction Information")

col1, col2 = st.columns(2)

amount = col1.number_input(
    "Transaction Amount ($)",
    min_value=0.0,
    value=100.0
)

transaction_hour = col2.slider(
    "Transaction Hour",
    0,
    23,
    12
)

st.divider()

st.subheader("Risk Indicators")

col1, col2, col3 = st.columns(3)

risk_v1 = col1.slider(
    "Transaction Pattern Risk",
    -10.0,
    10.0,
    0.0
)
col1.caption("Unusual spending behavior patterns")

risk_v2 = col2.slider(
    "Location / Behavior Risk",
    -10.0,
    10.0,
    0.0
)
col2.caption("Suspicious location or user behavior")

risk_v3 = col3.slider(
    "Device / Velocity Risk",
    -10.0,
    10.0,
    0.0
)
col3.caption("Rapid activity or suspicious device usage")

st.divider()

st.subheader("Fraud Risk Prediction")

if st.button("Analyze Transaction Risk"):

    with st.spinner("Analyzing transaction risk..."):

        input_data = [0] * len(feature_names)

        input_data[feature_names.index("Amount")] = amount
        input_data[feature_names.index("Time")] = transaction_hour * 3600
        input_data[feature_names.index("V1")] = risk_v1
        input_data[feature_names.index("V2")] = risk_v2
        input_data[feature_names.index("V3")] = risk_v3

        input_df = pd.DataFrame([input_data], columns=feature_names)

        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)

        fraud_probability = probability[0][1] * 100
        normal_probability = probability[0][0] * 100

    st.divider()
    

    if fraud_probability < 30:
        risk_level = "LOW RISK"
        decision = "APPROVE TRANSACTION"
        alert_message = "✅ Transaction Appears Safe"
        alert_type = "success"

    elif fraud_probability < 70:
        risk_level = "MEDIUM RISK"
        decision = "SEND FOR MANUAL REVIEW"
        alert_message = "⚠️ Suspicious Transaction Detected"
        alert_type = "warning"

    else:
        risk_level = "HIGH RISK"
        decision = "BLOCK TRANSACTION"
        alert_message = "🚨 High Fraud Risk Detected"
        alert_type = "error"

    st.subheader("Fraud Analysis Result")

    if alert_type == "success":
        st.success(alert_message)
    elif alert_type == "warning":
        st.warning(alert_message)
    else:
        st.error(alert_message)

    col1, col2 = st.columns(2)
    col1.metric("Fraud Probability", f"{fraud_probability:.2f}%")
    col2.metric("Normal Probability", f"{normal_probability:.2f}%")

    st.caption("Fraud Risk Intensity")
    st.progress(min(int(fraud_probability), 100))

    st.subheader("Transaction Decision Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Amount", f"${amount:.2f}")
    col2.metric("Hour", f"{transaction_hour}:00")
    col3.metric("Risk Level", risk_level)
    col4.write("Decision")
    col4.success(decision)
 
st.divider()

st.caption(
    "AI-Powered Fraud Detection System | Built with Streamlit, XGBoost, and Machine Learning"
)