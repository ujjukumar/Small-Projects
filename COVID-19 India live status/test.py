"""		This was originally in an article in geeksforgeeks. I made the code more cleaner and
		made various changes as per changing source (MOHFW India). I also modified the graph to  
		show numbers along with plot.
		by:- Ujjawal Kumar    """

# Importing libraries 
from bs4 import BeautifulSoup 
from tabulate import tabulate
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime
from selenium import webdriver
import time
import json

def processData():
	"""	This function returns a json [list of dictionaries] that contains all
	the data about all states	"""

	#url of the page we want to scrape 
	url = "https://www.mohfw.gov.in/"

	# Initiating the webdriver. 
	driver = webdriver.Chrome('./chromedriver') 
	driver.get(url) 
	# To ensure that the page is loaded 
	time.sleep(5) 
	html = driver.page_source 

	# Applying bs4 to html variable
	soup = BeautifulSoup(html, "html.parser") 
	all_divs = soup.find(class_="statetable table table-striped") 
	driver.close() # closing the webdriver

	data = all_divs.find_all("td")
	statelist = []

	for row in data:
		a = row.get_text()
		statelist.append(a)

	# Removing entries of Total cases and extra strings at end
	del statelist[-11:]

	all_states = []
	headers = ["Serial No.", "State", "Total Active Cases", "Change in Active Cases", "Total Cases", 
	"Change in Total Cases", "Total Death", "Change in Total Death"]

	for i in range(35):
		state = {}
		for indx, entry in enumerate(headers):
			tmp = statelist[i*8 + indx].strip()
			if entry == "State":
				state[entry] = tmp
			else:
				if tmp == "":
					state[entry] = 0
				else:
					state[entry] = int(tmp)
	
		all_states.append(state)

	return all_states

def export_to_json(all_states, filename):
	with open(filename, "w", encoding="utf-8") as f:
		json.dump(all_states, f, indent=4)

def load_from_json(filepath):
	with open(filepath, encoding="utf-8") as f:
		return json.load(f)

def json_to_list(json_data):
	"""	Returns a list of lists for given list of dictioanries 	"""
	all_states_list = []
	for state in json_data:
		tmp = []
		for v in state.values():
			tmp.append(v)
		all_states_list.append(tmp)

	return all_states_list

def addTotalCount(allStatesList):
	""" Adding total cases entry to list of lists	"""

	allStatesList.append([
		allStatesList[-1][0] + 1,
		"ALL INDIA",
		sum([state[2] for state in allStatesList]),
		sum([state[3] for state in allStatesList]),
		sum([state[4] for state in allStatesList]),
		sum([state[5] for state in allStatesList]),
		sum([state[6] for state in allStatesList]),
		sum([state[7] for state in allStatesList]),
	])

def printTable(allStatesList):
	# For tabulating the data
	SHORT_HEADERS = ["Serial No.", "State", "Total Active Cases", "Total Cases", "Total Death"]

	modified_list = [[state[0], state[1], state[2], state[4], state[6]] for state in allStatesList]
	table = tabulate(modified_list, headers=SHORT_HEADERS) 
	print(table)

	print("\n\n")
	print("Moratlity Rate: ", round(modified_list[-1][4]*100/modified_list[-1][3], 2), "%")
	print("Recovery Rate: ", round(100.00 - modified_list[-1][2]*100/modified_list[-1][3], 2), "%")

def createStateData(state_data_list):
	# For creating statesList from allStatesList
	statesName = [state[1] for state in state_data_list] 
	stateCases = [state[4] for state in state_data_list]
	serialNum = np.arange(len(statesName))

	return serialNum, statesName, stateCases

def removeTotalCount(statesName, stateCases):
	# For removing total values to from graph
	del stateCases[-1]    
	del statesName[-1]

def plotGraph(serialNum, statesName, stateCases):
	# For plotting a graph with matplotlib
	plt.barh(serialNum, stateCases, align='center', alpha=0.5, 
					color=(234/256.0, 128/256.0, 252/256.0), 
					edgecolor=(106/256.0, 27/256.0, 154/256.0)) 

	today = datetime.today()
	today = today.strftime("%b %d %Y %T")
	plt.yticks(serialNum, statesName) 
	plt.xlabel(f'Number of Cases as of ({today})') 
	plt.title('COVID-19 Cases per State')
	for index, value in enumerate(stateCases):
		plt.text(value, index, str(value))
	plt.show()

def main():
	all_state_json = processData()
	export_to_json(all_state_json, f"covid_data_{datetime.today().strftime('%b %d %Y')}.json")

	# Uncomment below line to lode json data from disk for offline functionality
	# all_state_json = load_from_json("covid_data_new.json")

	all_state_list = json_to_list(all_state_json)
	# deleting old variable
	del all_state_json

	addTotalCount(all_state_list)
	
	# To print Table
	printTable(all_state_list)

	# For plotting
	serialNum, statesName, stateCases = createStateData(all_state_list)
	removeTotalCount(statesName, stateCases)
	plotGraph(serialNum[:-1], statesName, stateCases) # Removing last count from serialNum

if __name__ == "__main__":
	main()