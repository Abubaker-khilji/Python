# import secretcode as sc
# import kbc 
# name = input("Please enter your name ")
# gamename = input(f"hello  {name} how are u please choose the game u wanted to play : secretscode,kbc ")
    
# match gamename:
#         case "secretcode":
#             print("----------------wait secretcode loading-----------------")
#             sc.encoder()
#             sc.decoder()
#         case "kbc":
#             print("----------------wait kbc loading-----------------")
#             kbc.games()
#         case "PMLN":
#             print("You've voted for PMLN")
#         case "PLMQ":
#             print("You've voted for PLMQ")
#         case "PTI":
#             print("You've voted for PTI")
#         case "PPP":
#              print("You've voted for PPP")
#         case "none":
#             print("---------------Please come back whenever u get bored----------------")
#import secretcode as sc
#import kbc 

if __name__ == "__main__":
    name = input("Please enter your name: ")
    gamename = input(f"Hello {name}, please choose the game you want to play (secretcode, kbc): ")

 #   if gamename == "secretcode":
 #       sc.encoder(code)
 #   elif gamename == "kbc":
  #      kbc.games(name)
   # else:
    #    print("---------------Please come back whenever you get bored----------------")