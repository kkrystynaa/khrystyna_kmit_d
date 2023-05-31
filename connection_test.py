import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="admin",
  password="Qwerty123!@",
  database="courses"
)
# Create a cursor object

cursorObject = mydb.cursor()

# SQL query string

sqlQuery = "SELECT * FROM courses.group;"

# Execute the sqlQuery

cursorObject.execute(sqlQuery)

# Fetch all the rows

rows = cursorObject.fetchall()
print(rows)
# print(mydb.query("SELECT * FROM users;"))