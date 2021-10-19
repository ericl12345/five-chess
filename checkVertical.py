import checkVerticalLine
from checkVerticalLine import check_vertical_line

def check_vertical(player_selection, size, board):

    for i in range(size):
        board_line = []
        for g in range(size):
            board_line.append(board[g * size + i])
        
        if (check_vertical_line(player_selection, board_line)):
            return True
    return False

if __name__ == "__main__":
    size = 9
    board = [" " for x in range(size * size)]

    a = 0
    board[5*size+a] = "B"
    board[6*size+a] = "B"
    board[7*size+a] = "B"
    board[3*size+a] = "B"
    board[4*size+a] = "B"

    print(board)
    player_selection = "B"

    result = check_vertical(player_selection, size, board)

    print(result)
