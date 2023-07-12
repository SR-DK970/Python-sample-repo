"""Create a function that finds the maximum element in a given list,
and write pytest cases to test the function's correctness."""

# Define a list
my_list = [12,45,78,96,56,48,29,799]


# Find max number in the list
def find_highest_element():
    highest_ele = max(my_list)
    print(f"The highest number in the list is: {highest_ele}")
    return highest_ele


# Find length of the list
def find_length_of_list():
    length_of_list = len(my_list)
    print(f"Length of the list is: {length_of_list}")
    return length_of_list


#find_highest_element()
#find_length_of_list()

