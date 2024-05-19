import sqlite3

connection=sqlite3.connect('students.db')

#create a cursor
cursor=connection.cursor()

# create a table
table_info="""CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)"""

cursor.execute(table_info)

#insert more records
cursor.execute("INSERT INTO STUDENT VALUES('Raj','10','A',90)")
cursor.execute("INSERT INTO STUDENT VALUES('Rahul','10','B',80)")
cursor.execute("INSERT INTO STUDENT VALUES('Ravi','10','C',70)")
cursor.execute("INSERT INTO STUDENT VALUES('Rajesh','10','D',60)")
cursor.execute("INSERT INTO STUDENT VALUES('Rakesh','10','E',50)")

# Display the records
print("The inserted records are:")

data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)
    
# Close the connection
connection.commit()   