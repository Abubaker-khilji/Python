# # strings are immutable
# a = "khilji bkr teodora"
# print(len(a))
# print(a.upper())
# print(a.lower())

# b = "khilji!!!!!"
# print(b.rstrip("!"))
# print(b.replace("khilji", "abuabker"))
# print(a.split(" "))

# blogheading = "introduction to python"	
# print(blogheading.capitalize())

# # it capitalize only first character of String

# str1 = "Welcome to the Console!!!"
# print(len(str1))
# print(len(str1.center(50)))
# print(a.count("khilji"))

# name = "abubaker"
# name.capitalize()
# print(name[1:-1])
# print(name.startswith("AB"))
# print(name.endswith("ker"))






# Python3 code to demonstrate
# how to remove 'n' characters from starting
# of a string
 
# Initialising string
ini_string1 = 'gargakshat123'
 
# Initialising number of characters to be removed
n = 5
 
# Printing initial string
print("Initial String", ini_string1)
 
# Removing n characters from a string
# This argument count length from zero
# So length to be stripped is passed n-1
res = ini_string1[4:]
 
# Printing resultant string
print("Resultant String", res)
