"""
############################## Homework TicTacTo ##############################

% Student Name: Angel Ranjel

% Student Unique Name: aranjel

% Lab Section 00X: 

% I worked with the following classmates: 

%%% Please fill in the first 4 lines of this file with the appropriate information before submitting on Canvas.
"""


# CONSTANTS
PLAYER_NAMES = ["Nobody", "X", "O"] 


# FUNCTIONS
def player_name(player_id):
    '''return the name of a player with a specified ID

    Looks up the name in the PLAYER_NAMES global list

    Parameters
    ----------
    player_id: int
        player's id, which is an index into PLAYER_NAMES

    Returns
    -------
    string
        the player's name

    '''
    return PLAYER_NAMES[player_id]


def display_board(board):
    '''display the current state of the board

    board layout:
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9

    Numbers are replaced by players' names once they move. 
    Iterate through the board and choose the right thing
    to display for each cell.

    Parameters
    ----------
    board: list
        the playing board

    Returns
    -------
    None
    '''

    board_to_show = "" 
    for i in range(len(board)):
        if board[i] == 0: 
            board_to_show += str(i + 1)
        else:
            board_to_show += player_name(board[i])
        if (i + 1) % 3 == 0:
            board_to_show += "\n"
        else:
            board_to_show += " | " 
    print()
    print(board_to_show)


def make_move(player, board):
    '''allows a player to make a move in the game

    displays who's move it is (X or O)
    prompts the user to enter a number 1-9
    validates input, repeats until valid input is entered
    checks move is valid (space is unoccupied), repeats until valid move
    is entered
    updates/modifies the board in place when a valid move is entered

    Parameters
    ----------
    player: int
        the id of the player to move (1 = X, 2 = O)

    board: list
        the board upon which to move
        the board is modified in place when a valid move is entered
    '''
    valid_move = False
    while not valid_move:
        try:
            move = int(input(f"Player {player_name(player)}'s turn. Enter a move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif board[move - 1] != 0:
                print("This space is already occupied. Please try another move.")
            else:
                board[move - 1] = player
                valid_move = True
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_win_horizontal(board):
    """Check for a horizontal win on the board.

    This function checks the three rows on a 3x3 Tic-Tac-Toe board to see if there's a horizontal win.
    A win is found if one row contains the same player ID (all '1's for player 1 or all '2's for player 2).

    Parameters
    ----------
    board : list
        the board to check for a win, assumed to be a flat list of 9 integers (0, 1, 2)

    Returns
    -------
    int
        the player ID of the winner if a win is found, or 0 if no win is found.
    """

    if (board[0] != 0 and 
        board[0] == board[1] and 
        board[0] == board[2]):
        return board[0]
    if (board[3] != 0 and
        board[3] == board[4] and 
        board[3] == board[5]):
        return board[3]
    if (board[6] != 0 and
        board[6] == board[7] and 
        board[6] == board[8]):
        return board[6]
    return 0


def check_win_vertical(board):
    """Check for a vertical win on the board.

    This function checks the three columns on a 3x3 Tic-Tac-Toe board to see if there's a vertical win.
    A win is found if one column contains the same player ID (all '1's for player 1 or all '2's for player 2).

    Parameters
    ----------
    board : list
        the board to check for a win, assumed to be a flat list of 9 integers (0, 1, 2)

    Returns
    -------
    int
        the player ID of the winner if a win is found, or 0 if no win is found.
    """
    if (board[0] != 0 and board[0] == board[3] and board[0] == board[6]):
        return board[0]
    if (board[1] != 0 and board[1] == board[4] and board[1] == board[7]):
        return board[1]
    if (board[2] != 0 and board[2] == board[5] and board[2] == board[8]):
        return board[2]
    return 0


def check_win_diagonal(board):
    """Check for a diagonal win on the board.

    This function checks the two diagonal lines on a 3x3 Tic-Tac-Toe board to see if there's a diagonal win.
    A win is found if either diagonal line contains the same player ID (all '1's for player 1 or all '2's for player 2).

    Parameters
    ----------
    board : list
        the board to check for a win, assumed to be a flat list of 9 integers (0, 1, 2)

    Returns
    -------
    int
        the player ID of the winner if a win is found, or 0 if no win is found.
    """
    if (board[0] != 0 and board[0] == board[4] and board[0] == board[8]):
        return board[0]
    if (board[2] != 0 and board[2] == board[4] and board[2] == board[6]):
        return board[2]
    return 0


def check_win(board):
    '''checks a board to see if there's a winner

    delegates to functions that check horizontally, vertically, and 
    diagonally to see if there is a winner. Returns the first winner
    found in the case of multiple winners.

    Parameters
    ----------        
    board: list
        the board to check

    Returns
    -------
    int
        the player ID of the winner. 0 means no winner found.
    '''

    winner = check_win_horizontal(board)
    if (winner != 0):
        return winner
    
    winner = check_win_vertical(board)
    if (winner != 0):
        return winner
    
    return check_win_diagonal(board)


def next_player(current_player):
    '''determines who goes next

    given the current player ID, returns the player who should 
    go next

    Parameters
    ----------        
    current_player: int
        the id of the player who's turn it is now

    Returns
    -------
    int
        the id of the player to go next
    '''
    """Determines who goes next.

    Given the current player ID, returns the player who should go next by toggling between player 1 and 2.

    Parameters
    ----------        
    current_player : int
        the id of the player who's turn it is now

    Returns
    -------
    int
        the id of the player to go next
    """
    return 2 if current_player == 1 else 1

# MAIN PROGRAM (INDENT LEVEL 0)

# GLOBAL VARIABLES
board = [0, 0, 0,   # top row:    indices 0, 1, 2
         0, 0, 0,   # middle row: indices 3, 4, 5
         0, 0, 0]   # bottom row: indices 6, 7, 8

player = 1          # X goes first
moves_left = 9      # number of moves so far 
winner = 0          # "Nobody" is winning to start

while(moves_left > 0 and winner == 0):
    display_board(board)
    make_move(player, board)
    winner = check_win(board)
    if winner != 0:
        display_board(board)
        print(f"Game over! {player_name(winner)} wins!")
        break
    player = next_player(player)
    moves_left -= 1

if winner == 0:
    display_board(board)
    print("Game over! Nobody wins!")

