# tic-tac-toe game

SIZE = 3
MIN_TURN = SIZE * 2 - 1

def check_lines(board):
    for row in board:
        if row.count("X") == SIZE:
            return "X"
        elif row.count("O") == SIZE:
            return "O"
    return "None"

def flip_board(board):
    flipped = []
    for i in range(SIZE):
        new_row = []
        for row in board:
            new_row.append(row[i])
        flipped.append(new_row)
    return flipped

def diags(board):
    lines = [[],[]]
    for i in range(SIZE):
           lines[0].append(board[i][i])
           lines[1].append(board[i][-i - 1])
    return lines
        

class TTT:
    # TTT() produces a new tic-tac-toe board and game state
    # __init__: -> TTT
    def __init__(self):
        self._board = [[" "] * SIZE] * SIZE
        self._player = "X"
        self._turn = 0
        self._winner = ""

    #
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
        if col < 0 or col > (SIZE - 1):
            print("Please enter a valid square selection")
        elif row < 0 or row > (SIZE - 1):
            print("Please enter a valid square selection")
        else:
            if self._board[row][col] == " ":
                self._board[row][col] = self._player
                self._turn += 1
                if self._player == "X":
                    self._player = "O"
                else:
                    self._player = "X"
            else:
                print("Please select an empty square")
                

    # self.check() determines if a game has concluded
    def check(self):
        if self._turn < MIN_TURN:
            return False
        else:
            to_check = [self._board,flip_board(self._board),diags(self._board)]
            checked = list(filter(lambda x: False if x == "None" else True, map(check_lines, to_check)))
            if len(checked) > 0:
                self._winner = checked[0]
                return True
            elif self._turn == (SIZE * SIZE - 1) and len(checked) == 0:
                self._winner = "Tie"
                return True
            else:
                return False

