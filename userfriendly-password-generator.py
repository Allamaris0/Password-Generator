"""User-friendly password generator
The program generates password using words_aplha.txt from https://github.com/dwyl/english-words"""

import random
import string

#Loading a file with English words
def load_words():
    word_file=open("words_alpha.txt","r")
    return word_file.readlines()

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

    if y == "Y":
        p2=str(random.randint(0,9))
    else:
        p2=""

    if z == "Y" and y == "Y":
        p3=random.choice(string.punctuation)
    else:
        p3=""

    new_words = []
    for w in load_words():
        if len(w.strip()) == pass_lenght - len(p2) - len(p3):
            new_words.append(w.strip())

    if len(new_words)== 0:
        return "We'ry sorry but our dictionary doesn't have so long word"
    elif x == "Y":
        return (random.choice(new_words)+p2+p3).capitalize()
    else:
        return random.choice(new_words)+p2+p3

def satisfy():
    ask=input("\nAre you satisfied with the password?(Y/N): ")
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
