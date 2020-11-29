import random  

# random integet
number = random.randint(0, 10)

# stores user choice for game continuation
choice = ''

# stores user's guess
guess = -1


while guess != number:
    # user enter his/her guess here
    guess = eval(input("Guess the number: "))

    # check if user won 
    if guess == number: 
        print ("You guessed it right!!")
        
        # ask for game continuation
        choice = input("Do you want to continue? " )

        if choice == 'y' or choice == 'Y':
            guess = -1
            number = random.randint(0, 10)
        elif choice == 'n' or choice == 'N':
            break


        
