import gradio as gr
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load(r"D:\car_price_predictor\model.joblib")

# Load dataset
car = pd.read_csv("Cleaned_Car_data.csv")
car.columns = car.columns.str.strip()

# Dropdown options
companies = sorted(car['company'].unique())
car_models = sorted(car['name'].unique())
years = sorted(car['year'].unique(), reverse=True)
fuel_types = list(car['fuel_type'].unique())

# Prediction function
def predict_price(company, car_model, year, fuel_type, kms_driven):
    input_df = pd.DataFrame(
        [[car_model, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )
    
    prediction = model.predict(input_df)
    return f"💰 Estimated Price: ₹ {round(prediction[0], 2)}"

# Interface
interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Dropdown(companies, label="Company"),
        gr.Dropdown(car_models, label="Model"),
        gr.Dropdown(years, label="Year"),
        gr.Dropdown(fuel_types, label="Fuel Type"),
        gr.Number(label="Kilometers Driven")
    ],
    outputs="text",
    title="🚗 Car Price Predictor",
    description="Enter details and get price instantly"
)

interface.launch()