number = int(input("Enter a number: "))
number1 = int(input("Enter a number: "))

ans = number + number1

if(ans == 0 ):
    print("number is neutral")
    if(ans > 100):
       print("number is positive")
    elif(ans < 0):
       print("number is negative")
    else:
        print("please enter a number")
    
else:
    print("apun  abhi kya bolay ga")

print("thank you")