from datetime import datetime
import pytest

from Practice.custom_fixtures.myapp.demo_07 import Std


@pytest.fixture(scope="function")
def dummy_std():
    print("making dummy std")
    return Std("pavan", datetime(1999, 2, 4), "udemy")


def test_std_get_age(dummy_std):
    dummy_std_age == (datetime.now() - dummy_std.dob).days // 365
    assert dummy_std.get_age() == dummy_std_age


def test_student_add_credits(dummy_std):
    dummy_std.add_credits(5)
    assert dummy_std.get_credits() == 5


def test_student_get_credits(dummy_std):
    assert dummy_std.get_credits() == 0