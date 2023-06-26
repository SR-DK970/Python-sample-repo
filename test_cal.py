"""import pytest
from calculator_01 import *
import sys

@pytest.mark.skipif(sys.version_info > (3, 7), reason="use python 3.7 or less")
def add_num():
    assert add(num1, num2) == addition

@pytest.mark.xfail(sys.platform == "linux", reason="run only on linux")
def sub_num():
    assert subtract(num1, num2) == sub
    raise Exception() """

import pytest
from calculator_func import add, subtract, multiply, divide
import sys
# Define a fixture to provide test data
@pytest.fixture(params=[(1, 2), (3, 4), (-5, -6)])
def numbers(request):
    return request.param

# Define a marker to skip some tests
@pytest.mark.skip()
def test_version():
    pass

# Define a decorator to parametrize some tests
@pytest.mark.parametrize("a,b,result", [(7, 8, 15), (9, -10, -1), (0.5, 0.5, 1)])
def test_add(a, b, result):
    assert add(a, b) == result

# Use the fixture as an argument in some tests
def test_subtract(numbers):
    a, b = numbers
    assert subtract(a, b) == a - b

def test_multiply(numbers):
    a, b = numbers
    assert multiply(a, b) == a * b

def test_divide(numbers):
    a, b = numbers
    assert divide(a, b) == a / b

# Handle zero division errors in some tests
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)