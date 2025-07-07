import  sqlite3
import os
import datetime

if os.path.exists('students.db'):
    os.remove('students.db')

conn = sqlite3.connect('students.db')

conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENTS(
  ID INTEGER PRIMARY KEY,
  NAME TEXT NOT NULL,
  GRADE INTEGER NOT NULL,
  BIRTHYEAR INTEGER);
''')

data = [
  (1, 'Noa', 85, 2010),
  (2, 'Lior', 90, 2011),
  (3, 'Dana', 78, 2009)
]

cursor.executemany('''
INSERT INTO STUDENTS (ID,NAME,GRADE,BIRTHYEAR)
VALUES (?,?,?,?);''',data)

#ANSWER 5:  Update grade to Dana
cursor.execute('''UPDATE students set GRADE = ? WHERE ID = ?;''',(88, 3))  #update grade to Dana

#ANSWER 6:  Deleting student with ID =2
cursor.execute('''DELETE from students WHERE ID = ?;''',(2,))

#Ans 7:  print all stidents with "fetchall"
cursor.execute('''SELECT * from students;''')
result = cursor.fetchall()
for row in result:
    print(dict(row))

#Ans 8:

while True:
    try:
        new_id = int(input("Enter ID: "))
        new_name = input("Enter name: ")
        new_grade = int(input("Enter grade: "))
        while new_grade not in range(0,100):
            print("Grade can not be greater 100 or less than 0.\n Try again.")
            new_grade = int(input("Enter grade: "))
        new_birth_year = int(input("Enter birth year: "))
        current_year = datetime.datetime.now().year
        while new_birth_year not in range(current_year - 100,current_year):
            print(f"Enter birth year between: {current_year - 100} and {current_year - 5}")
            new_birth_year = int(input("Enter birth year:"))

        cursor.execute('''
        INSERT into students (ID,NAME,AGE,BIRTHYEAR)
        VALUES (?,?,?,?);
        ''',(new_id,new_name,new_grade,new_birth_year))
        break

    except ValueError:
        print("Type only number")
    except:
        print("Try again")

cursor.execute('SELECT * FROM students WHERE ID = ?;', (new_id,))
result = cursor.fetchone()
print(dict(result))



conn.commit()
conn.close()
