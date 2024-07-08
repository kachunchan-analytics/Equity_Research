#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
from sec_cik_mapper import StockMapper
global symbol

def add_zeros_to_cik():
    global symbol
    while True:
        symbol = input("Enter a ticker symbol: ")
        mapper = StockMapper()
        num = mapper.ticker_to_cik[f'{symbol.upper()}']
        if num.isdigit() and 0 < len(num) <= 10:
            return str(num).zfill(10)
        else:
            print("Invalid input. Please enter a numeric CIK number with 1-10 digits.")

cik = add_zeros_to_cik()

sec_url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
print(sec_url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

response = requests.get(sec_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    with open(f'./SEC_company_facts/{symbol.upper()}.json', 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Response saved as {symbol.upper()}.json")
else:
    print("Failed to retrieve data")


# In[ ]:




