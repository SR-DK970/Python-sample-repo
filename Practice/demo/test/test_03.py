import pytest

from Practice.demo.demo_03 import validate_age

def test_validate_valid():
    validate_age(0)


"""def test_validate_invalid():
    with pytest.raises(ValueError) as exec_info_file:
        validate_age(-11)
    assert str(exec_info_file.value) == "Age cannot be less than 0" """


def test_validate_invalid():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-22)
