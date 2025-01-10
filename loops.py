# Python Loops
#
# In computer programming, loops are used to repeat a block of code. We perform a process of iteration (repeating tasks).
#
#
#
# There are 2 types of loops in Python:
#
# for loop
# while loop
#
# Programming languages like Python implement two types of iteration:
#
# Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.
# Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).
#
# In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length.
#
#
#
# With for loops, on each iteration, we will be able to perform an action on each element of the collection.
#For loop syntax
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

my_tuple = ("apple", "banana", "orange")
for item in my_tuple:
    print(item)

# Example of a for loop with range
for num in range(10,21):
    print(num)

#While loop
count = 1

while count <= 10:
    print(count)
    count += 1
b = 20
while b <= 30:
    print(b)
    b += 1

r = 20
while r >= 10:
    print(r)
    r = r - 1


# Loop controls: Break and Continue
# The break statement is used to terminate the loop immediately when it is encountered.
# The continue statement skips the rest of the code in the loop for the current iteration.

for number in range(1, 11):
    if number == 5:
        break  # Exit the loop entirely when number is 5
    elif number % 2 == 0:
        continue  # Skip even numbers and move to the next iteration
    print(number)  # Only odd numbers less than 5 will be printed


# Python continue Statement
#
# The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.
#
# While the break control statement will come in handy, there are other situations where we don’t want to end the loop entirely. What if we only want to skip the current iteration of the loop?
#
#
#
# Nested Loops
#
# In Python, loops can be nested inside other loops. Nested loops can be used to access items of lists which are inside other lists. The item selected from the outer loop can be used as the list for the inner loop to iterate over.
#
# Example code
# Example of a nested loop
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")