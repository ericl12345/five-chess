import checkVerticalLine
from checkVerticalLine import check_vertical_line

def check_vertical(player_selection, size, board):
    board_line = []

    for i in range(size):
        for g in range(size):
            board_line.append(board[g * size + i])
        
        if (check_vertical_line(player_selection, board_line)):
            return True
    return False

if __name__ == "__main__":
    size = 9
    board = [" " for x in range(size * size)]

    a = 7
    board[0+a] = "B"
    board[size+a] = "B"
    board[2*size+a] = "B"
    board[3*size+a] = "B"
    board[4*size+a] = "B"

    print(board)
    player_selection = "B"

    result = check_vertical(player_selection, size, board)

    print(result)
