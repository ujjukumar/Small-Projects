''' Convert text file into a csv '''

import pandas as pd

read_file = pd.read_csv(r'named_list.txt')
read_file.to_csv(r'employee_data.csv', index = None)