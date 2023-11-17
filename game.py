import random

def initialize_game():
    print("Welcome to Tic-Tac-Toe! The rules are as follows:\n"
          "\t1) Players (X and O) choose spots to play on a 3x3 board\n"
          "\t2) The first player to attain 3 in a row, column, or diagonal wins!\n"
          "\t3) If the board is full with no winners, the two players tie\n")
    
    against_computer_raw = \
        input("Would you like to play against the computer? (Y/N): ").lower()
    
    while against_computer_raw != 'y' and against_computer_raw != 'n':
        against_computer_raw = input("Invalid choice, try again! (Y/N): ").lower()

    return (against_computer_raw == 'y')

def is_valid_square(board, row, col):
        """
        Checks whether the row and column entered is a valid position based on:
            Whether row and column are within bounds [0, 2]
            Whether the square is already occupied
        """

        if not 0 <= row <= 2 or not 0 <= col <= 2:
            return False
        
        if board[row][col] != ' ':
            return False
        
        return True

def get_player_choice(board):
    """
    Parses and verifies user input to choose a square on the board
    """

    print("Enter the empty square to play on")
    row = int(input("\trow: "))
    col = int(input("\tcolumn: "))

    # Input validation
    while not is_valid_square(board, row, col):
        print("Invalid choice, try again!")
        row = int(input("\trow: "))
        col = int(input("\tcolumn: "))
    
    return (row, col)

def get_computer_choice(board):
    row, col = random.randrange(3), random.randrange(3)
    while not is_valid_square(board, row, col):
        row, col = random.randrange(3), random.randrange(3)
    return (row, col)

def print_board(board):
    for i,row in enumerate(board):
        print(f'{row[0]:^3}|{row[1]:^3}|{row[2]:^3}')
        if i < 2: print('---+---+---')

def has_won(board, player):
    """
    Checks whether a specified player has won the tic-tac-toe game

    Parameters:
    board -- A 2D list holding the current board state
    player -- The string representing the player that just played ("X" or "O")
    
    Return:
    won -- (bool) whether the specified player has won
    """
    
    # Flag value used in nested loops. Set to False upon finding of 
    won = False

    # Check rows
    for row in board:
        won = True
        for square in row:
            if square != player:
                won = False
                break
        if won:
            return True
    # Check columns
    for col_idx in range(len(board)):
        won = True
        for row in board:
            if row[col_idx] != player:
                won = False
                break
        if won:
            return True
    # Check diagonal (start = top left)
    for idx in range(len(board)):
        won = True
        if board[idx][idx] != player:
            won = False
            break
    if won:
        return True
    # Check diagonal (start = top right)
    for idx in range(len(board)):
        won = True
        if board[idx][-1-idx] != player:
            won = False
            break
    if won:
        return True
    
    return False

def game():
    in_play = True
    board = [[' ' for _ in range(3)] for _ in range(3)]
    against_computer = initialize_game()

    current_player = ''

    while in_play:
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

        print_board(board)
        if current_player == 'O' and against_computer:
            print("Computer's turn")
            row, col = get_computer_choice(board)
        else:
            print(f"Player {current_player}'s turn")
            row, col = get_player_choice(board)
        board[row][col] = current_player
        in_play = not has_won(board, current_player)

    
    if current_player == 'O' and against_computer:
        print('Uh oh! You lost against the computer')
    else:
        print(f'Congrats! Player {current_player} won!')

if __name__ == "__main__":
    game()