import csv
import operator

with open('employee_data.csv', newline='') as f:
    reader = csv.reader(f)
    sortedlist = sorted(reader, key=operator.itemgetter(3), reverse=True)

with open('new_employee_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sortedlist)