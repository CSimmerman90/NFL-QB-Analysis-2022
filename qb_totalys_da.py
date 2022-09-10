import csv

filename = 'qb_data/top_qb_totals.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
