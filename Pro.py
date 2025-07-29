import sqlite3
from tabulate import tabulate
# Connect to the database
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
# Update rows where weather_type is 'Rain'
cursor.execute("""
UPDATE weather
SET is_holiday = 'yes'
WHERE weather_type = 'Drizzle'
""")
# Commit changes
conn.commit()
# Optional: Show the updated table
cursor.execute("SELECT is_holiday,weather_type FROM weather WHERE weather_type IN('Rain','Mist','Drizzle')")
rows = cursor.fetchall()
print(tabulate(rows, headers=[i[0] for i in cursor.description]))