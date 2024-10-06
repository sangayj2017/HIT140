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

# 2. Scatter plot of screen time vs. well-being scores
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Total_Screen_Time', y='Avg_Wellbeing', data=merged_df)
plt.title('Total Screen Time vs Average Well-being Score')
plt.xlabel('Total Screen Time')
plt.ylabel('Average Well-being Score')
plt.savefig('scatter_plot.png')
plt.close()