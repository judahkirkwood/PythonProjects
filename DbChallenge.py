import sqlite3

# File list 
fileList = ('information.docx', 'Hello.txt', 'information.docx', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Searching through files with .txt format
txtFiles = [file for file in fileList if file.endswith('.txt')]

# Connecting to database
conn = sqlite3.connect('fileRecords.db')

# Using a cursor to interact with the database
with conn:
    cur = conn.cursor()
    # Creating the table if it doesn't exist
    cur.execute("CREATE TABLE IF NOT EXISTS Files (ID INTEGER PRIMARY KEY AUTOINCREMENT, FileName TEXT)")

    # Putting the files into the database
    for file in txtFiles:
        cur.execute("INSERT INTO Files (FileName) VALUES (?)", (file,))

    # Selecting text files from database and printing to console
    cur.execute("SELECT FileName FROM Files")
    txtFiles_from_db = cur.fetchall()
    print("Qualifying text files:")
    for file in txtFiles_from_db:
        print(file[0])

# Closing connection to the database
conn.close()
