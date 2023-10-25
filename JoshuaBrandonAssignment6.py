import random


def main():
    print('Assignment 6 by Joshua Brandon')

print('Welcome to the guessing game. I have selected a number between 1 and 100 inclusive. Your goal is to guess it in as few guesses as possible. Let’s get started. ')
Continue = 'y'
ask_continue = 'ok'
while (Continue == 'y'):
    Continue = 'n'
    Correct = random.randint(1,100)
    Loop = bool(True)
    guess_count = 0
    low_value = 1
    high_value = 100
    while (Loop == True):
        ask_continue = 'ok'
        guess = int(input(f'What is your guess between {low_value} and {high_value} inclusive? '))
        if(guess == -999):
            print('Thanks for playing. See you another day.')
            Loop = False
        elif(guess < low_value or guess > high_value):
            print('Invalid guess – out of range. Guess doesn’t count. Guess again. ')
        else:
            guess_count += 1
            if (guess == Correct):
                print(f'Congratulations you won in {guess_count} guesses.')
                Loop = False
                
                while (ask_continue != 'y' and ask_continue != 'n'):
                    print('')
                    ask_continue = input('Would you like to play again (y or n)? ')
                    if ask_continue == 'y':
                        Continue = 'y'
                        print('')
                        print('OK. Let\'s play again.')
                        Loop = True
                        guess_count = 0
                        Correct = random.randint(1,100)
                        low_value = 1
                        high_value = 100
                    elif ask_continue == 'n':
                        Continue = 'n'
                        print('')
                        print('OK. Have a good day.')
                    else:
                        print('I\'m sorry, I do not understand that answer.')
            elif(guess < Correct):
                print('Your guess was too low. Guess again.')
                low_value = guess + 1
            elif(guess > Correct):
                print('Your guess was too high. Guess again.')
                high_value = guess - 1

    
        

main()
