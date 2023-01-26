import random
import time

header = "=" * 100
texto = "Welcome to the Rock - Papper - Scissors game"
print(header)
print(texto.upper().center(len(header)))
print(header)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("0", rock)
print()
print("1", paper)
print()
print("2", scissors)
print()

game_images = [rock, paper, scissors]




while True:
    
    try:

        computer_choice = random.randint(0, 2)
        
        x = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors and 3 to shut it dowm. "))

        if x == 3:

            print(f"You chose {x}, so I will shut myself down. See you later, bye!")
            time.sleep(3)
            break

        elif x != 0 and x != 1 and x != 2:
            time.sleep(2)
            print("You chose:", x, game_images[x])
            print("Computer chose:", game_images[computer_choice])
            print("Wrong! You lose!")
            
    #Condicionais para variável x == 0

        elif x == 0 and computer_choice == 0:
            time.sleep(1)
            print("You chose:", x, game_images[x])
            print("Computer chose:", game_images[computer_choice])
            print("Draw!")
            

        elif x == 0 and computer_choice == 1:
            time.sleep(1)
            print("You chose:", x, game_images[x])
            print("Computer chose:", computer_choice, game_images[computer_choice])
            print("You lose!")

        elif x == 0 and computer_choice == 2:
            time.sleep(1)
            print("You chose:", x, game_images[x])
            print("Computer chose:", computer_choice, game_images[computer_choice])
            print("You win!")

        #Condicionais para variável x == 1

        elif x == 1 and computer_choice == 0:
            time.sleep(1)
            print("You chose:", x, game_images[x])
            print("Computer chose:", computer_choice, game_images[computer_choice])
            print("You win!")
            time.sleep(1)

        elif x == 1 and computer_choice == 1:
            time.sleep(1)
            print("You chose:", x, game_images[x])
            print("Computer chose", computer_choice, game_images[computer_choice])
            print("Draw!")          

        elif x == 1 and computer_choice == 2:
            time.sleep(1)
            print(f"You chose: {x}, {game_images[x]}")
            print("Computer chose:", computer_choice, game_images[computer_choice])
            print("You lose!")

        #Condicionais para variável x == 2

        elif x == 2 and computer_choice == 0:
            time.sleep(1)
            print("You chose:", x, game_images[x])
            print("Computer chose:", computer_choice, game_images[computer_choice])
            print('You lose!')
        
        elif x == 2 and computer_choice == 1:
            time.sleep(1)
            print("You chose:", x, game_images[x])
            print("Computer chose:", computer_choice, game_images[computer_choice])
            print("You win!")         
        
        elif x == 2 and computer_choice == 2:

            time.sleep(1)
            print("You chose:", x, game_images[x])
            print("Computer chose:", computer_choice, game_images[computer_choice])
            print("Draw!")

    except:
            print("Invalid data!")
            continue
