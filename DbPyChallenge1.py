

import sqlite3

# Connect to RAM SQLite db
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Roster table created here
cursor.execute('''
    CREATE TABLE Roster (
        Name TEXT,
        Species TEXT,
        IQ INT
    )
''')

# Insert data into the Roster table
insert_data = [
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Human", 100),
    ("Ak'not", "Mangalore", -5)
]

cursor.executemany('INSERT INTO Roster (Name, Species, IQ) VALUES (?, ?, ?)', insert_data)

# Commit the changes
conn.commit()

# Query the table to display names and IQs of Humans
cursor.execute('SELECT Name, IQ FROM Roster WHERE Species = "Human"')
humans_data = cursor.fetchall()

# Display the result
for name, iq in humans_data:
    print(f"Name: {name}, IQ: {iq}")

# Close the connection
conn.close()

