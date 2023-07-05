
import pytest
import mysql.connector
from mysql.connector import Error
from pytest import ExitCode

try:
    def connection_check():
        db_connection = mysql.connector.connect(host='localhost',
                                             database='demodb1',
                                             user='root',
                                             password='Raja$1234567')
        if db_connection.is_connected():
            db_Info = db_connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = db_connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

# Use the fixture as an argument in the test function
@pytest.fixture()
def test_db_query(db_connection):
    # Perform some query using the connection
    result = db_connection.query("SHOW DATABASES;")
    # Assert some expectation
    assert result != "something"

# Example of a parametrized fixture
"""import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    # Return the current parameter value
    return request.param

# Use the fixture as an argument in the test function
def test_number(number):
    # Assert some expectation based on the number
    assert number > 0

# Example of parametrizing a test function
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54)
])
def test_eval(test_input, expected):
    # Evaluate the test input as an expression
    assert eval(test_input) == expected

# Example of indirect parametrization
import pytest

class TimeLine:
    def __init__(self, instances):
        self.instances = instances

@pytest.fixture
def timeline(request):
    # Create a TimeLine object with the parameter value
    return TimeLine(request.param)

@pytest.mark.parametrize(
    "timeline",
    ([1, 2, 3], [2, 4, 6], [6, 8, 10]),
    indirect=True
)
def test_timeline(timeline):
    # Assert some expectation based on the timeline instances
    for instance in timeline.instances:
        assert instance % 2 == 0 """
