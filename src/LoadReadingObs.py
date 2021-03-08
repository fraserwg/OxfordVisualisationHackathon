#!/usr/bin/env python3
import pandas as pd
import csv

data_path = '../data/reading_data.csv'

# Read in using pandas
df = pd.read_csv(data_path)


# Read in using csv module and convert to lists
with open('../data/reading_data.csv') as file:
    csv_file = csv.reader(file)
    data_set = list()
    for line in csv_file:
        data_set.append(line)

data_set_columns = list(zip(*data_set))  # List where each element corresponds to a data column

year = data_set_columns[0]
day = data_set_columns[2]
month = data_set_columns[1]
