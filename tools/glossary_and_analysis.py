#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
import os
import json

stocks_json_files = []
counter = 0
folder_path = "./SEC_company_facts"  # Replace with your actual folder path

# Load JSON data from files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):  # only consider files with.json extension
        filepath = os.path.join(folder_path, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                stocks_json_files.append(data)
                counter += 1
        except Exception as e:
            print(f"Error loading file {filename}: {str(e)}")
    else:
        print(f"Skipping non-JSON file: {filename}")

print(f"There are {counter} Json files loaded")

# Create a DataFrame to store the facts and their counts
df = pd.DataFrame(columns=['facts', 'count'])

# Iterate over the JSON data and update the DataFrame
for i in stocks_json_files:
    key_list = i['facts']['us-gaap'].keys()
    for j in key_list:
        if j not in df['facts'].values:
            df.loc[len(df)] = [j, 1]  # add fact to the column and set count to 1
        else:
            idx = df[df['facts'] == j].index[0]
            df.at[idx, 'count'] += 1  # increment the count for the existing fact

df.to_excel('./glossary/glossary.xlsx', sheet_name='Glossary', index=False)


