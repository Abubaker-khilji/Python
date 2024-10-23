import string
import random


code = input("Enter your string must be larger than three character:  ")
ask = input("the string you enter what you want us to do decoding or encoding").lower()

def encoder(code):
            global stringfinal
            if len(code)>3:
                print(f"the string u enter is {code}")
                str1=code[0:3]

                # print(str1)
                secretcode = code + str1
                # print(f"the string  after appending  is {secretcode}")
                newsecretcode = secretcode[3:]
                # print(f"the final string code is {newsecretcode}")

                N = 3

                # using random.choices()
        # generating random strings
                res = ''.join(random.choices(string.ascii_lowercase +
                                        string.punctuation, k=N))
                stringfinal = newsecretcode + res                         
                print(f"the fullfinal string code is {stringfinal}")
                                    
            else:
                print(code[::-1])


def decoder():
        global stringfinal
        if len(code)<3:
          print(f"the reverse string is {stringfinal[::-1]}")
        else:
            # Remove the last 3 random characters
            decoded_without_random = stringfinal[:-3]

            # Add the first 3 characters that were originally removed back to the start
            original_code = decoded_without_random[-3:] + decoded_without_random[:-3]
            
            print(f"The decoded string is: {original_code}")



# Main logic based on user input
if ask == "encoding":
    encoder(code)  # Call the encoder function

elif ask == "decoding":
    # Call the decoder function
    if stringfinal == "":
        print("No encoded string found! Please run the encoding process first.")
    else:
        decoder()

else:
    print("The term you entered is invalid.")       



      
       



