"""Write a password generator in Python. Be creative with how you generate passwords.
Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

import string
import random

x, y, z = None, None, None
pass_lenght = None
def options():
    global x, y, z
    x=input("Do you want uppercases?(Y/N): ")
    y=input("Do wou want numbers?(Y/N): ")
    z=input("Do you want special characters?(Y/N): ")
    x,y,z = x.upper(),y.upper(),z.upper()

    if (x != "N" and x != "Y") or (y != "Y" and y !="N") or (z != "N" and z != "Y"):
        print("Put Y/N ")
        options()
    return x, y, z

def gen_pass():
    global x, y, z, pass_lenght
    if x == "Y":
        p1=string.ascii_letters
    else:
        p1 = string.ascii_lowercase
    if y == "Y":
        p2=string.digits
    else:
        p2=""
    if z == "Y":
        p3=string.punctuation
    else:
        p3=""
    return "".join(random.sample(list(p1+p2+p3), pass_lenght))

def satisfy():
    ask=input("\nAre you satisfied with the pasword?(Y/N): ")
    ask=ask.upper()

    if ask == "Y":
        quit("Good bye")
    elif ask == "N":
        main()
    else:
        satisfy()

def main():
    global pass_lenght
    try:
        new=input("Do you want new password?:(Y/N) ")
        new=new.upper()
        if new == "Y":
            pass_lenght = int(input("How many characters should contain your password?: "))
            print("Choose which special characters you want:")
            options()
            print("\nYou chose: \nDo you want uppercases?: ", x, " Do you want numbers?: ", y,
                  " Do you want special characters?: ", z)
            print("Generated password: ", gen_pass())
            satisfy()
        elif new =="N":
            quit("Good bye")
        else:
            print("Put Y or N")
            main()

    except ValueError:
        print("Put an integer")

main()

