command = ""
started = False
while True:
    command= input("> ").lower()
    if command == "start":
        if started:
            print("caaar is already startedddd uuu piece of shit ")
        else:
            started = True
            print("car start")
    elif command == "stop":
        print("car stop")
    elif command == "help":
        print("""
for car start type 'start'
for car stop type 'stop'
for car quit type 'quit'
for help type 'help'
        """)      
    elif command == "quit":
        break
    else:
        print("this command does not exist")  

