# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.

def sum_to(n):
    n_array = list(range(1, n + 1))
    total_sum = sum(n_array)
    return total_sum

print('Exercise 5:', sum_to(6))
print(sum_to(10))
