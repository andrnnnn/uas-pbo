import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='pboperpus',
  port='8111'
)

if mydb.is_connected():
  print("berhasil")
else:
  print("gagal")