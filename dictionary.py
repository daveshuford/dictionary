'''
Dictionary application running off remote mysql server.
'''
from database import dictionary
from spelling import checker
import mysql.connector


word = input('Enter a Word: ')


connect = mysql.connector.connect(**dictionary)

data = checker(word)

cursor = connect.cursor()

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % data)
result = cursor.fetchall()

connect.close()

if result: # Creates a True conditional
    for word in result:
        print(data+':')
        print("     ", word[1])




