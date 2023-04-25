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


def add_random_products(conn: Connection):
    insert_product(conn, ('банан', 24.3, 5,))
    insert_product(conn, ('картошка', 77.7, 18,))
    insert_product(conn, ('хлеб', 24.3, 34,))
    insert_product(conn, ('яблоко', 1000.3, 56,))
    insert_product(conn, ('гречка', 24.3, 31,))
    insert_product(conn, ('фасоль', 94.3, 1,))
    insert_product(conn, ('творог', 80.3, 4,))
    insert_product(conn, ('жвачка', 27, 65,))
    insert_product(conn, ('вишня', 2.4, 35,))
    insert_product(conn, ('апельсин', 24.3, 335,))
    insert_product(conn, ('редиска', 240.3, 94,))
    insert_product(conn, ('лук', 24.3, 9,))
    insert_product(conn, ('чесное', 2.3, 3,))
    insert_product(conn, ('утюг', 54.9, 5,))
    insert_product(conn, ('хлеб', 24.3, 6,))


def insert_product(conn: Connection, product: tuple):
    sql_query = '''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, product)
        conn.commit()
    except Error as e:
        print(e)


def update_product_quantity(conn: Connection, quantity_id):
    sql_query = '''
    UPDATE products 
    SET quantity = ?
    WHERE id = ?
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, quantity_id)
        conn.commit()
    except Error as e:
        print(e)


def update_product_price(conn: Connection, price_id):
    sql_query = '''
    UPDATE products 
    SET price = ?
    WHERE id = ?
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, price_id)
        conn.commit()
    except Error as e:
        print(e)


def delete_product(conn: Connection, id: tuple):
    sql_query = '''
    DELETE FROM products
    WHERE ID = ?
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, id)
        conn.commit()
    except Error as e:
        print(e)


def print_all_products(conn: Connection):
    sql_query = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()

        print('Все товары:', end='\n\n')
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def find_cheapest_products(conn: Connection):
    sql_query = '''
    SELECT * FROM products
    WHERE price < 100 and quantity > 5
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()

        print(
            'Товары, которые дешевле 100 сомов и количество которых больше 5:', end='\n\n')
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def find_product(conn: Connection, name: tuple):
    if not name or len(name) > 1:
        return

    name = name[0].lower(),
    sql_query = r'''
    SELECT * FROM products
    WHERE product_title LIKE '%' || ? || '%'
    '''

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query, name)
        rows = cursor.fetchall()

        print(
            f'Товары, в названии которых есть подстрока "{name[0]}"', end='\n\n')
        for row in rows:
            print(row)
    except Error as e:
        print(e)


connection = create_connection(
    r'/Users/larginator/learning_python/geeks/week_9/hw7/hw.db')

create_table_sql = '''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
);'''

if connection is not None:
    create_table(connection, create_table_sql)
    add_random_products(connection)
    update_product_quantity(connection, (17, 1))
    update_product_price(connection, (100.0, 2))
    delete_product(connection, (12,))
    print_all_products(connection)
    find_cheapest_products(connection)
    find_product(connection, ('ка',))
    connection.close()
