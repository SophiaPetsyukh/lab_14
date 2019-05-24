from random import choice

class Node:
    ''' Class for node representation'''
    def __init__(self, data):
        ''' Initialize a new Node. '''
        self.data = data
        self.left = None
        self.right = None


class BTree():
    ''' Class for binary tree representation'''
    def __init__(self, data=None):
        ''' Initialize a new tree object. '''
        self._root = Node(data)

    def build_tree(self):
        '''Build a tree of possible game outcome'''
        root1 = self._root

        def build_next_moves_tree(root):
            '''Helper recursive function'''
            board = root.data
            free_cords = board.free_pos()[0]
            if len(free_cords) == 0:
                pass
            else:
                if board.lastmove == 'x':
                    x_o = 'o'
                else:
                    x_o = 'x'
                move1 = choice(free_cords)
                free_cords.remove(move1)
                board1 = board.copy_board()
                board1.add_move(move1, x_o)
                root.left = Node(board1)
                if len(free_cords) == 0:
                    move2 = None
                else:
                    move2 = choice(free_cords)
                    free_cords.remove(move2)
                    board2 = board.copy_board()
                    board2.add_move(move2, x_o)
                    root.right = Node(board2)
                if move2 is not None:
                    build_next_moves_tree(root.right)
                build_next_moves_tree(root.left)
        build_next_moves_tree(root1)

    def find_best_move(self, x_o):
        '''Function for finding the best move with more winning # COMBAK: inations'''
        move1 = self._root.left
        move2 = self._root.right
        move1_res = 0
        move2_res = 0
        def check_tree(node, res):
            '''Helper recursive function'''
            if node.data is not None:
                if node.data.check_for_win(x_o):
                    res += 1
                if node.left is not None:
                    check_tree(node.left, res)
                if node.right is not None:
                    check_tree(node.right, res)
            return res
        wins1 = check_tree(move1, move1_res)
        wins2 = check_tree(move2, move2_res)
        if wins1 > wins2:
            return move1.data.lastmovecord
        else:
            return move2.data.lastmovecord
