"""1. Write a program to iterate the first 10 numbers and in each iteration,
print the sum of the current and previous number."""

# Create a list
new_list = [1,3,4,5,6,8,7,9,12,17,16,19,20,17,24,29,27]
print(f"Length of the list is {len(new_list)}\n")
s_list = new_list[0:10]
# Filtered list
print(f"Filtered list prints up to 10th index {s_list}\n")
list_sum = 0

# iterate s_list values and calculate sum of each objects
for i in s_list:
    list_sum = list_sum + i
    #print(f"Sum of previous number is {list_sum}")
    print(f"Sum of current number is {list_sum} and Sum of previous number is {list_sum - i}")

# Type of the list
print(type(list_sum))







