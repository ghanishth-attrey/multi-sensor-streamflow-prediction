# Multi-Sensor Data Fusion for Streamflow Prediction  
### Godavari Basin, India

## Overview

This project explores how combining multiple rainfall data sources can improve streamflow prediction in the Godavari River Basin.

In hydrology, rainfall measurement is always uncertain. Satellite data provides wide spatial coverage but may contain bias, while ground stations provide local accuracy but sparse coverage. I wanted to investigate whether combining these two sources using machine learning could improve discharge prediction performance.

This project implements and compares different fusion strategies using real rainfall and streamflow data.

---

## Motivation

During my study of remote sensing and hydrology, I became particularly interested in multi-sensor data fusion. Many research papers suggest that combining heterogeneous data sources can significantly improve predictive performance, but I wanted to test this practically using a structured ML pipeline.

The goal was not just to train a model, but to:

- Compare satellite-only vs ground-only rainfall models  
- Implement early (feature-level) fusion  
- Implement late (model-level) fusion  
- Quantify the improvement using proper metrics  

---

## Study Area

Godavari River Basin, India

The Godavari basin was selected because:

- It is one of the largest river basins in India  
- It experiences strong monsoon variability  
- It has complex hydrological response behavior  

This makes it a good candidate for testing rainfall fusion strategies.

---

## Data Sources

The datasets used in this project include:

- Satellite rainfall (GPM IMERG)  
- Ground rainfall (IMD gridded dataset)  
- Daily streamflow discharge (gauge station data)  

All datasets were aligned temporally and processed at daily resolution.

---

## Methodology

### 1. Data Preprocessing

- Converted all timestamps to daily format  
- Merged rainfall and discharge data by date  
- Removed missing values  
- Ensured consistent feature scaling  

---

### 2. Feature Engineering

To capture hydrological response behavior, I created:

- 1-day lag rainfall features  
- 3-day rolling average rainfall  
- Combined rainfall indicators  

These features help model delayed runoff effects after rainfall events.

---

### 3. Fusion Strategies

I implemented and compared:

**Baseline Models**
- Satellite rainfall only  
- Ground rainfall only  

**Early Fusion**
- Combined satellite and ground features before training  

**Late Fusion**
- Trained separate models and combined predictions using weighted averaging  

---

## Models Used

- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  

Random Forest performed particularly well due to its ability to capture nonlinear hydrological relationships.

---

## Evaluation Metrics

Model performance was evaluated using:

- RMSE (Root Mean Squared Error)  
- MAE (Mean Absolute Error)  
- R² Score  

---

## Results

The fusion-based approaches consistently outperformed single-source rainfall models.

Example comparison:

| Model Type     | RMSE | R²  |
|---------------|------|-----|
| Satellite Only | 0.93 | 0.72 |
| Ground Only    | 0.86 | 0.76 |
| Early Fusion   | 0.61 | 0.90 |
| Late Fusion    | 0.66 | 0.88 |

Key takeaways:

- Early fusion produced the strongest performance improvement.  
- Lag rainfall and rolling averages were highly important predictors.  
- Multi-sensor integration reduces prediction uncertainty.  

---

## Repository Structure

multi-sensor-streamflow-prediction/
│
├── data/
│   └── raw/
│
├── src/
│   ├── config.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── fusion.py
│   ├── models.py
│   ├── evaluation.py
│
├── main.py
├── requirements.txt
└── README.md

---

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Add your CSV files inside:

data/raw/

Required files:
- satellite.csv  
- ground.csv  
- streamflow.csv  

3. Run:

python main.py

---

## Future Improvements

If I extend this project further, I would like to:

- Implement LSTM-based time series models  
- Add SHAP-based feature explainability  
- Perform hyperparameter tuning with cross-validation  
- Explore bias correction for satellite rainfall  

---

## Author

Ghanishth Attrey  
B.Tech Civil Engineering  
Indian Institute of Technology Patna  

---
