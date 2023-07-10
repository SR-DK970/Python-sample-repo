
"""3. Write all content of a given file into a new file by skipping line number 5. """

with open("sample01.txt", mode='r') as testfile:
    rr = testfile.readlines()
    print(rr.pop(4))

x = open('sample01.txt', mode='w')
print(x)

