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
print ("Welcome to rock - paper - scissors game")
user_choice = input("Please type one of the following options: rock, paper, or scissors.\n ").lower()
print(f"You have choosen {user_choice}.")
if user_choice == "rock":
  print (rock)
elif user_choice == "paper":
  print (paper)
elif user_choice == "scissors":
  print (scissors)
else:
  print ("invalid value")
computer_choice = [rock, paper, scissors]
comp_result = random.choice(computer_choice)
if comp_result == rock:
  print("The computer has choosen rock")
elif comp_result == paper:
  print("The computer has choosen paper")
else: 
  print("The computer has choosen scissors")
print(comp_result)
if user_choice == "rock" and comp_result == rock :
  print ("This is a draw")
elif user_choice == "paper" and comp_result == paper :
  print ("This is a draw")
elif user_choice == "scissors" and comp_result == scissors :  print ("This is a draw")
elif user_choice == "rock" and comp_result == paper :
  print ("The computer won this match")
elif user_choice == "rock" and comp_result == scissors :
  print ("You won this match")
elif user_choice == "paper" and comp_result == rock :
  print ("You won this match")
elif user_choice == "paper" and comp_result == scissors :
  print ("The computer won this match")
elif user_choice == "scissors" and comp_result == rock :
  print ("The computer won this match")
elif user_choice == "scissors" and comp_result == paper :
  print ("You won this match")
else:
    print ("You lose")
