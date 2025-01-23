#!/usr/bin/python
"""
Purpose: Writing csv using csv module

"""
import csv

with open("fourth.csv", "w", newline="") as gh:
    header_names = ("sno", "name", "age", "designation")
    writer = csv.writer(gh, delimiter="/")

    # To write the headers
    writer.writerow(header_names)

    # print(dir(writer))
    writer.writerow([1, "akhila", 11, "carpenter"])
    writer.writerows([[2, "hiral", 12, "software"], [1, "neha", 13, "business"]])
    gh.close()


# assignment - create csv files with all possible delimiters and read the content also

#!/usr/bin/python
"""
Purpose: Writing and reading CSV files using various delimiters
"""
import csv

# Data for write
data = [
    ("sno", "name", "age", "designation"),
    (1, "akhila", 11, "carpenter"),
    (2, "hiral", 12, "software"),
    (3, "neha", 13, "business")
]

# List of delimiters to use
delimiters = [",", "|", ";", "\t", ":"]

# Writing CSV files with different delimiters
for delimiter in delimiters:
    filename = f"output_delimiter_{repr(delimiter)[1:-1]}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)
    print(f"File '{filename}' created with delimiter '{delimiter}'.")

# Reading and displaying content from each file
for delimiter in delimiters:
    filename = f"output_delimiter_{repr(delimiter)[1:-1]}.csv"
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter=delimiter)
        print(f"\nContent of file '{filename}' with delimiter '{delimiter}':")
        for row in reader:
            print(row)
