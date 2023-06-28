import sys

import pytest

from Practice.Markers.myapp.demo_04 import add


@pytest.mark.skip("skip test practice")
def test_1():
    assert add(2, 7) == 9


@pytest.mark.skipif(sys.version_info > (3, 7), reason="version check didn't meet")
def test_str():
    assert add("hello ", "world") == "hello world"


@pytest.mark.xfail(sys.platform == "win32", reason="Don't run on win32")
def test_list():
    assert add([2], [7]) == [2, 7]
    raise Exception()