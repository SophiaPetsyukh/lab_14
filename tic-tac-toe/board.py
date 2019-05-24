class Board:
    '''Class for board representation'''
    def __init__(self):
        '''
        Initialize a new Board
        '''
        self.board = [[' ' for i in range(3)] for i in range(3)]
        self.lastmove = None
        self.lastmovecord = None

    def free_pos(self):
        '''
        Return number and list of free positions on the board
        '''
        result_lst = []
        result_num = 0
        for row in range(3):
            for el in range(3):
                if self.board[row][el] == ' ':
                    result_num += 1
                    result_lst.append((row, el))
        return result_lst, result_num

    def check_for_win(self, x_o):
        '''
        Checking board for winning combination.
        Return True if there is one and False otherwise.
        '''
        for i in range(3):
            win_h = 0
            win_v = 0
            for j in range(3):
                if self.board[i][j] == x_o:
                    win_h += 1
                if self.board[j][i] == x_o:
                    win_v += 1
            if win_h == 3 or win_v == 3:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == x_o:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == x_o:
            return True
        return False

    def check_game(self):
        '''
        Checking game status
        '''
        if self.check_for_win('x'):
            return 'You won!!! End of the game!'
        elif self.check_for_win('o'):
            return 'You lost!!! End of the game!'
        elif len(self.free_pos()) == 0:
            return 'End of the game!'
        else:
            return 'continue'

    def add_move(self, pos, x_o):
        '''
        Function for adding a move on a given position to the board
        '''
        self.board[int(pos[0])][int(pos[1])] = x_o
        self.lastmove = x_o
        self.lastmovecord = pos

    def copy_board(self):
        '''
        Function for making a copy of the board
        '''
        bcopied = Board()
        for i in range(3):
            for j in range(3):
                bcopied.board[i][j] = self.board[i][j]
        return bcopied

    def __str__(self):
        '''String representation of the board'''
        result = ''
        for i in range(3):
            for j in range(3):
                result += '|' + self.board[i][j]
            result += '|\n'
        return result
