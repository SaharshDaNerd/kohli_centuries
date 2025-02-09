# Kohli Performance Analysis

## Introduction
This Jupyter Notebook analyzes the cricket performance of **Virat Kohli** based on data from a CSV file (`kohli.csv`). The dataset is processed and visualized to extract insights.

## Data Preparation
### Libraries Used
```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
```
The notebook imports essential libraries for data manipulation and visualization.

### Loading and Cleaning Data
```python
kohli_df = pd.read_csv('kohli.csv', parse_dates=True)
kohli_df['Date'] = pd.to_datetime(kohli_df['Date'], format="mixed")
kohli_df['Year'] = kohli_df['Date'].dt.year
```
- Loads the CSV file.
- Converts the `Date` column to a proper **datetime** format.
- Extracts the `Year` for further analysis.

### Handling Runs and Not-Outs
```python
kohli_df['Runs'] = kohli_df['Runs'].astype(str)
kohli_df['Not Out'] = kohli_df['Runs'].str.contains("*", regex=False)
kohli_df['Runs'] = kohli_df['Runs'].str.replace('*','')
kohli_df['Runs'] = kohli_df['Runs'].str.replace(' ', '')
kohli_df['Runs'] = kohli_df['Runs'].astype(int)
kohli_df['Not Out'] = kohli_df['Not Out'].astype(str).replace("True","Not Out").replace("False","Out")
```
- Converts the `Runs` column into a numeric format.
- Extracts `Not Out` status by checking if `*` is present in `Runs`.
- Removes unnecessary spaces and symbols.

### Handling Match Results
```python
kohli_df['Result'] = kohli_df['Result'].str.replace(' ', '')
kohli_df[kohli_df['Result'] == 'Tied'].index
```
- Cleans the `Result` column by removing spaces.
- Identifies matches that ended in a **Tie**.

### Data Summary
```python
kohli_df.info()
```
- Displays dataset structure, including column types and missing values.
