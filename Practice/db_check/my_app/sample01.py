import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='demodb1',
                                         user='root',
                                         password='Raja$1234567')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# test.py
import unittest
import pytest
import pymysql

@pytest.fixture(scope="class")
def db_class():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Raja$1234567',
                                 database='demodb1')
    """yield connection
    # Close the connection
    connection.close()"""

@pytest.fixture(autouse=True)
def _mock_db_connection(mocker, db_class):
    mocker.patch('MySQL.pymysql.connect', return_value=db_class)

class TestMySQL(unittest.TestCase):

    def test_link(self):
        # Create a new record
        sql = "INSERT INTO `users` (`dk652071@outlook.com`, `deep@1234`) VALUES (%s, %s)"
        cursor.execute(sql, ('dk652071@outlook.com', 'deep@1234'))
        # Commit the changes
        connection.commit()
        # Check if the record was inserted
        sql = "SELECT * FROM `users` WHERE `email` = %s"
        cursor.execute(sql, ('dk652071@outlook.com',))
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['email'], 'dk652071@outlook.com')
        self.assertEqual(result['password'], 'deep@1234')

