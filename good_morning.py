time = float(input("Enter time: "))

if(time < 12):
  print("good morning sir/madam : ")
elif(time > 12 and time < 16):
  print("good afternoon sir/madam : ")
elif(time > 16 and time < 20):
  print("good evening sir/madam : ")
else:
  print("good night sir/madam : ")

print("have a good time")