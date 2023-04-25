import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_student(conn, student):
    sql = '''
    INSERT INTO students (full_name, mark, hobby, birth_date, is_married) 
    VALUES (?, ?, ?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_students(conn):
    sql = '''SELECT * FROM students'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_students_by_mark_limit(conn, limit):
    sql = '''SELECT * FROM students WHERE mark >= ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def update_student(conn, student):
    sql = '''
    UPDATE students SET mark = ?, is_married = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_student(conn, id):
    sql = '''
    DELETE FROM students WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)



connect = create_connection('group_29.db')

sql_create_students_table = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(200) NOT NULL, 
mark DOUBLE(5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL, 
birth_date DATE NOT NULL, 
is_married BOOLEAN DEFAULT FALSE
)
'''

if connect is not None:
    print('Connected successfully')
    # create_table(connect, sql_create_students_table)
    # insert_student(connect, ('Cholpon Kaparova', 99.78, 'Programming', '2000-01-02', False))
    # insert_student(connect, ("Mark Daniels", 77.12, "Football", "1999-01-02", False))
    # insert_student(connect, ("Alex Brilliant", 77.12, None, "1989-12-31", True))
    # insert_student(connect, ("Diana Julls", 99.3, "Tennis", "2005-01-22", True))
    # insert_student(connect, ("Michael Corse", 100.0, "Diving", "2001-09-17", True))
    # insert_student(connect, ("Jack Moris", 50.2, "Fishing and cooking", "2001-07-12", True))
    # insert_student(connect, ("Viola Manilson", 41.82, None, "1991-03-01", False))
    # insert_student(connect, ("Joanna Moris", 100.0, "Painting and arts", "2004-04-13", False))
    # insert_student(connect, ("Peter Parker", 32.0, "Travelling and bloging", "2002-11-28", False))
    # insert_student(connect, ("Paula Parkerson", 77.09, None, "2001-11-28", True))
    # insert_student(connect, ("George Newel", 93.0, "Photography", "1981-01-24", True))
    # insert_student(connect, ("Miranda Alistoun", 87.55, "Playing computer games", "1997-12-22", False))
    # insert_student(connect, ("Fiona Giordano", 66.12, "Driving fast", "1977-01-15", True))

    # select_all_students(connect)
    # select_students_by_mark_limit(connect, 50)
    # update_student(connect, (57, True, 2))
    delete_student(connect, 2)
    connect.close()
