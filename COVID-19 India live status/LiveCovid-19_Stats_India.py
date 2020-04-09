# This was originally in an article in geeksforgeeks. I just combined all together
# and modified the the graph plot to be more cleaner!
#  by:- Ujjawal Kumar

# importing libraries 
import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate
import os 
import numpy as np 
import matplotlib.pyplot as plt

# Fecthing the data from government site
extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['SNo', 'State','Total Confirmed Cases','Cured','Death']

response = requests.get(URL).content 
soup = BeautifulSoup(response, 'html.parser') 
header = extract_contents(soup.tr.find_all('th'))

stats = [] 
all_rows = soup.find_all('tr') 

for row in all_rows: 
	stat = extract_contents(row.find_all('td')) 
	if stat: 
		if len(stat) == 5: 
			stats.append(stat)
		elif len(stat) == 6: 
			stats.append(stat)

# Creating total cases
total_confirmed = 0
total_cured = 0
total_death = 0
serial_num_last = str(int(stats[-1][0]) + 1)
for i in range(len(stats)):
    total_confirmed+= int(stats[i][2])
    total_cured += int(stats[i][3])
    total_death += int(stats[i][4])

stats.append([serial_num_last, 'TOTAL CASES', total_confirmed, total_cured, total_death ])

# For tabulating the data
objects = [] 
for row in stats : 
	objects.append(row[1]) 

y_pos = np.arange(len(objects)) 

performance = [] 
for row in stats :
	performance.append(int(row[2]) + int(row[3])) 

table = tabulate(stats, headers=SHORT_HEADERS) 
print(table)


# For plotting a graph with matplotlib
del performance[-1]    # for removing total values from graph
del objects[-1]
y_pos = y_pos[:-1]

plt.barh(y_pos, performance, align='center', alpha=0.5, 
				color=(234/256.0, 128/256.0, 252/256.0), 
				edgecolor=(106/256.0, 27/256.0, 154/256.0)) 

plt.yticks(y_pos, objects) 
plt.xlabel('Number of Cases') 
plt.title('Corona Virus Cases')
for index, value in enumerate(performance):
    plt.text(value, index, str(value))
plt.show()