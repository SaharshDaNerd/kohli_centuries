import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
kohli_df = pd.read_csv('kohli.csv',parse_dates=True)
kohli_df['Date'] = pd.to_datetime(kohli_df['Date'], format="mixed")
kohli_df['Year'] = kohli_df['Date'].dt.year 
kohli_df['Runs'] = kohli_df['Runs'].astype(str)
kohli_df['Not Out'] = kohli_df['Runs'].str.contains("*",regex=False)
kohli_df['Runs'] = kohli_df['Runs'].str.replace('*','')
kohli_df['Runs'] = kohli_df['Runs'].str.replace(' ', '')
kohli_df['Runs'] = kohli_df['Runs'].astype(str).astype(int)
sns.barplot(kohli_df['Against'].value_counts())
plt.show()