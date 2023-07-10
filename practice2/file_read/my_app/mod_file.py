
"""import pytest


file = 'sample2.txt'

def file_mod():
    file_name = open(file)
    line = file_name.readlines()
    file_name.close()
    return line

print(file_mod())

@pytest.fixture()
def test_filemod():
    if file == file:
        print("Collected file data")
    else:
        print("no files or directories found")

with open('sample2.txt', mode='r') as new_file:
    cont = new_file.readlines()
print(cont) """

with open('sample23.txt', mode='w') as new_file:
    rr = new_file.write("I created this file")
print(type(rr))

with open("sample23.txt", mode='r') as f:
    print(f.read())