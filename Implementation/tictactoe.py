'''''''#  The code Below is a code for implementing a TIC_TAC_TOE game using OOPS and python.'''

# CODE:


ALL_SPACES = list('123456789')  # The keys for a TTT board.
X, O, BLANK = 'X', 'O', ' '  # Constants for string values.


def main():
    '''Runs a game of tic-tac-toe'''

    print('Welcome to tic-tac-toe!')
    game_board = TTTBoard()  # Create a TTT board object.
    current_player, next_player = X, O  # X goes first, O goes next.

    while True:
        print(game_board.get_board_str())  # Display the board on the screen.

        # Keep asking the player until they enter a number 1-9:
        move = None
        while not game_board.is_valid_space(move):
            print(f'What is {current_player}\'s move? (1-9)')
            move = input()
        game_board.update_board(move, current_player)  # Make the move.

        # Check if the game is over:
        if game_board.is_winner(current_player):  # First check for victory.
            print(game_board.get_board_str())
            print(current_player + ' has won the game!')
            break


        elif game_board.is_board_full():  # Next check for a tie.
            print(game_board.get_board_str())
            print('The game is a tie!')
            break

        current_player, next_player = next_player, current_player  # Swap turns.
    print('Thanks for playing!')

    # Implementing OOPS concepts by the use of a Class


class TTTBoard:
    '''Contains all the functions reqired to perform the operation'''
    def __init__(self, use_pretty_board=False, use_logging=False):  # Constructor
        """Create a new, blank tic tac toe board."""
        self.use_logging = use_logging
        self.use_pretty_board = use_pretty_board
        self._spaces = {}  # The board is represented as a Python dictionary.
        for space in ALL_SPACES:
            self._spaces[space] = BLANK  # All spaces start as blank.

    def get_board_str(self):
        '''Return a text-representation of the board'''
        return f'''
      {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}  1 2 3
      -+-+-
      {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}  4 5 6
      -+-+-
      {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}  7 8 9'''

    def is_valid_space(self, space):
        '''Returns True if the space on the board is a valid space number
        # and the space is blank'''
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def is_winner(self, player):
        '''Return True if player is a winner on this TTTBoard'''
        s_arr, p_arr = self._spaces, player  # Shorter names as "syntactic sugar".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((s_arr['1'] == s_arr['2'] == s_arr['3'] == p_arr) or  # Across the top
                (s_arr['4'] == s_arr['5'] == s_arr['6'] == p_arr) or  # Across the middle
                (s_arr['7'] == s_arr['8'] == s_arr['9'] == p_arr) or  # Across the bottom
                (s_arr['1'] == s_arr['4'] == s_arr['7'] == p_arr) or  # Down the left
                (s_arr['2'] == s_arr['5'] == s_arr['8'] == p_arr) or  # Down the middle
                (s_arr['3'] == s_arr['6'] == s_arr['9'] == p_arr) or  # Down the right
                (s_arr['3'] == s_arr['5'] == s_arr['7'] == p_arr) or  # Diagonal
                (s_arr['1'] == s_arr['5'] == s_arr['9'] == p_arr))  # Diagonal

    def is_board_full(self):
        '''Return True if every space on the board has been taken'''
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # If a single space is blank, return False.
        return True  # No spaces are blank, so return True.

    def update_board(self, space, player):
        '''Sets the space on the board to player'''
        self._spaces[space] = player

    def print_mark(self):
        '''Used to place the mark 0 on the board'''
        return O

    def print_markx(self):
        '''Used to place the mark X on the board'''
        return X



class TTiBoard(TTTBoard):  # Derieved Class or Inherited class
    '''This is the derieved class of the TTTBoard class'''
    def __init__(self):
        self.posn = self

        # INVOKING the CONSTRUCTOR of the PARENT class
        TTTBoard.__init__(self, use_pretty_board=False, use_logging=False)




# Call main() if this module is run, but not when imported.


if __name__ == '__main__':
    main()
