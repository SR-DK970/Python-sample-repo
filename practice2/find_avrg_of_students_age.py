"""2. Write a program that reads a CSV file containing student information
(e.g., name, age, grade), and create a class to represent each student.
    Implement a method in the class to calculate the student's average grade,
    and write pytest cases to validate the functionality. """

import csv

# field names
column_headers = ['Name', 'Age', 'Grade']

# data rows of csv file
rows = [['Pavan', 12, 'A'],
        ['Nikhil', 10, 'B'],
        ['Revanth', 11, 'B'],
        ['Arif', 14, 'C'],
        ['Sravan', 15, 'B'],
        ['Mahesh', 13, 'C']]

# name of csv file
filename = "students_records.csv"


def modify_file():
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields and the data into rows
        csvwriter.writerow(column_headers)
        csvwriter.writerows(rows)
    print(csvfile)


modify_file()






