import random
computer_number = random.randint(1, 50)

while True:
    guess = int(input('\nGuess a number between 1, 50: '))  
    if guess > computer_number:
        print('Too high...')
    elif guess < computer_number:
        print('Too low...')
    else:
        print(f'\nYou win, the correct the number was {computer_number}.')
        rematch = input('\nDo you want to play again (y/n)? ').lower()
        if rematch.lower() == 'y':
            computer_number = random.randint(1, 50)
        else:
            print('\nThanks for playing!\n')
            break
        



    

    
   
