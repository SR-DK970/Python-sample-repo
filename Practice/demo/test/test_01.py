from Practice.demo.demo_02 import add

def test_1():
    assert add(2, 7) == 9

def test_str():
    assert add("hello ", "world") == "hello world"

class Test_cls():
    def test_1(self):
        assert add(2, 7) == 9

    def test_str(self):
        assert add("hello ", "world") == "hello world"