import sqlite3

# Connects to SQLite database (will create one if it doesn't exist)
db = sqlite3.connect("students.db")
cursor = db.cursor()

# Creates table
cursor.execute("""
CREATE TABLE IF NOT EXISTS python_programming (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
)
""")

# Data for table
students = [
    (55, "Carl Davis", 61),
    (66, "Dennis Fredrickson", 88),
    (77, "Jane Richards", 78),
    (12, "Peyton Sawyer", 45),
    (2, "Lucas Brooke", 99)
]

cursor.executemany(
    "INSERT OR IGNORE INTO python_programming (id, name, grade) "
    "VALUES (?, ?, ?)", students
)

# Select all records with a grade between 60 and 80
cursor.execute(
    "SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80"
)
print("Students with grades between 60 and 80:", cursor.fetchall())

# Change Carl Davis's grade to 65
cursor.execute(
    "UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'"
)

# Delete Dennis Fredrickson's row
cursor.execute(
    "DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'"
)

# Change the grade of all students with id greater then 55 to 80
cursor.execute(
    "UPDATE python_programming SET grade = 80 WHERE id > 55"
)

# Commits changes and closes the connection
db.commit()
db.close()

# Connect to the database
db = sqlite3.connect("students.db")
cursor = db.cursor()

# Select all records from the table
cursor.execute("SELECT * FROM python_programming")
all_records = cursor.fetchall()

# Prints all the records
print("All Students in the Table:")
for record in all_records:
    print(record)

# Closes the connection
db.close()
