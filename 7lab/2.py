import sqlite3
import os

if os.path.exists('lab7.db'):
    os.remove('lab7.db')

conn = sqlite3.connect('lab7.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    group_name TEXT,
    average_score REAL
)
""")

students_data = [
    ('Александр Глазков', '221331', 4.5),
    ('Степан Агапов', '221331', 4.8),
    ('Никита Федюнин', '220431', 4.2),
    ('ААА БББ', '123', 4.9),
    ('123 123', '222', 0),
    ('Дмитрий Морозов', '220431', 4.3)
]

cur.executemany(
    "INSERT INTO students (name, group_name, average_score) VALUES (?, ?, ?)",
    students_data
)


cur.execute("""
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    teacher TEXT,
    hours INTEGER
)
""")

subjects_data = [
    ('Базы данных', 'Скобельцын С.А.', 72),
    ('Исследование операций и методы оптимизации', 'Двоенко С.Д', 108),
    ('Методы и технологии программирования', 'Цымлов А.В.', 90)
]

cur.executemany(
    "INSERT INTO subjects (name, teacher, hours) VALUES (?, ?, ?)",
    subjects_data
)

conn.commit()
print(f" Вставлено {len(students_data)} студентов и {len(subjects_data)} предметов")

group_name = '221331'
cur.execute(
    "SELECT name,average_score FROM students WHERE group_name = ? ORDER BY average_score DESC",
    (group_name,)
)

print(f" Студенты группы {group_name}:")
for name, score in cur.fetchall():
    print(f"  {name}: {score}")

min_score = 4.5
cur.execute(
    "SELECT name, group_name FROM students WHERE average_score >= ?",
    (min_score,)
)

print(f"\n Отличники (средний балл >= {min_score}):")
for name, group in cur.fetchall():
    print(f"  {name} ({group})")

cur.execute("""
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
)
""")


grades_data = [
    (1, 1, 5),  
    (1, 2, 4),  
    (2, 1, 5),  
    (2, 3, 5),  
    (3, 2, 3),  
    (4, 1, 5),  
    (6, 3, 4)   
]

cur.executemany(
    "INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
    grades_data
)

conn.commit()
print("1. INNER JOIN - студенты с их оценками:")
cur.execute("""
SELECT s.name, sub.name, g.grade
FROM students s
INNER JOIN grades g ON s.id = g.student_id
INNER JOIN subjects sub ON g.subject_id = sub.id
WHERE g.grade >= 4
ORDER BY s.name
""")

for name, subject, grade in cur.fetchall():
    print(f"  {name}: {subject} - {grade}")

print("\n2. LEFT JOIN - все студенты с оценками (если есть):")
cur.execute("""
SELECT s.name, s.group_name, 
       COALESCE(sub.name, 'нет предмета') as subject,
       COALESCE(g.grade, 0) as grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
LEFT JOIN subjects sub ON g.subject_id = sub.id
ORDER BY s.group_name, s.name
""")

for name, group, subject, grade in cur.fetchall():
    if grade > 0:
        print(f"  {name} ({group}): {subject} - {grade}")
    else:
        print(f"  {name} ({group}): нет оценок")

print("\n ОБЗОР БАЗЫ ДАННЫХ:")
cur.execute("SELECT COUNT(*) FROM students")
print(f"Студентов: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM subjects")
print(f"Предметов: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM grades")
print(f"Оценок: {cur.fetchone()[0]}")

cur.close()
conn.close()

print(" База данных сохранена в файле: lab7.db")
