name = input("What is you name: ")
print(f"Welcome {name} to Kon bnay ga crorepati \n")
question = [" 1.what is the capital  of pakistan?\n","2.who is the presidnet of pakistan?\n","3.when pakistan got independce?\n"]
for q in question:
    print(q)

ask = int(input("Please choose the question u wanted to answer" ))
while True:
  if ask == 1:
    print(question[0])
    answers = ["1.lahore\n","2.peshawar\n","3.islamabad"]
    for a in answers:
        print(a)
    capital = input("choose the correct answers").lower()
    if capital == "1" or capital == "lahore":
        print( f"sorry {name} the answer is incorrrect ") 
    elif capital == "2" or capital == "peshawar":
        print( f"sorry {name} the answer is incorrrect ") 
    elif capital == "3" or capital == "islamabad":
        print( f"congratualtion {name} you won 1 crore rupees")
    else:
        print("the option u choose is invalid ")             

  elif ask == 2:
    print(question[1])
    bask = ["1.nawaz\n","2.imran\n","3.asif"]
    for b in bask:
        print(b)
    pm = input("enter the name of president").lower()   
    if pm == "1" or pm == "nawaz" :
        print(f"congratulation {name} u won 1 crore rupees ") 
    elif pm == "2" or pm == "imran":
        print(f'sorry {name} u lose the game tata bye bye loser')
    elif pm == "3" or pm == "asif":
        print(f"u {name} u lose the game")
    else:
       print("the option u choose is invalid ")  


  elif ask == 3:
    print(question[2])
    cask = ["1.1947\n","2.1948\n","3.1946"]
    for c in cask:
        print(c)
    year= int(input("enter the year of independce"))
    if year == 1 or year == 1947:
        print(f"congrats {name} u won 1 crore rupees")
    elif year == 2 or year == 1948:
        print(f"u lose  the game mr.{name}")
    elif year == 3 or year == 1946:
        print(f"u lose the game mr.{name}")
    else:
       print("the option u choose is invalid ")  

  break         
else:
    print("the option u choose is invalid ")                 




#questionarie = input("what is the capital  of pakistan ,who is the presidnet of pakistan, when pakistan got independce" )
#print([question[i] for i in (0,1,2)])


 
