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

human = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if human == "0":
  print(rock)
elif human == "1":
  print(paper)
elif human == "2":
  print(scissors)
else:
  print("Please select a number between 0 and 2.")

print("Computer chose:")

import random

prs = [rock, paper, scissors]

random_number = random.randint(0, 2)

computer = prs[random_number]

print(computer)

if human == "0":
  if computer == rock:
    print("It's a draw.")
  elif computer == paper:
    print("You lose.")
  elif computer == scissors:
    print("You win.")
elif human == "1":
  if computer == rock:
    print("You win.")
  elif computer == paper:
    print("It's a draw.")
  elif computer == scissors:
    print("You lose.")
elif human == "2":
  if computer == rock:
    print("You lose.")
  elif computer == paper:
    print("You lose.")
  elif computer == scissors:
    print("It's a draw.")
else:
  print("Because you chose an invalid number, you lose!")