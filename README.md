# multi-sensor-streamflow-prediction

Multi-Sensor Data Fusion for Streamflow Prediction
Godavari Basin, India
Overview

This project implements multi-sensor rainfall data fusion to improve streamflow prediction in the Godavari River Basin, India.

Rainfall sources:

Satellite rainfall from NASA GPM IMERG

Ground rainfall from India Meteorological Department

Streamflow discharge from Central Water Commission

The project evaluates whether combining multiple rainfall sources improves predictive accuracy.

Methodology

Data preprocessing and temporal alignment

Feature engineering (lag rainfall, rolling averages)

Baseline models (satellite-only, ground-only)

Early fusion (feature-level fusion)

Late fusion (model-level fusion)

Model evaluation using RMSE, MAE, and R²

Results

Early fusion significantly improves prediction accuracy compared to single-source rainfall inputs.

Tech Stack

Python

Pandas

NumPy

How to Run
pip install -r requirements.txt
python main.py
Author

Ghanishth Attrey
B.Tech Civil Engineering
IIT Patna

Scikit-learn

XGBoost
