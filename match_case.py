vp=int(input("Enter your age: "))
vp_name=input("Enter your name: ")
gender=input("Enter your gender: ")


if(age>18):
  print("congratulations you are eligible for voting", vp_name)
  

candidatename=input("please choose your candidate name: TLP,TTP,PMLN,PLMQ,PTI,PPP " )
match candidatename:
    case "TLP":
      print("You've voted for TLP")
    case "TTP":
      print("You've voted for TTP")
    case "PMLN":
      print("You've voted for PMLN")
    case "PLMQ":
      print("You've voted for PLMQ")
    case "PTI":
      print("You've voted for PTI")
    case "PPP":
      print("You've voted for PPP")
    case "none":
      print("You haven't voted")

else(age<18):
    print("not eligible for voting :  " , vp_name)


print("Thank you for voting")

                    



  


  