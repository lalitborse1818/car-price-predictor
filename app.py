import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CarPrice AI",
    page_icon="🚗",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.joblib")

# ---------------- LOAD DATA ----------------
car = pd.read_csv("Cleaned_Car_data.csv")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background: linear-gradient(135deg, #5B6CFF, #A855F7, #EC4899);
    color: white;
}

/* Remove top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main Glass Container */
.glass-container {
    background: rgba(255,255,255,0.10);
    border-radius: 30px;
    padding: 50px;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    margin-bottom: 40px;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 80px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 32px;
    color: #F3F3F3;
    margin-bottom: 10px;
}

/* Labels */
label {
    color: white !important;
    font-size: 20px !important;
    font-weight: 600;
}

/* Select Boxes */
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255,255,255,0.12);
    border-radius: 15px;
}

/* Number Input */
.stNumberInput input {
    background: rgba(255,255,255,0.12);
    color: white;
    border-radius: 15px;
}

/* Predict Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(to right, #FF4D6D, #FF758F);
    color: white;
    font-size: 28px;
    font-weight: bold;
    border-radius: 20px;
    height: 4em;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #FF758F, #FF4D6D);
}

/* Result Box */
.result-box {
    background: rgba(0,255,140,0.2);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    color: white;
    margin-top: 30px;
}

/* Hide Streamlit Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="glass-container">
    <div class="main-title">🚗 CarPrice AI</div>
    <div class="subtitle">
        Instant Car Valuation
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- FORM SECTION ----------------
st.markdown('<div class="glass-container">', unsafe_allow_html=True)

# First Row
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox(
        "🏢 Car Brand",
        sorted(car['company'].unique())
    )

with col2:
    car_model = st.selectbox(
        "🚘 Model",
        sorted(car['name'].unique())
    )

# Second Row
col3, col4 = st.columns(2)

with col3:
    year = st.selectbox(
        "📅 Year",
        sorted(car['year'].unique(), reverse=True)
    )

with col4:
    fuel_type = st.selectbox(
        "⛽ Fuel Type",
        car['fuel_type'].unique()
    )

# Kilometers
kms_driven = st.number_input(
    "🛣️ Kilometers Driven",
    min_value=0
)

# Predict Button
if st.button("✨ PREDICT PRICE NOW"):

    input_df = pd.DataFrame(
        [[car_model, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    prediction = model.predict(input_df)

    st.markdown(
        f"""
        <div class="result-box">
            Estimated Price: ₹ {round(prediction[0],2)}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)