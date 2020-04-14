''' This Script takes CSV file from the given url and then prints output in the range specified '''

# Importing Libraries
import csv
import datetime
import requests
import operator

# url of CSV file
FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)

    # Decode all lines into strings
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def create_to_dictionary(start_date, lines):
    """Creates a dictionary from csv file type given."""

    # Initializing employees_dict
    employees_dict = {}

    # Removing first row from csv file and sorting it in ascendinng order
    reader = csv.reader(lines[1:])
    sortedlist = sorted(reader, key=operator.itemgetter(3))

    # Creating dictionary from each row in sortedlist
    for row in sortedlist:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        name = row[0] + ' ' + row[1]
        if row_date not in employees_dict:
            employees_dict[row_date] = [name]
        else:
            employees_dict[row_date].append(str(name))
    
    return employees_dict

def print_values(start_date, employees_dict):
    """Print in format if conditions matches."""

    for dict_date, employees in employees_dict.items():
        if dict_date <= datetime.datetime.today() and dict_date >= start_date:
            print("Started on {}: {}".format(dict_date.strftime("%b %d, %Y"), employees))


def main():
    
    start_date = get_start_date()
    employees_csv_list = get_file_lines(FILE_URL)
    sorted_employees = create_to_dictionary(start_date, employees_csv_list)
    print_values(start_date, sorted_employees)

if __name__ == "__main__":
    main()