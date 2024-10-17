# strings are immutable
a = "khilji bkr teodora"
print(len(a))
print(a.upper())
print(a.lower())

b = "khilji!!!!!"
print(b.rstrip("!"))
print(b.replace("khilji", "abuabker"))
print(a.split(" "))

blogheading = "introduction to python"	
print(blogheading.capitalize())

# it capitalize only first character of String

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("khilji"))

name = "abubaker"
name.capitalize()
print(name[1:-1])
print(name.startswith("AB"))
print(name.endswith("ker"))
