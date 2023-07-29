import random

#make the computer generate random integer using random library
computer_guess = random.randint(1, 99)
user_answer = input("Do you want to play? Yes or  No?").upper()
while user_answer == 'YES':
    #get user input
    your_guess = int(input("guess your number: "))
    if your_guess != computer_guess:
        print("wrong guess, try again")
    else:
        print("You got it!")
        break
