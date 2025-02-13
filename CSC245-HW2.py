import random
from math import factorial

# Exercise 1
print("Hello World!\n")

# Exercise 2
print(f'5 + 10 = {5 + 10}')
print(f'20 - 7 = {20 - 7}')
print(f'3 * 8 = {3 * 8}')
print(f'25 / 5 = {25 / 5}')

# Exercise 3
age = 20
print(f'\nI am {age} years old.')

# Exercise 4
celsius = int(input("\nEnter temperature in celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f'The temperature in Fahrenheit is: {fahrenheit}')

# Exercise 5
number = int(input('\nEnter a number: '))
if number % 2 == 0:
    print(f'{number} is even.')
else:
    print(f'{number} is odd.')

# Exercise 6
number = int(input('\nEnter a number: '))
if number > 0:
    print("The number is positive.\n")
elif number < 0:
    print("The number is negative.\n")
else:
    print("The number is zero.\n")

# Exercise 7
numbers = [2, 4, 6, 8, 10]
numbers.remove(2)
numbers.append(12)
print(f'This list contains {len(numbers)} elements.')
numbers.sort()
print(f"Sorted list: {numbers}")

# Exercise 8
n = int(input("\nEnter a number: "))
print(f'The factorial of {n} is {factorial(n)}')

# Exercise 9
n = int(input("\nEnter a number: "))
for i in range(1, 11):
    print(f'{n} * {i} = {n * i}')

# Exercise 10
numbers: list[int] = [2, 4, 6, 8, 10]
total = 0
for i in numbers:
    total += i
print(f'\nThe sum of numbers is: {total}')

# Exercise 11
print("\nI'm thinking of a number between 1 and 20. Try to guess it!")
number = random.randint(1, 20)
guess = int(input("Your guess: "))

while guess != number:

    if guess < number:
        print("Too low. Try again.")
    elif guess > number:
        print("Too high. Try again.")
    guess = int(input("Your guess: "))

print(f"Correct! The number was {number}!")

# Exercise 12
string = str(input("Enter a string: "))
count = 0
for char in string:
    if char.lower() in 'aeiou':
        count += 1
print(f'Number of vowels: {count}\n')

# Exercise 13
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 14
string = input("Enter a string: ")
reverse = string[::-1]
print(f'Reversed string: {reverse}')


