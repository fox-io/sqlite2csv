import csv
import sqlite3

# Connect to database
db_file = 'main.sqlite'
conn = sqlite3.connect(db_file)
cur = conn.cursor()

# Get all table names
db_list = []
for db_name in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'"):
    db_list.append(db_name)

# Export all tables to csv
for table in db_list:
    try:
        cur.execute(f"SELECT * FROM {table[0]}")
        rows = cur.fetchall()
        with open(f"{table[0]}.csv", 'w', newline='') as table_csv:
            writer = csv.writer(table_csv)
            writer.writerows(rows)
    except sqlite3.Error as e:
        continue

# Close connection
conn.close()
