#!/usr/bin/env python3
import pandas as pd

data_path = '../data/ProcessedAGU.csv'

# Read in using pandas
df = pd.read_csv(data_path)


# Read in using csv module and convert to lists
with open('../data/ProcessedAGU.csv') as file:
    csv_file = csv.reader(file)
    data_set = list()
    for line in csv_file:
        data_set.append(line)

N, country, state, city, lon, lat, distance = list(zip(*data_set))
