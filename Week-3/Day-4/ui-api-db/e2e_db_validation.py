import requests
import mysql.connector
# -----------------------
# DB Connection
# -----------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="company_db"
)

cursor = conn.cursor()

# Insert data into DB
sql = """
INSERT INTO employees(name, position, salary)
VALUES (%s, %s, %s)
"""

employee_id = 1

cursor.execute(sql, (name, job, salary))

conn.commit()

print("Data inserted into MySQL")

# -----------------------
# Validation
# -----------------------
cursor.execute(
    "SELECT * FROM employees WHERE id = %s",
    (employee_id,)
)

record = cursor.fetchone()

print("DB Record:", record)

cursor.close()
conn.close()