import json
import os

from Practice.pytest_fixtures.myapp.demo_06 import save_dict

def test_dir_save(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test.json")
    _dic = {"a": 12, "b": 24}

    save_dict(_dic, filepath)
    assert json.load(open(filepath, 'r')) == _dic
    assert capsys.readouterr().out == "saved\n"





















"""def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test.json")
    _dict = {"a": 1, "b": 2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "saved\n" """