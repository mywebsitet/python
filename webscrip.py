import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
get titel
title = soup.title
#get text
text = soup.get_text()
#get all href tage
soup.find_all('a')
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
#get rows
rows = soup.find_all("tr")
print(rows[:10])
list_rows = []
for row in rows:
    row_td = row.find_all('td')
    #print(row_td)
    #type(row_td)
    str_cells = str(row_td)
    #clean = re.compile('<.*?>')
    #clean2 = (re.sub(clean, '',str_cells))
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    #list_rows.append(clean2)
    list_rows.append(cleantext)
    #print(clean2)
    #type(clean2)

    #print(cleantext)
df = pd.DataFrame(list_rows)
df1 = df[0].str.split(',', expand=True)
df1.head()
col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str,"lxml").get_text()
all_header.append(cleantext2)
#print(all_header)
df2 = pd.DataFrame(all_header)
df3 = df2[0].str.split('[',expand=True)
df3.head()
freames = [df3, df1]
df4 = pd.concat(freames)
#df5 = df4.rename(columns=df4.iloc[0])
print(df4.head())
#print(df4.head(10))
