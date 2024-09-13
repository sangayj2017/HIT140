import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


# Step 1: Load datasets
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')

# Merge datasets on 'ID'
merged_data = pd.merge(pd.merge(dataset1, dataset2, on='ID'), dataset3, on='ID')

# Step 3: Hypothesis testing - Is there a significant effect of screen time reduction on well-being?

# Group respondents based on their screen time
low_screen_time = merged_data[merged_data['C_we'] <= 2]  # Less screen time on weekends
high_screen_time = merged_data[merged_data['C_we'] > 2]  # More screen time on weekends

# Perform t-test on well-being scores between low and high screen time groups for 'Optm' (Optimism)
t_stat, p_value = stats.ttest_ind(low_screen_time['Optm'], high_screen_time['Optm'])

print(f"\nT-test for 'Optm' (Optimism): t-stat = {t_stat}, p-value = {p_value}")

# Interpret the result
if p_value < 0.05:
    print("The result is statistically significant; reducing screen time significantly affects well-being.")
else:
    print("The result is not statistically significant; screen time reduction may not affect well-being.")

# Step 5: Visualizations
# Scatter plot for screen time vs. well-being ('Optm')
plt.figure(figsize=(10, 6))
sns.scatterplot(x=merged_data['C_we'], y=merged_data['Optm'])
plt.title('Screen Time on Weekends vs. Feeling Optimistic')
plt.xlabel('Screen Time on Weekends (C_we)')
plt.ylabel('Feeling Optimistic (Optm)')
plt.grid(True)
plt.show()

# Correlation heatmap for screen time and well-being variables
plt.figure(figsize=(12, 8))
correlation_matrix = merged_data[screen_time_cols + well_being_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Screen Time and Well-Being Indicators')
plt.show()

