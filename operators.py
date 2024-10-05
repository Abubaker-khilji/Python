name = input("Enter	you name : ")

if  len(name) < 3:
    print("name must be atleast 3 character long") 
elif len(name) > 50:
    print("name must be atleast 50 characters long")    
else:
    print(f"name looks good! {name} ")    
