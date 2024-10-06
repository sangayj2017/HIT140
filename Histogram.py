import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV files
csv1 = pd.read_csv('dataset1.csv')
csv2 = pd.read_csv('dataset2.csv')
csv3 = pd.read_csv('dataset3.csv')

# Merge the dataframes
merged_df = csv1.merge(csv2, on='ID', how='outer').merge(csv3, on='ID', how='outer')

# Define screen time columns and well-being score columns
screen_time_cols = ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']
wellbeing_cols = ['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 'Loved', 'Intthg', 'Cheer']

# Calculate total screen time
merged_df['Total_Screen_Time'] = merged_df[screen_time_cols].sum(axis=1)

# Calculate average well-being score
merged_df['Avg_Wellbeing'] = merged_df[wellbeing_cols].mean(axis=1)

# 1. Histograms of screen time and well-being scores
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(merged_df['Total_Screen_Time'], kde=True)
plt.title('Distribution of Total Screen Time')
plt.xlabel('Total Screen Time')

plt.subplot(1, 2, 2)
sns.histplot(merged_df['Avg_Wellbeing'], kde=True)
plt.title('Distribution of Average Well-being Score')
plt.xlabel('Average Well-being Score')

plt.tight_layout()
plt.savefig('histograms.png')
plt.close()