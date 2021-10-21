import askBoardLength
from askBoardLength import ask_board_length

def print_board_line_top(cols):
    for i in range(cols):
        if i == 0:
            print("\t", end='')
        if i == cols -1:
            print("     ")
        else:
            print("     |", end='')

def print_board_line_bottom(cols, end_line):
    if end_line:
        print_board_line_top(cols)
        return

    for i in range(cols):
        if i == 0:
            print("\t", end='')
        if i == cols -1:
            print("_____")
        else:
            print("_____|", end='')

def print_board_line_mid(board_line, cols):
    for i in range(cols):
        if i == 0:
            print("\t", end='')
        if i == cols -1:
            print("  {}  ".format(board_line[i]))
        else:
            print("  {}  |".format(board_line[i]), end='')

def print_board_line(board_line, cols, end_line):
    print_board_line_top(cols)
    print_board_line_mid(board_line, cols)
    print_board_line_bottom(cols, end_line)

def print_board(size, board):
    for i in range(size):
        if i == size - 1:
            print_board_line(board[(i * size) : ((i + 1) * size)], size, True)
        else:
            print_board_line(board[(i * size) : ((i + 1) * size)], size, False)

if __name__ == "__main__":
    size = ask_board_length()
    board = [" " for x in range(size * size)]

    result = print_board(size, board)
    print(result)