## Number Guessing Game
## This is number guessing game in which user has to guess randomly generated number in minimum 5 trial.

##  Author Details 

## Name  :  Er. Amar kumar 
## Email :  amarkumar9685079691@gmail.com 

## Start of a Game ##

import random 

print("Hi, You're welcome to play number guessing game! ")
print("Let's Play Game")
print("Best of luck!")

low  = int(input("Enter lower number of your range in which you want to guess number! \n"))
high = int(input("Enter higher number of your range in which you want to guess number! \n"))

actual_number = random.randrange(low, high)

allowed_trials = 5 

your_trials = 0

while your_trials < allowed_trials : 
    
    current_number = int(input("Enter your guess number! \n"))
    your_trials +=1
    
    if current_number == actual_number:

        print("Congratulations!")
        print("You won the game")
        print("Your score: ",your_trials)
        
        play_again = int(input("If you want to play game again then please type 1 or 2 to exit!"))
        
        if play_again == 1: 
           actual_number = random.randrange(low, high)
           your_trials = 0
        else:
           print("Thank you for playing a game! Bye")      
           break

    else:

        if your_trials >= allowed_trials:
            print("Ohh! You have used all allowed trials")
            print("Better Luck Next Time!")
            break 

        if current_number < actual_number:
            print("Try Again! You guessed too small")
        else:
            print("Try Again! You guessed too high")
            

## End of a Game ##

