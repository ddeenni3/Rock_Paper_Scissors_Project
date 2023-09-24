import random

valid_options = ['r', 'p', 's']

player_move = input('Choose [r]ock, [p]aper or [s]cissors: ').lower()

if player_move in valid_options:
    computer_rng = random.randrange(len(valid_options))
    computer_move = valid_options[computer_rng]
    computer_print = ''
    if computer_move == 'r':
        computer_print = 'rock'
    elif computer_move == 'p':
        computer_print = 'paper'
    elif computer_move == 's':
        computer_print = 'scissors'
    print(f'The computer has chosen {computer_print}')
    if player_move == computer_move:
        print('Draw!')
    elif (player_move == 's' and computer_move == 'p') or\
            (player_move == 'r' and computer_move == 's') or\
            (player_move == 'p' and computer_move == 'r'):
        print('You win!')
    else:
        print('You lose!')
else:
    raise SystemExit('Invalid input. Try again.')
