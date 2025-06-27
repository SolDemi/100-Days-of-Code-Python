import random
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

game = [scissors, rock, paper]

computer_choice = random.randint(0, 2)
user_choice = input("Please choose：o = scissors, 1 = rock, 2 = paper\n")
t = user_choice - computer_choice
print(game[user_choice])
print(game[computer_choice])

if t == 1 or t == -2:
    print("You WIN!")
elif t == -1 or t == 2:
    print("You lose...")
elif t == 0:
    print("It's a draw...")
else:
    print("You type a invalid number.")
