"""		This was originally in an article in geeksforgeeks. I made the code more cleaner and
		made various changes s per changing source (MOHFW India). I also modified the graph to  
		show numbers with plot.
		by:- Ujjawal Kumar    """

# Importing libraries 
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

allStatesList = [] 
all_rows = soup.find_all('tr') 

for row in all_rows: 
	stateList = extract_contents(row.find_all('td')) 
	if stateList: 
		if len(stateList) == 5: 
			allStatesList.append(stateList)

# Creating total cases
total_confirmed = 0
total_cured = 0
total_death = 0
serial_num_last = str(int(allStatesList[-1][0]) + 1)
for i in range(len(allStatesList)):
    total_confirmed+= int(allStatesList[i][2])
    total_cured += int(allStatesList[i][3])
    total_death += int(allStatesList[i][4])

allStatesList.append([serial_num_last, 'TOTAL CASES', total_confirmed, total_cured, total_death ])

# For tabulating the data

table = tabulate(allStatesList, headers=SHORT_HEADERS) 
print(table)

statesName = [] 
for row in allStatesList : 
	statesName.append(row[1]) 

serialNum = np.arange(len(statesName)) 

stateCases = [] 
for row in allStatesList :
	stateCases.append(int(row[2]) + int(row[3])) 

# For plotting a graph with matplotlib
del stateCases[-1]    # for removing total values from graph
del statesName[-1]
serialNum = serialNum[:-1]

plt.barh(serialNum, stateCases, align='center', alpha=0.5, 
				color=(234/256.0, 128/256.0, 252/256.0), 
				edgecolor=(106/256.0, 27/256.0, 154/256.0)) 

plt.yticks(serialNum, statesName) 
plt.xlabel('Number of Cases') 
plt.title('COVID-19 Cases per State')
for index, value in enumerate(stateCases):
    plt.text(value, index, str(value))
plt.show()