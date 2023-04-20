#!C:\Users\Anisha B Sangolli\anaconda3

print("Content-type:text/html; charset=utf-0\n\n")

import cgitb,cgi
import MySqldb

cgitb.enable()

form.cgi.FieldStorage()
email = form.getvalue("email")

connection = MySqldb.connect('localhost','root','','ecomerce')

cursor = connection.cursor()
cursor.execute("insert into subscribe values('%s')"%(email))
print("Subscribed")
connection.commit()
connection.close()

# database name: ecomerce
# table name: subscribe
# column name: email