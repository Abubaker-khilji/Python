#file = open('help.txt' , 'r')
#print(file)
#text = file.read()
#print(text)
#file.close
""" 
file = open("help.txt" , "a")
file.write("helloooooooooooooooooooooooooooooooooooo worldddddddddddddddddd")
file = open('help.txt' , 'r')
print(file)
text = file.read()
print(text)
file.close
 """
#with open('help.txt', 'a') as file:
 # file.write("Hey I am inside with")


with open('help.txt' , 'w') as file:
  print(type(file))
  file.seek(10)
  #print(file.tell())
  #data = file.read(5)
 # print(data)
  file.truncate(3)

with open("help.txt" , "r") as file:
  print(file.read())

