import random
from sqlite3 import Connection, Error, connect


def create_connection(db_file: str):
    connection = None

    try:
        connection = connect(db_file)
    except Error as e:
        print(e)

    return connection


def create_table(conn: Connection, create_table_sql: str):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_country(conn: Connection, country: tuple):
    sql_query = '''
        INSERT INTO countries (title)
        VALUES (?)
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, country)
        conn.commit()
    except Error as e:
        print(e)


def add_random_countries(conn: Connection):
    insert_country(conn, ('USA',))
    insert_country(conn, ('China',))
    insert_country(conn, ('France',))


def insert_city(conn: Connection, city: tuple):
    sql_query = '''
        INSERT INTO cities (title, area, country_id)
        VALUES (?, ?, ?)
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, city)
        conn.commit()
    except Error as e:
        print(e)


def add_random_cities(conn: Connection):
    insert_city(conn, ('Moscow', 22.09, 1))
    insert_city(conn, ('Tokyo', 300.34, 2))
    insert_city(conn, ('Бишкек', 203.6, 3))
    insert_city(conn, ('Ош', 21.96, 2))
    insert_city(conn, ('Берлин', 3.43, 1))
    insert_city(conn, ('Пекин', 22.14, 2))
    insert_city(conn, ('Нью-Йорк', 43.3, 3))


def insert_employee(conn: Connection, employee: tuple):
    sql_query = '''
        INSERT INTO employees (first_name, last_name, city_id)
        VALUES (?, ?, ?)
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, employee)
        conn.commit()
    except Error as e:
        print(e)


def add_random_employees(conn: Connection):
    cities_id = [i for i in range(1, 8)]

    insert_employee(conn, ('Вася', 'Пупкин', random.choice(cities_id)))
    insert_employee(conn, ('Жорик', 'Варламов', random.choice(cities_id)))
    insert_employee(conn, ('Ксения', 'Собчак', random.choice(cities_id)))
    insert_employee(conn, ('Игорь', 'Шпак', random.choice(cities_id)))
    insert_employee(conn, ('Боб', 'Большой', random.choice(cities_id)))
    insert_employee(conn, ('Игорь', 'Синь', random.choice(cities_id)))
    insert_employee(conn, ('Валерий', 'Младзи', random.choice(cities_id)))
    insert_employee(conn, ('Ви', 'Джелинк', random.choice(cities_id)))
    insert_employee(conn, ('Дима', 'Гордый', random.choice(cities_id)))
    insert_employee(conn, ('Копи', 'Паст', random.choice(cities_id)))
    insert_employee(conn, ('Цзынь', 'Кусь', random.choice(cities_id)))
    insert_employee(conn, ('Кира', 'Найтли', random.choice(cities_id)))
    insert_employee(conn, ('Анджелина', 'Джоли', random.choice(cities_id)))
    insert_employee(conn, ('Олег', 'Нью-Йорк', random.choice(cities_id)))
    insert_employee(conn, ('Валерия', 'Черных', random.choice(cities_id)))


def select_cities_title(conn: Connection):
    result = None
    sql_query = 'select title, id from cities'

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
    except Error as e:
        print(e)

    return result


def find_employees(conn: Connection, city_id: tuple):
    result = None
    sql_query = '''
        SELECT employees.first_name AS test1,
               employees.last_name AS test2,
               countries.title AS country,
               cities.title AS city
        FROM countries
        LEFT JOIN cities 
            ON countries.id=cities.country_id
        LEFT JOIN employees 
            ON employees.city_id=cities.id
        WHERE employees.city_id=?
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, city_id)
        result = cursor.fetchall()
    except Error as e:
        print(e)

    return result


connection = create_connection('hw.db')

create_countries_table_sql = '''
    CREATE TABLE IF NOT EXISTS countries (
    id    INTEGER     PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(30) NOT NULL
);'''

create_cities_table_sql = '''
    CREATE TABLE IF NOT EXISTS cities (
    id         INTEGER      PRIMARY KEY AUTOINCREMENT,
    title      VARCHAR(30)  NOT NULL,
    area       DOUBLE(5, 2) DEFAULT 0.0,
    country_id INTEGER,
    FOREIGN KEY(country_id)
        REFERENCES countries (id)
);'''

create_employees_table_sql = '''
    CREATE TABLE IF NOT EXISTS employees (
    id         INTEGER     PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name  VARCHAR(30) NOT NULL,
    city_id    INTEGER,
    FOREIGN KEY(city_id)
        REFERENCES cities (id)
);'''

if connection is not None:
    create_table(connection, create_countries_table_sql)
    create_table(connection, create_cities_table_sql)
    create_table(connection, create_employees_table_sql)
    add_random_countries(connection)
    add_random_cities(connection)
    add_random_employees(connection)

    while True:
        print('\nВы можете отобразить список сотрудников по выбранному id'
              'города из перечня городов ниже, для выхода из программы введите 0:')

        cities = select_cities_title(connection)
        if cities is not None:
            for city, id in cities:
                print(city, id, sep=' - ')

        employee_id = input('\nВведите id города: ')
        print()
        if employee_id == '0':
            break

        employees = find_employees(connection, (employee_id,))
        if employees is not None:
            for second_name, first_name, country, city in employees:
                print(second_name, first_name, country, city, sep=' | ')