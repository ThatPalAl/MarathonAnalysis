import pandas as pd
import numpy as np 

df = pd.read_csv('./polmaraton_results_all_years.csv')
print(df.head())
print(df['Uczestnik'][0])

#'Cleaning Uczestnik':
print(df.iloc[0])
df['Uczestnik'] = df['Uczestnik'].str.replace('\n', '').str.replace(r'\s+', ' ', regex=True).str.strip()


print(df.head(30))
pattern_uczestnik = r'^.*? '
df['Uczestnik'] = df['Uczestnik'].str.replace(pattern_uczestnik, 'XXX', regex=True)
print(df.head(30))

pattern_uczestnik_end = r" .*$"
df['Uczestnik'] = df['Uczestnik'].str.replace(pattern_uczestnik_end, 'XXX', regex=True)

#Cleaning year
df = df.copy()
print(df.keys())
pattern_year = r"pp"


df['Year'] = df['Year'].str.replace(pattern_year, '', regex=True)
#Assuming each half marathon took place after year 2000
df['Year'] = '20' + df['Year']
print(df.head(40))
print(df[df['Miejsce'] == 6283])
print(df[df['Miejsce'] == 6282])

#'Rocznik' config
df['Year'] = df['Year'].astype(int)
df['Rocznik'] = df['Year'] - df['Rocznik']
df.rename(columns={'Rocznik' : 'Wiek'}, inplace=True)

#Czas_minuty value might be easier for statistical operations 
df[['hours', 'minutes', 'seconds']] = df['Czas'].apply(lambda czas: list(map(int, czas.split(':')))).apply(pd.Series)
df['czas_MMSS'] = df.apply(lambda row: f"{row['hours'] * 60 + row['minutes']:02d}:{row['seconds']:02d}", axis=1)

#Czas per km 
df['total_seconds'] = df.apply(lambda row: row['hours'] * 3600 + row['minutes'] * 60 + row['seconds'], axis=1)
df['czas_km'] = df['total_seconds'].apply(
    lambda total_seconds: f"{int(total_seconds / 21.0975 // 60):02d}:{int(total_seconds / 21.0975 % 60):02d}"
)

print(df.head())

#Remove values which were only helpful for main columns
df.drop(columns=['hours', 'minutes', 'seconds', 'total_seconds'], inplace=True)
print(df.head())
#Save the file for analitical operations
df.to_csv('cleaned_polmaraton_results.csv', index = False)