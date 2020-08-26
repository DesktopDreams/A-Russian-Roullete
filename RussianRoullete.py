#This is russian roullete game, where in 5/6, you get a luxurious reward.
#But theres a 1/6 chance it will be fatal!

#We start by importing some functions.
import random
from time import sleep

#Headline to welcome the users.
print('Welcome to the game of russian roullete, o brave soul!')

#Program to pick random numbers
def random():
    global number
    import random
    number = random.randint(1,6)
    
#Program to ask user if they want to enter a number or random.
while True:
    try:
        print('Please choose between the option "number" and "random"')
        option = input()
    except TypeError and ValueError:
        print('Your choice are not available!')
        continue
    #If user chose number, this program will make sure user only input numbers between 1 and 6.
    if option == 'number':
        print('You have chosen to enter your own number!')
        sleep(1)
        while True:
            try:
                print('Please choose between number 1 and 6')
                number = int(input())
            except TypeError and ValueError:
                print('Your input are invalid!')
                continue
            if 1 <= number <= 6:
                print('Excellent choice! Or is it...?')
                break
            else:
                continue
        break
    #If user chose random, this program will automatically choose a number for the user.
    elif option == 'random':
        random()
        print('You got ' + str(number) + '!')
        break
    #If user choose anything but 'number' and 'random', they will need to choose again.
    else:
        print('Did you even choose anything!?')
        continue

#Program to determine the user's outcome.
#First we create a list of options for the program to choose
aaa = ['You won 8$ million dollars!', 'You inherited 9 acres of land!', 'You received $10000 worth gaming rig', 'Your steam account has been gifted all available games in the store', 'Your body is free of sickness!', 'You are killed until death']

#Then we create function that prints the result
def outcomes():
    import random
    print(random.choice(aaa))
    print('Thank you for playing!')
    
#We now give out the result based on the number the user selected or given
if number in range(0,7):
    outcomes()

          

    
            
                

        

        
