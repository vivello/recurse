# tic-tac-toe game

import copy

# *********
# HELPERS
# *********

# check_lines(board, size) returns which player has completed a row on the board, if any
def check_lines(board, size):
    for row in board:
        if row.count("X") == size:
            return "X"
        elif row.count("O") == size:
            return "O"
    return "None"

# flip_board(board, size) inverts the rows and columns of a board
def flip_board(board, size):
    flipped = []
    for i in range(size):
        new_row = []
        for row in board:
            new_row.append(row[i])
        flipped.append(new_row)
    return flipped

# diags(board, size) represents the diagonals of a board as rows
def diags(board, size):
    lines = [[],[]]
    for i in range(size):
           lines[0].append(board[i][i])
           lines[1].append(board[i][-i - 1])
    return lines

# gen_board(size) generates a tic tac toe board where the dimensions are size * size
def gen_board(size):
    board = []
    empty_row = [" "] * size
    for i in range(size):
        board.append(copy.deepcopy(empty_row))
    return board



# ************
# CLASS STUFF
# ************
        

class TTT:
    # TTT() produces a new tic-tac-toe board and game state
    # __init__: -> TTT
    def __init__(self, board_size=3):
        self._size = board_size
        self._board = gen_board(self._size)
        self._player = "X"
        self._turn = 0
        self._winner = ""

    # self.show_board() produces a string representation of the tic-tac-toe board
    def show_board(self):
        board = "    "
        line = ""
        for i in range(self._size):
            line += str(i) + " " * 3
        board += line + "\n\n"
        for i in range(self._size):
            line = str(i) + "  "
            for j in range(self._size):
                if j < (self._size - 1):
                    line += " " + self._board[i][j] + " |"
                else:
                    line += " " + self._board[i][j] + " \n"
            if i < (self._size - 1):
                line += "   " + ("--- " * self._size) + "\n"
            board += line
        return board 
    
    ##    Sample Board
##
##        0   1   2
##         
##    0   X | O | X 
##       --- --- ---
##    1   O | X | O
##       --- --- ---
##    2   X | O | X
##    

    # self.add(self, col, row) enters the player's move into the board if it is valid
    def add(self):
        while True:
            col, row = input("Enter the column and then the row number for your square selection separated by a space: ").split()
            col = int(col)
            row = int(row)
            if col < 0 or col > (self._size - 1):
                print("Please enter a valid column selection")
                continue
            elif row < 0 or row > (self._size - 1):
                print("Please enter a valid row selection")
                continue
            else:
                if self._board[row][col] == " ":
                    self._board[row][col] = self._player
                    self._turn += 1
                    if self._player == "X":
                        self._player = "O"
                    else:
                        self._player = "X"
                    print(self._board)
                    break
                else:
                    print("Please select an empty square")
                                       

    # self.check() determines if a game has concluded
    def check(self):
        if self._turn < (self._size * 2 - 1):
            return False
        else:
            to_check = [self._board,flip_board(self._board, self._size),diags(self._board, self._size)]
            checked = list(filter(lambda x: False if x == "None" else True, map(lambda y: check_lines(y, self._size), to_check)))
            if len(checked) > 0:
                self._winner = checked[0]
                return True
            elif self._turn == (self._size * self._size) and len(checked) == 0:
                self._winner = "Tie"
                return True
            else:
                return False

    #self.winner() returns which player is the winner of the game or if there is not winner yet
    def winner(self):
        return self._winner

    #self.player() returns which player the current turn belongs to
    def player(self):
        return self._player



# *************
# GAME WRAPPER
# *************

def play_game():
    game = ""
    game_type = ""
    print("Welcome to TIC TAC TOE")
    while True:
        print("If you would like to play classic tic tac toe, enter Y.")
        print("Alternatively, for a custom game, please enter C.")
        game_type = input("Y / C: ")
        if game_type == "Y":
            game = TTT()
            break
        elif game_type == "C":
            print("here")
            while isinstance(game, str):
                size_input = input("Please enter the size of your desired custom board: ")
                try:
                    game_size = int(size_input)
                except ValueError:
                    print("Board size must be a positive integer value. Try again.")
                else:
                    if game_size < 1:
                        print("Board size must be a positive integer value. Try again.")
                    else:
                        game = TTT(game_size)
                        break
            break
        else:
            print("That is not a valid selection. Try again.")

    while game.winner() == "":
        print(game.show_board())
        print("It is {}'s turn".format(game.player()))
        game.add()
        game.check()

    print(game.show_board())
    if game.winner() == "Tie":
        print("Tie game!")
    else:
        print(game.winner() + " wins!")
    print("GAME OVER")

play_game()        
            
