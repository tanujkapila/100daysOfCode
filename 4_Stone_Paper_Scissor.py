#https://replit.com/@TanujKapila/rock-paper-scissors-start#main.py
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

#Write your code below this line 👇
choice_list = [rock,paper,scissors]
x=0
while x != 3:    
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. 3 to exit \n"))
  if user_choice > 3 or user_choice < 0:
    print("Invalid choice")
  elif user_choice == 3 :
    x=3
    print("Thank you for playing")
  else:
    print(choice_list[user_choice])
    print("Computer Choice: \n")
    computer_choice= random.randint(0,2)
    print(choice_list[computer_choice])
    if user_choice == 0 :
      if computer_choice == 0 :
       print("It's a Tie")
      elif computer_choice == 1 :
       print("You Lose")
      else:
       print("You Win")

    if user_choice == 1:
      if computer_choice == 0:
       print("You Win")
      elif computer_choice == 1 :
       print("It's a Tie")
      else:
       print("You Lose")

    if user_choice == 2:
      if computer_choice == 0:
       print("You Lose")
      elif computer_choice == 1 :
       print("You Win")
      else:
       print("It's a Tie")







