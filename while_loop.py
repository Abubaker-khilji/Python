#table = int(input("enter a number:  "))
#i = 1
#while(table <= 10):
 #   print(table ," X " , i + 1 ,"=", table * 1)
#i += 1   



table = int(input("Enter a number: "))

i = 1  # Start from 1
while i <= 10:  # Loop until 10 for the multiplication table
    print(table, " X ", i, "=", table * i)
    i += 1  # Increment i to avoid infinite loop

