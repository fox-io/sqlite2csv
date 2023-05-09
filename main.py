import csv
import sqlite3

db_file = ''
db_table = ''
conn = sqlite3.connect(db_file)
cur = conn.cursor()
data = cur.execute(f"SELECT * FROM {db_table}")

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
