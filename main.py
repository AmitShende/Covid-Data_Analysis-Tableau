# -*- coding: utf-8 -*-

import pandas as pd
import requests, os

import os
os.chdir('D:\\Data_science\\Projects\\Completed_projects\\Tableau_Covid_Python\\covid19_data_analysis_with_python-master')

#Step 1 Data Collection
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
req = requests.get(url)
data_list = pd.read_html(req.text) # to extract the tabular data from website
target_df = data_list[1] # Choosing the correct list containing the countrywise data of covid data in tabular form

target_df
target_df.info()

# After inspection of the data there are 6 different problems are identified from the data set as
# Column names, extra Columns, Extra rows at the end of the table, inconsistance country names, No data in some rows/columns and column type

#Step 2 Data Cleaning
target_df.columns
#Issue 1 Column Names
target_df.columns = ['Col0','Country Name','Total Cases','Total Deaths','Total Recoveries','Col5']
#Issue 2 Extra Columns
target_df = target_df[['Country Name','Total Cases','Total Deaths','Total Recoveries']]
#Issue 2 Extra Rows [Need Index number information]
#target_df = target_df.drop([229, 230])
last_idx = target_df.index[-1]
target_df = target_df.drop([last_idx, last_idx-1])
#Issue 4 Inconsistent Country Name
target_df['Country Name'] = target_df['Country Name'].str.replace('\[.*\]','')
#Issue 5 Extra Value ("No Data") in Columns (missing value replacement by '0' if data not available)
target_df['Total Recoveries'] = target_df['Total Recoveries'].str.replace('No data','0')
target_df['Total Cases'] = target_df['Total Cases'].str.replace('No data','0')
target_df['Total Deaths'] = target_df['Total Deaths'].str.replace('No data','0')

#Issue 6 Wrong Data Type
target_df['Total Cases'] = pd.to_numeric(target_df['Total Cases'])
target_df['Total Deaths'] = pd.to_numeric(target_df['Total Deaths'])
target_df['Total Recoveries'] = pd.to_numeric(target_df['Total Recoveries'])

#Step 3 Export The Data
target_df.to_excel(r'covid19_dataset.xlsx')

# Step 4 Visualising the data in Tableau

