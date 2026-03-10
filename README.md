# Insurance Pricing Pipeline (French MTPL Data)

## Overview
In this project, I build a simplified insurance pricing pipeline in Python using data inspired by the French Motor Third Party Liability (MTPL) market.
The project demonstrates how raw policy and claims data can be processed and used to create a basic actuarial pricing model.

## Steps

1. **Data Loading** – import policy and claims datasets.  
2. **Exploratory Data Analysis** – analyze data, distributions, correlations, detect outliers and plot data to identify relationships.  
3. **Data Processing** – merge datasets, clean data, handle missing values and engineer features.  
4. **Risk Modelling**
   - Frequency model (claim frequency) - predicts the expected number of claims per year
   - Severity model (average claim amount) - predicts the expected average cost of a single claim
5. **Actuarial Cost Calculation**
Combining the predictions to estimate the pure risk per policy

6. **Premium Calculation**
Calculating the final commercial price offered to the customer to ensure a specific profitability level

## Technologies

- Python  
- pandas  
- numpy  
- matplotlib / seaborn
- statsmodels / scikit-learn