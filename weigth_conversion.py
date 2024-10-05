weight = int (input("Enter your weight:  "))

conversion = input ("(L)bs or (K)gs "  )

if conversion.upper() == "L":
    converted = weight*0.45
    print(f"your {converted} weight in kiligrams")
else:
    converted = weight / 0.45
    print(f"your {converted} weight  in pounds ")