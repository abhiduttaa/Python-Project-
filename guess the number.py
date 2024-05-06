import random

Target=random.randint(1,100)
# print(randnum)
while True:
    userchoice = (input("Guess the target or Quit="))
    if(userchoice == "Quit"):
        break
    userchoice = int(userchoice)
    if(userchoice == Target):
        print("Suceess : Correct Guess!!")
        break
    elif(userchoice<Target):
        print("Your Number Was too small.Take a bigger Guess.........")
    else:
        print("Your Number Was too Big.Take a Smaller Guess.........")



print("------Game End-------")