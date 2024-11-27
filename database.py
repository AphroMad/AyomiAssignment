import sqlite3

# define connection and cursor

connection = sqlite3.connect('npi_results.db')

cursor = connection.cursor()

# create results table

command1 = """CREATE TABLE IF NOT EXISTS
result(calcul_id INTEGER PRIMARY KEY, npi TEXT)"""
cursor.execute(command1)

# add to results table

cursor.execute("INSERT INTO result VALUES (1, '3 4 +')")
cursor.execute("INSERT INTO result VALUES (2, '8 5 -')")


# get from results table

cursor.execute("SELECT * FROM result")

result = cursor.fetchall()
print(result)


# update 

cursor.execute("UPDATE result SET npi = '3 4 -' WHERE calcul_id = 1")

# delete 

cursor.execute("DELETE FROM result WHERE calcul_id = 2")

# close connection

connection.commit()
connection.close()
