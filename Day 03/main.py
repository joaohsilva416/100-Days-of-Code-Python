print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input("You are at a crossroads. Do you want to go 'left' or 'right'? ").lower()

if road == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake.\n"
                 "Type 'wait' to wait for a boat or 'swim' to swim across. ").lower()

    if lake == "wait":
        house_doors = input("You arrived at the island unharmed. There is a house with 3 doors.\n"
                            "One red, one yellow and one blue. Which colour do you choose? ").lower()

        if house_doors == "red":
            print("Burned by fire.\n"
                  "Gamer Over!")
        elif house_doors == "blue":
            print("Eaten by beasts.\n"
                  "Game Over!")
        elif house_doors == "yellow":
            print("You Win!!!")
        else:
            print("Game Over!")

    else:
        print("Attacked by trout. \n"
              "Game Over!")

else:
    print("Fall into a hole.\n"
          "Game Over!")
