import sqlite3
import re
import datetime
def main():
    connection = sqlite3.connect('myTable.db')
    c = connection.cursor()
    c.execute('SELECT id FROM emp ORDER BY id DESC LIMIT 1')
    results = c.fetchall()
    connection.commit()
    connection.close()
    results = re.findall(r'\d+',str(results))
    for i in results:
        results = int(i)
    id = results + 1
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    fname = str(input("What is your first name : "))
    lname = str(input("What is your last name : "))
    gender = str(input("What is your gender (M/F) : "))
    x = datetime.datetime.now()
    date = str(x.day) + '/' + str(x.month) + '/' + str(x.year)
    params = (id,fname, lname, gender, date)
    crsr.execute('INSERT INTO emp VALUES (?, ?, ?, ?, ?)',params)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
