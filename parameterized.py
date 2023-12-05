import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    C = connection.cursor()
    C.execute("DROP TABLE IF EXISTS People")
    C.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    C.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)



    C.execute("SELECT FirstName, LastName FROM people WHERE Age > 30")
    while True:
        row = C.fetchone()
        if row is None:
            break
        print(row)
