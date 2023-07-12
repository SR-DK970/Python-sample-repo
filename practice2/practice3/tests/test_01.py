import pytest
from practice3.my_app.demo_01 import find_highest_element, find_length_of_list, my_list





@pytest.fixture(params=[1000,977])
def add_elements_to_list(request):
    my_list.append(request.param)
    print(my_list)
    return request.param


def test_modified_list(add_elements_to_list):
    length = find_length_of_list()
    assert length != 8, "Length of the list is not equal to 8"


def test_current_highest_ele(add_elements_to_list):
    current_highest_ele = find_highest_element()
    assert current_highest_ele == 1000, f"Then find current highest element from the list"


# Write a test function to verify highest number in list
@pytest.mark.skip(reason="I am skipping this test01")
def test_highest_element():
    max_element = find_highest_element()
    assert max_element == 799


# Write a test function to check length of the list
@pytest.mark.xfail
def test_length_of_list():
    list_lenth = find_length_of_list()
    assert list_lenth == 8


