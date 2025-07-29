import sqlite3
from tabulate import tabulate
# Connect to the database
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT weather_type,MIN(Temperature),MAX(Temperature) FROM weather GROUP BY weather_type ")   # Replace with your actual table name

# Fetch and print results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()

column_names = [description[0] for description in cursor.description]
print("Column Names:", column_names)

print(tabulate(rows, headers=column_names, tablefmt="pretty"))