import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns   
import os
import matplotlib
matplotlib.use('Agg')  #gui issues

# Loading data
df = pd.read_csv('./cleaned_polmaraton_results.csv')
#print(df.head())

df['Czas_minutes'] = pd.to_timedelta(df['Czas']).dt.total_seconds() / 60
df['czas_km_minutes'] = pd.to_timedelta('00:' + df['czas_km']).dt.total_seconds() / 60

#print("Basic statistical summary:")
#print(df.describe())

# binning - performances
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

# Time intervals (pace per km)
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

time_category_counts = df['Time_Category'].value_counts().sort_index()
pace_category_counts = df['Pace_Category'].value_counts().sort_index()


#if not os.path.exists('static/images'):
#    os.makedirs('static/images')

def save_plot(filename):
    try:
        path = os.path.join('static', 'images', filename)
        #print(f"saving plot to {path}")  
        plt.savefig(path, bbox_inches='tight')
        plt.close()
    except Exception as e:
        print(f'Unable to save the plot image: {filename}')

# Histogram - race times
def plot_race_times_hist():
    plt.figure(figsize=(10, 6))
    plt.hist(df['Czas_minutes'], bins=50, color='blue', alpha=0.7)
    plt.title('Race Times (minutes) - distribution')
    plt.xlabel('Time (in minutes)')
    plt.ylabel('Frequency')
    plt.grid(True)
    save_plot('race_times_histogram.png')

# Bar chart - race times
def plot_race_time_categories():
    time_category_counts = df['Time_Category'].value_counts().sort_index()
    plt.figure(figsize=(8, 6))
    time_category_counts.plot(kind='bar', color='skyblue', alpha=0.7)
    plt.title('Race Time Categories')
    plt.xlabel('Category')
    plt.ylabel('Number of Participants')
    plt.grid(True)
    save_plot('race_time_categories.png')

# Scatter plot - age vs race time
def plot_age_vs_time():
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Wiek'], df['Czas_minutes'], alpha=0.5, color='purple')
    plt.title('Age vs race time')
    plt.xlabel('Age')
    plt.ylabel('Time (in minutes)')
    plt.grid(True)
    save_plot('age_vs_time.png')

# Histogram - pace per km
def histogram_pace():
    plt.figure(figsize=(10, 6))
    plt.hist(df['czas_km_minutes'], bins=50, color='green', alpha=0.7)
    plt.title('Average Pace per Kilometer')
    plt.xlabel('pace per km')
    plt.ylabel('Frequency')
    plt.grid(True)
    save_plot('histogram_pace.png')

# bar chart - pace per km categories
def pace_categories_perKM():
    plt.figure(figsize=(8, 6))
    pace_category_counts.plot(kind='bar', color='lightgreen', alpha=0.7)
    plt.title('Pace per km Categories')
    plt.xlabel('Category')
    plt.ylabel('Number of Participants')
    plt.grid(True)
    save_plot('pace_categories_perKM.png')

# Pie chart - pace per km categories
def pace_pie_chart():
    plt.figure(figsize=(8, 6))
    pace_category_counts.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('viridis', 7))
    plt.title('Pace per km Categories Distribution')
    plt.ylabel('')
    save_plot('pie_chart_pacePerKM.png')

# Scatter plot - age vs time
def age_v_time():
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Wiek'], df['Czas_minutes'], alpha=0.5, color='purple')
    plt.title('Age vs. Race Time')
    plt.xlabel('Age')
    plt.ylabel('Time (minutes)')
    plt.grid(True)
    save_plot('age_v_time.png')

# Bar chart - yearly participation 
def participants_count():
    yearly_participation = df['Year'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    yearly_participation.plot(kind='bar', color='orange', alpha=0.7)
    plt.title('Yearly Participation')
    plt.xlabel('Year')
    plt.ylabel('Number of Participants')
    plt.grid(True)
    save_plot('participants_count.png')

# Area chart - average time per age group
def age_vs_time():
    plt.figure(figsize=(10, 6))
    df.groupby('Wiek')['Czas_minutes'].mean().plot(kind='area', color='lightblue', alpha=0.6)
    plt.title('Average Time per Age Group')
    plt.xlabel('Age')
    plt.ylabel('Average Time (minutes)')
    plt.grid(True)
    save_plot('age_v_time_area.png')

# Bar chart - pace per age group
def pace_chart():
    plt.figure(figsize=(10, 6))
    df.groupby('Wiek')['czas_km_minutes'].mean().plot(kind='bar', color='lightgreen', alpha=0.7)
    plt.title('Average Pace per Age Group')
    plt.xlabel('Age')
    plt.ylabel('Average Pace (minutes per km)')
    plt.grid(True)
    save_plot('pace_chart.png')

#generating:
plot_race_times_hist()
plot_race_time_categories()
plot_age_vs_time()
histogram_pace()
pace_categories_perKM()
pace_pie_chart()
age_v_time()
pace_chart()
