import sqlite3
db = sqlite3.connect('data/python_progrmming.db')
cursor = db.cursor()

# create table structure
cursor.execute('''CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT NOT NULL, grade INTEGER NOT NULL)''')

# save
db.commit()

# Table values
cursor = db.cursor() 
id1 = 55
name1 = 'Carl Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

# insert values into table
cursor.execute('''INSERT INTO python_programming(id, name, grade) 
               VALUES(?, ?, ?)''', (id1, name1, grade1))
cursor.execute('''INSERT INTO python_programming(id, name, grade) 
               VALUES(?, ?, ?)''', (id2, name2, grade2))
cursor.execute('''INSERT INTO python_programming(id, name, grade) 
               VALUES(?, ?, ?)''', (id3, name3, grade3))
cursor.execute('''INSERT INTO python_programming(id, name, grade) 
               VALUES(?, ?, ?)''', (id4, name4, grade4))
cursor.execute('''INSERT INTO python_programming(id, name, grade) 
               VALUES(?, ?, ?)''', (id5, name5, grade5))
print('All students inserted into the database. ')

db.commit()

# grade between 60 and 80
cursor.execute('''SELECT * FROM python_programming WHERE grade >= 60 AND grade <= 80''')
for row in cursor:
    print('{0}|{1}|{2}'.format(row[0], row[1], row[2]))

# change Carl's grade to 65
new_grade = 65
carls_id = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ?''', (new_grade, carls_id))
print('Student grade for Carl Davis updated.')

# Delete Dennis row
delete_id = 66
cursor.execute('''DELETE FROM python_programming WHERE id = ?''', (delete_id,))
print('Student record for Dennis Frederickson deleted.')

# if id > 55, grade = 80
new_grade1 = 80
ids = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id > ?''', (new_grade1, ids))
print('Students with ID greater than 55 now have grade 80.')

db.commit()
db.close()