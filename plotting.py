import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns   
 
#lets dig into our dataset
df = pd.read_csv('./cleaned_polmaraton_results.csv')
print('Lets check the dataset after the data corrections')
print(df.head())
print('Basic statistic operations to gain more insights from the dataset')

df['Czas_minutes'] = pd.to_timedelta(df['Czas']).dt.total_seconds() / 60
df['czas_km_minutes'] = pd.to_timedelta('00:' + df['czas_km']).dt.total_seconds() / 60


print(df.head())

print(df)
print("Basic statistical summary:")
print(df.describe())

# separating results in groups, to present this data in various ways
time_bins = [60, 75, 90, 105, 120, 135, 180] 
time_labels = [
    '1. Best performances (0-75 min)',
    '2. Very good (75-90 min)',
    '3. Good (90-105 min)',
    '4. Average (105-120 min)',
    '5. Below Average (120-135 min)',
    '6. Low Performances (> 135 min)'
]

df['Time_Category'] = pd.cut(df['Czas_minutes'], bins=time_bins, labels=time_labels, include_lowest=True)

# time intervals for pace per km 
pace_bins = [0, 4, 4.5, 5, 5.5, 6, 6.5, 10]  
pace_labels = [
    '1. Best Performances (< 4 min/km)',
    '2. Very Good (4-4.5 min/km)',
    '3. Good (4.5-5 min/km)',
    '4. Above Average (5-5.5 min/km)',
    '5. Average (5.5-6 min/km)',
    '6. Below Average (6-6.5 min/km)',
    '7. Low Performances (> 6.5 min/km)'
]

df['Pace_Category'] = pd.cut(df['czas_km_minutes'], bins=pace_bins, labels=pace_labels, include_lowest=True)

#counting the number of participants ineach category
time_category_counts = df['Time_Category'].value_counts().sort_index()
pace_category_counts = df['Pace_Category'].value_counts().sort_index()

# histogram of race times 
plt.figure(figsize=(10, 6))
plt.hist(df['Czas_minutes'], bins=50, color='blue', alpha=0.7)
plt.title('Distribution of Race Times (minutes)')
plt.xlabel('Time (minutes)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# bar chart of race times 
plt.figure(figsize=(8, 6))
time_category_counts.plot(kind='bar', color='skyblue', alpha=0.7)
plt.title('Race Time Categories')
plt.xlabel('Category')
plt.ylabel('Number of Participants')
plt.grid(True)
plt.show()

# pie chart of race times
plt.figure(figsize=(8, 6))
time_category_counts.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('coolwarm', 7))
plt.title('Race Time Categories Distribution')
plt.ylabel('')  
plt.show()

# case no.2 Km/H
# histogram of pace per km
plt.figure(figsize=(10, 6))
plt.hist(df['czas_km_minutes'], bins=50, color='green', alpha=0.7)
plt.title('Distribution of Average Pace per Kilometer')
plt.xlabel('Pace per km')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Bar chart of Pace per km Categories
plt.figure(figsize=(8, 6))
pace_category_counts.plot(kind='bar', color='lightgreen', alpha=0.7)
plt.title('Pace per km Categories')
plt.xlabel('Category')
plt.ylabel('Number of Participants')
plt.grid(True)
plt.show()

# pie chart of Pace per km Categories
plt.figure(figsize=(8, 6))
pace_category_counts.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('viridis', 7))
plt.title('Pace per km Categories Distribution')
plt.ylabel('') 
plt.show()


# age vs time simple plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Wiek'], df['Czas_minutes'], alpha=0.5, color='purple')
plt.title('Age vs. Race Time')
plt.xlabel('Age')
plt.ylabel('Time (minutes)')
plt.grid(True)
plt.show()

#lets check how many participants we've got on each year we retrieved
yearly_participation = df['Year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
yearly_participation.plot(kind='bar', color='orange', alpha=0.7)
plt.title('Yearly Participation')
plt.xlabel('Year')
plt.ylabel('Number of Participants')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
df['Time_Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('coolwarm', 6), startangle=90)
plt.title('Race Time Categories Distribution')
plt.ylabel('')  # Hide y-label to make chart cleaner
plt.show()

# age vs time - Area chart
plt.figure(figsize=(10, 6))
df.groupby('Wiek')['Czas_minutes'].mean().plot(kind='area', color='lightblue', alpha=0.6)
plt.title('Average Time per Age Group')
plt.xlabel('Age')
plt.ylabel('Average Time (minutes)')
plt.grid(True)
plt.show()

# Pace - age, bar chart 
plt.figure(figsize=(10, 6))
df.groupby('Wiek')['czas_km_minutes'].mean().plot(kind='bar', color='lightgreen', alpha=0.7)
plt.title('Average Pace per Age Group')
plt.xlabel('Age')
plt.ylabel('Average Pace (minutes per km)')
plt.grid(True)
plt.show()
