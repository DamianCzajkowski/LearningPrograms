import unittest
from sqlite3 import connect
from customers.customers import CustomersDB


class TestCustomersDB(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_add_customer(self):
        # Given
        customer_db = CustomersDB(self.connection)
        expected = (
            ('Adam', 'Smith', 'Adam.smith@mail.com', '222', 'RPA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        cursor = self.connection.cursor()

        # When
        customer_db.add_customer('Adam', 'Smith', 'Adam.smith@mail.com', '222', 'RPA')
        cursor.execute("""SELECT * FROM CUSTOMERS ORDER BY FIRST_NAME, LAST_NAME;""")

        # Then
        self.assertEqual(tuple(cursor), expected)

    def test_find_customers_by_first_name(self):
        # Given
        customer_db = CustomersDB(self.connection)
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
        )

        # When
        actual = tuple(customer_db.find_customers_by_first_name('John'))

        # Then
        self.assertEqual(actual, expected)

    def test_find_customers_by_country(self):
        # Given
        customer_db = CustomersDB(self.connection)
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )

        # When
        actual = tuple(customer_db.find_customers_by_country('USA'))

        # Then
        self.assertEqual(actual, expected)
