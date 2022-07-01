# tic-tac-toe game

import copy


def check_lines(board, size):
    for row in board:
        if row.count("X") == size:
            return "X"
        elif row.count("O") == size:
            return "O"
    return "None"

def flip_board(board, size):
    flipped = []
    for i in range(size):
        new_row = []
        for row in board:
            new_row.append(row[i])
        flipped.append(new_row)
    return flipped

def diags(board, size):
    lines = [[],[]]
    for i in range(size):
           lines[0].append(board[i][i])
           lines[1].append(board[i][-i - 1])
    return lines

def gen_board(size):
    board = []
    empty_row = [" "] * size
    for i in range(size):
        board.append(copy.deepcopy(empty_row))
    return board
        

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
    
    '''
        0   1   2
         
    0   X | O | X 
       --- --- ---
    1   O | X | O
       --- --- ---
    2   X | O | X
    
    '''

    # self.add(self, col, row) enters the player's move into the board if it is valid
    def add(self, col, row):
        if col < 0 or col > (self._size - 1):
            print("Please enter a valid square selection")
        elif row < 0 or row > (self._size - 1):
            print("Please enter a valid square selection")
        else:
            if self._board[row][col] == " ":
                self._board[row][col] = self._player
                self._turn += 1
                if self._player == "X":
                    self._player = "O"
                else:
                    self._player = "X"
                print(self._board)
            else:
                print("Please select an empty square")
                

    # self.check() determines if a game has concluded
    def check(self):
        if self._turn < (self._size * 2 - 1):
            return False
        else:
            to_check = [self._board,flip_board(self._board),diags(self._board)]
            checked = list(filter(lambda x: False if x == "None" else True, map(check_lines, to_check)))
            if len(checked) > 0:
                self._winner = checked[0]
                return True
            elif self._turn == (self._size * self._size - 1) and len(checked) == 0:
                self._winner = "Tie"
                return True
            else:
                return False

