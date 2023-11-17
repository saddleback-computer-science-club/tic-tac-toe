from game import *

def test_hasWon():
    board = [['X', 'X', 'X'],
             [' ', ' ', ' '],
             ['O', 'O', 'O']]
    
    assert has_won(board, 'X') == True
    assert has_won(board, 'O') == True

    board = [['X', ' ', 'O'],
             ['X', ' ', 'O'],
             ['O', ' ', 'O']]
    
    assert has_won(board, 'X') == False
    assert has_won(board, 'O') == True

    board = [['X', 'O', 'X'],
             ['O', 'X', 'O'],
             ['O', 'X', 'O']]
    
    assert has_won(board, 'X') == False
    assert has_won(board, 'O') == False

    board = [['X', ' ', ' '],
             [' ', 'X', ' '],
             [' ', ' ', 'X']]
    
    assert has_won(board, 'X') == True

    board = [[' ', ' ', 'X'],
             [' ', 'X', ' '],
             ['X', ' ', ' ']]
    
    assert has_won(board, 'X') == True