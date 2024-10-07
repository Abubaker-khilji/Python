secret = 9
guess_count=0
guess_limit = 3
while guess_count<guess_limit:
    guess = int(input("Enter the number: "))
    guess_count = guess_count+1
    if guess==secret:
        print("you win")
        break    
else:
   print("You failed")





    



