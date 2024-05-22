'''A simple text-based, 2-player tic-tac-toe game.'''

empty_board = '___|___|___\n___|___|___\n   |   |   '

positions = {'1':1, '2':5, '3':9, 
            '4':13, '5':17, '6':21, 
            '7':25, '8':29, '9':33}

winning_combos = [(1, 5, 9), (13, 17, 21), (25, 29, 33),
               (1, 13, 25), (5, 17, 29), (9, 21, 33),
               (1, 17, 33), (9, 17, 25)]

p1_char, p2_char = 'X', 'O'


def show_possible_pos():
    '''Displays board with positions 1-9 labeled for start of game instructions.'''
    posgrid = list(empty_board)

    for position, index in positions.items():
        posgrid[index] = position

    posgrid = ''.join(posgrid)

    print(f"Possible positions to enter during the game are as follows:\n{posgrid}\n")

def player_continue():
    '''Prompts the player to hit enter to continue.'''
    input("Press ENTER to continue...\n")

def execute_turn(board, turn):
    '''Displays board, has player take next turn, and returns board with marker placed.'''

    # show current turn and board
    print(f"\nTurn {turn}: Current board:\n{board}\n")

    # convert to list for later inserting player marker
    board = list(board)
    
    # get player, marker
    if turn % 2 == 0:
        player = 2
        marker = p2_char
    else:
        player = 1
        marker = p1_char

    # get player choice, ensure player enters number 1-9
    pos = ''
    while pos not in positions:
        pos = input(f"Player {player}, it's your turn. Enter an open position 1-9:\n")

    index = positions[pos]
    
    # place marker at position, return board
    board[index] = marker

    board = ''.join(board)
    return board

def game_mainloop():
    '''Main game loop.'''
    # setup
    game_board = empty_board
    winner = None
    current_turn = 0
    board_full_no_winner = False

    # begin game
    print("Let's play tic-tac-toe. Player 1, you are X, and Player 2, you are O.\n")

    player_continue()

    show_possible_pos()

    player_continue()

    while not winner and not board_full_no_winner:
        current_turn +=1
        game_board = execute_turn(game_board, current_turn)

        # check for winner
        for combo in winning_combos:
            p1_count = 0
            p2_count = 0
            for pos in combo:
                if game_board[pos] == 'X':
                    p1_count += 1
                if game_board[pos] == 'O':
                    p2_count += 1
            if p1_count == 3:
                winner = "PLAYER 1"
                break
            elif p2_count == 3:
                winner = 'PLAYER 2'
                break
                
        # check for full board no winner
        full_count = 0
        for pos in positions.values():
            if game_board[pos] in ["X", "O"]:
                full_count += 1

        if full_count == 9:
            board_full_no_winner = True

    if winner:
        print(game_board)
        print(f"\n{winner} WINS!")
    elif board_full_no_winner:
        print(game_board)
        print(f"\nTIE!")


if __name__ == "__main__":
    game_mainloop()