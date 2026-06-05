import mysql.connector

# Database Connection
conn = mysql.connector.connect(
host="localhost",
user="root",
password="P@ssw0rd",
database="company_db"
)

cursor = conn.cursor()

# SELECT Query
cursor.execute("SELECT * FROM Employee")

print("Employee Records")

for row in cursor.fetchall():
    print(row)

# WHERE Query
cursor.execute("SELECT * FROM Employee WHERE salary > 50000")

print("\nEmployees Salary > 50000")

for row in cursor.fetchall():
    print(row)

# JOIN Query
query = """
SELECT e.emp_name,d.dept_name
FROM Employee e
JOIN Department d
ON e.dept_id=d.dept_id
"""

cursor.execute(query)

print("\nEmployee Department Details")

for row in cursor.fetchall():
    print(row)

# ORDER BY Query
cursor.execute(
"SELECT * FROM Employee ORDER BY salary DESC"
)

print("\nSorted Records")

for row in cursor.fetchall():
    print(row)

conn.close()
