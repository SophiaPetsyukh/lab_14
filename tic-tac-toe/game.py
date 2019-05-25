from board import Board
from btree import BTree

def game():
    coordinates = ['00', '01','02', '10', '11', '12', '20', '21', '22']
    board = Board()
    print('Start of the game tic-tac-toe')
    game1 = True
    while game1:
        move = input('Enter your move (two numbers): ')
        if len(move) != 2 or move not in coordinates:
            print('Invalid input of coordinates!')
            break
        if (int(move[0]), int(move[1])) not in board.free_pos()[0]:
            print('This position is already taken!')
            break
        if board.free_pos()[1] != 0:
            board.add_move(move, 'x')
            print(board)
            if board.check_game() != 'continue':
                print(board.check_game())
                break
            tree = BTree(board)
            tree.build_tree()
            mymove = tree.find_best_move('o')
            if board.free_pos()[1] != 0:
                board.add_move(mymove, 'o')
                print(board)
        if board.check_game() != 'continue':
            print(board.check_game())
            game1 = False

if __name__ == '__main__':
    game()
