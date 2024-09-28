vp = int(input("Enter your age: "))
vp_name = input("Enter your name: ")
gender = input("Enter your gender: ")

if vp > 18:
    print("Congratulations, you are eligible for voting", vp_name)
    candidatename = input("Please choose your candidate name: TLP, TTP, PMLN, PLMQ, PTI, PPP ")
    
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
else:
    print("Not eligible for voting:", vp_name)

print("Thank you for voting")
