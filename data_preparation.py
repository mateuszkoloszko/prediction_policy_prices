import numpy as np
import pandas as pd


claims = pd.read_csv('claims.csv', sep=',')
policies = pd.read_csv('policies.csv', sep=',')

def prepare_data(data_one, data_two):
    final_data = pd.merge(data_one, data_two, on='POLICY_ID', how='left')

    final_data['CLAIM_NB'] = final_data['CLAIM_NB'].fillna(0)
    final_data['CLAIM_TOTAL_AMOUNT'] = final_data['CLAIM_TOTAL_AMOUNT'].fillna(0)

    final_data['CLAIM_FREQ'] = final_data['CLAIM_NB'] / final_data['EXPOSURE']
    final_data = final_data.drop(columns=['POLICY_ID'])

    model_data = final_data[final_data['CLAIM_NB'] != 0].copy()

    model_data['CLAIM_MEAN_AMOUNT'] = model_data['CLAIM_TOTAL_AMOUNT'] / model_data['CLAIM_NB']
    model_data['CLAIM_MEAN_AMOUNT_CAPPED'] = model_data['CLAIM_MEAN_AMOUNT'].clip(upper=50_000)

    drop_columns = ['CLAIM_TOTAL_AMOUNT', 'CLAIM_MEAN_AMOUNT', 'CLAIM_FREQ', 'EXPOSURE']
    model_data = model_data.drop(columns=drop_columns)

    return final_data, model_data

main_dataset, severity_dataset = prepare_data(policies, claims)

main_dataset.to_csv("main_dataset.csv", index=False)
severity_dataset.to_csv("severity_dataset.csv", index=False)