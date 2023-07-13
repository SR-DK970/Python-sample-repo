"""Task-
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
A recursive function is a function that calls itself again and again."""


# Initial value of N
N = int(input("Enter an integer: "))


# Recursive function
def calculate_sum(N):
    # Base condition
    # When this condition is met,
    # the recursion terminates
    if (N == 0):
        return

    # Pr the current value of N
    #print(N, end=" ")
    sum_of_numbers = 0
    for num in range(N + 1):
        sum_of_numbers += num
    print(f"The sum of the given numbers is: {sum_of_numbers}")

    # Call itself recursively
    calculate_sum(N - 1)


# Call the recursive function
calculate_sum(N)











"""def calculate_sum():
    sum_of_num = 0
    print("Sum of the numbers is zero")
    # Ask for user input
    user_input = int(input("Enter a number that you want to find the sum: "))
    try:
        for ele in range(user_input + 1):
            print(ele)
            sum_of_num += ele
        # Print the sum of the numbers
        print(f"The sum of the given number: {sum_of_num}")
        calculate_sum()
    except RecursionError:
        print("Maximum recursion depth 1000 is exceeded while calling a Python object")


calculate_sum() """



"""def demo(x):
    if x == 1:
        return 1
        print("Hello")
    else:
        val = 0
        val += demo(x)
        return val
        print("x value is more than 1")
    demo(x)

demo(10) """