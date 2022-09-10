import csv

# Import data manipulation modules
import pandas as pd
import numpy as np

# Import data visualization modules
import matplotlib as mpl
import matplotlib.pyplot as plt

filename = 'top_qb_pg.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    qbs = []
    for row in reader:
        qb = str(row[1])
        qbs.append(qb)

print(qbs)
