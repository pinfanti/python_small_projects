import random                 

logo = ''' 

  ▄████ █    ██▓█████  ██████  ██████      ▄████ ▄▄▄      ███▄ ▄███▓█████    
 ██▒ ▀█▒██  ▓██▓█   ▀▒██    ▒▒██    ▒     ██▒ ▀█▒████▄   ▓██▒▀█▀ ██▓█   ▀    
▒██░▄▄▄▓██  ▒██▒███  ░ ▓██▄  ░ ▓██▄      ▒██░▄▄▄▒██  ▀█▄ ▓██    ▓██▒███      
░▓█  ██▓▓█  ░██▒▓█  ▄  ▒   ██▒ ▒   ██▒   ░▓█  ██░██▄▄▄▄██▒██    ▒██▒▓█  ▄    
░▒▓███▀▒▒█████▓░▒████▒██████▒▒██████▒▒   ░▒▓███▀▒▓█   ▓██▒██▒   ░██░▒████▒   
 ░▒   ▒░▒▓▒ ▒ ▒░░ ▒░ ▒ ▒▓▒ ▒ ▒ ▒▓▒ ▒ ░    ░▒   ▒ ▒▒   ▓▒█░ ▒░   ░  ░░ ▒░ ░   
  ░   ░░░▒░ ░ ░ ░ ░  ░ ░▒  ░ ░ ░▒  ░ ░     ░   ░  ▒   ▒▒ ░  ░      ░░ ░  ░   
░ ░   ░ ░░░ ░ ░   ░  ░  ░  ░ ░  ░  ░     ░ ░   ░  ░   ▒  ░      ░     ░      
      ░   ░       ░  ░     ░       ░           ░      ░  ░      ░     ░  ░   
                                                                             
                                                                                   
 '''
def generate_number():
   random_number = random.randrange(101)
   return random_number

def logic_game (gen_number, num_range):
  run_flag = True
  x = 0
  while run_flag ==True and x < num_range:
    x += 1
    guess = int(input("Make a guess only Numbers:\n"))
    if gen_number > guess:
      print("Too Low\nGuess Again\n")
      print (f"You have {num_range - x} attempts remaining to guess the number")
    elif gen_number < guess:
      print("Too High\n Guess Again\n")
      print (f"You have {num_range - x} attempts remaining to guess the number")
    else:
      run_flag = False
  if run_flag == True:
    print ("You've run out of guesses, you lose.")
  else: 
    print (f"You got it! The answer is {gen_number}")

print (logo)
print ("Welcome to the Number Guessing Game!")
final_number = generate_number()
difficult = input("Choose a difficulty. Type 'easy' or 'hard\n")
if difficult =="easy":
  logic_game (final_number, 10)
elif difficult == "hard":
  logic_game (final_number, 5)
else:
  print ("Invalid information start again")





