"""2. Write a program to accept a string from the user and display characters
that are present at an even index number."""

while True:
    # ask for user input by default input methods takes string data type
    user_input = input("Please enter names of your friends\n")
    print(f"Hii {user_input}, how are you doing")

    # ignore below liness
    """print(f"Skip 1 char from user input \n{user_input[::2]}")
    for letter in user_input: #if user_input == type(str()):
        print(letter) """

# Method 1
    # Create an empty list
    mylist = []

    # iterate user input and append to list from there print out by skipping 2nd char
    for letter in user_input:
        mylist.append(letter)
    print(f"Printing out results from method 1 {mylist[::2]}")

#Method 2

    mylist = [letter for letter in user_input]
    print(f"Printing out results from method 2 {mylist[::2]}")











    """elif user_input == int():
        print("Entered invalid data type")
    else:
        print("Not a valid input")"""