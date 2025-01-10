#Data types specify the type of data that that can be stored in a variable
# Python Data Types
# Data Types	Class	Description
# numeric	int, float, complex	Holds numeric values
v = float(6)
print(type(v))
b = complex(9j)
print(type(b))
j = 8j
print(type(j))
#converting from int to float
num = 3
numf = float(num)
print(type(num))
print(numf)
n = float(7)
print(type(n))
print(n)
# string	str	Holds sequence of characters
p = 8
print(type(p))
p_str = str(p)
print(type(p_str))
print(p_str)
print(type(p_str))
l = "I love you"
print(f"Favour, {l}")
# sequence	list, tuple ,range	Holds collection of items
#Python List Data Type
# A list is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ].
# For example,
p_languages = ["python", "Dart", "Java", "R", "Ruby", 34, 59]
p_languages.append("C++")
print(p_languages)
# Access List Items
# To access items from a list, we use the index number (0, 1, 2 ...). For example,
#accessing elements in a list
print(p_languages[0])
for item in p_languages:
    print(item)
#
# Python Tuple Data Type
# A tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
# In Python, we use the parentheses () to store items of a tuple. For example,
products = ('Laptop', 896.09, "Habibi", 23)
print(products)

# Access Tuple Items
# Similar to lists, we use the index number to access tuple items in Python. For example,
print(products[2])

# Python String Data Type
# String is a sequence of characters represented by either single or double quotes.
# For example,
school_name = "MODCOM INSTITUTE OF TECHNOLOGY"
print(school_name)
print(len(school_name))
u = "you"
print(len(u))
# mapping	dict	Holds data in key-value pair form
# Python Dictionary Data Type
# Python dictionary is an ordered collection of items.
# It stores elements in key/value pairs.
counties_airports = {"Meru": 0, "Kisii": 1, "Isiolo": 1, "Nairobi": 10}
print(counties_airports)
# boolean	bool	Holds either True or False
# set	set	Holds collection of unique items
# Python Set Data Type
# The Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }.
# For example,
student_ids = {234, 123, 564}
print(student_ids)
# print(student_ids[1])  Since sets are unordered collections, indexing has no meaning. Hence, the slicing operator [] does not work.


