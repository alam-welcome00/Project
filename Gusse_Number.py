import random

target = random.randint(1,10)

while True:
    userNum = input("Gusse the number or Quit: ")
    if userNum == "Q":
        print("__end__")
        break
    userNum = int(userNum)
    if userNum == target:
        print("Winner!!")
        break
    elif userNum < target:
        print("Your number is to small, try to gusse bigger Number")
    else:
        print("Your number is too big, try to gusse smaller number")