# Get user input as integers
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# Addition
addition = num1 + num2
print('Addition:', num1, '+', num2, '=', addition)

# Subtraction
subtraction = num1 - num2
print('Subtraction:', num1, '-', num2, '=', subtraction)

# Multiplication
multiplication = num1 * num2
print('Multiplication:', num1, '*', num2, '=', multiplication)

# Division
if num2 != 0:
    division = num1 / num2
else:
    division = 'Undefined (cannot divide by zero)'

print('Division:', num1, '/', num2, '=', division)
