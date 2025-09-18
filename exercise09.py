# Exercise 9: Basic Calculator
#
# Create a function named `basic_calculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basic_calculator(10, 5, 'subtract') should return 5.
# basic_calculator(10, 5, 'add') should return 15.
# basic_calculator(10, 5, 'multiply') should return 50.
# basic_calculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.



def basic_calculator(a, b, oper):
    if oper == "subtract":
        return(a - b)
    if oper == "add":
        return(a + b)
    if oper == "multiply":
        return(a * b)
    if oper == "divide":
        return(a / b)
    
print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
print(basic_calculator(10, 5, "add"))
print(basic_calculator(10, 5, "multiply"))
print(basic_calculator(10, 5, "divide"))
