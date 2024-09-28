import time as timestamp
name = input("Enter your name: ")
time = int(input("Enter your time: "))

# Or, use strftime to get the hour:
hour = int(time.strftime('%H'))
timestamp = hour


if(time < 9 and hour < 9):
  print("Good Morning", name)
else:
  print(name, "you are late")