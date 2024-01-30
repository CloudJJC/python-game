print('''
****************************************************************
                                     888                      
                                     888                      
                                     888                      
 .d88b.  8888b. 88888b.d88b.  .d88b. 88888b.  .d88b. 888  888 
d88P"88b    "88b888 "888 "88bd8P  Y8b888 "88bd88""88b888  888 
888  888.d888888888  888  88888888888888  888888  888888  888 
Y88b 888888  888888  888  888Y8b.    888 d88PY88..88PY88b 888 
 "Y88888"Y888888888  888  888 "Y8888 88888P"  "Y88P"  "Y88888 
     888                                                  888 
Y8b d88P                                             Y8b d88P 
 "Y88P"                                               "Y88P"  

*****************************************************************
''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
choiceA = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if choiceA == "left":
  choiceB = input("You have to make another choice. Type 'swim' or 'wait'\n")
  if choiceB == "wait":
    choiceC = input("You have to make a choice between three doors. Type 'red', 'blue' or 'yellow'\n")
    if choiceC == "yellow":
      print("You win!")
    elif choiceC == "blue":
      print("You've been eaten by wild beasts. Game over!")
    elif choiceC == "red":
      print("Burned by fire. Otilo! Game over!")
    else:
      print("Game over!")
  else:
    print("You've been attacked by a trout. Game over!")
else:
  print("You've fallen into a hole. It's game over! Otilo!!")