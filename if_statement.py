#Conditional statements help in decision making
# In Python, there are three forms of the if...else statement.

# if statement
# # if...else statement
# # if...elif...else statement

# 1. Python if Statement
# The basic syntax for the if statement:
temp = 38
if temp > 25:
    print("It is a hot day")
#Example 2
time = 10
if time > 8:
    print("It's late")



# 2. Python if...else Statement
# Syntax
age = 18
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")

# 3. Python if...elif...else Statement
# The if...else statement is used to execute a block of code among two alternatives.
# However, if we need to make a choice between more than two alternatives, then we use the if...elif...else statement.
#The syntax of the if...elif...else statement is:
age1 = 18
if age1 > 18:
    print("Adult in Kenya")
elif age1 > 16:
    print("Adult in US")
else:
    print("Not Adult in both countries")
    


