import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

years_and_pages = {
    'pp18': 81,
    'pp19': 79,
    'pp22': 54,
    'pp23': 52
}

data = []

for year, total_pages in years_and_pages.items():
    for page in range(1, total_pages + 1):
        url = f"https://www.polmaratonpraski.pl/startmeta/{year}/lista-startowa/{page}/?q=&k=&f=&sort=mUp&class=0"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table_body = soup.find('tbody', class_='fullList')
        for row in table_body.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) >= 5:
                uczestnik = columns[0].text.strip()

                pattern_start = r'^.*? '
                uczestnik = re.sub(pattern_start, 'XXX', uczestnik)
                pattern_end = r" .*$"
                uczestnik = re.sub(pattern_end, 'XXX', uczestnik)
                
                miejsce = columns[1].text.strip()
                miejsce_wg_plci = columns[2].text.strip()
                czas = columns[3].text.strip()
                rocznik = columns[4].text.strip()
                
                data.append([year, uczestnik, miejsce, miejsce_wg_plci, czas, rocznik])


df = pd.DataFrame(data, columns=['Year', 'Uczestnik', 'Miejsce', 'Miejsce wg płci', 'Czas', 'Rocznik'])

print(df)
df.to_csv('polmaraton_results_all_years.csv', index=False)
