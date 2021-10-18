import checkVerticalLine
from checkVerticalLine import check_vertical_line

def check_vertical(player_selection, size, board):
    board_line = []
    for g in range(size):
        board_line.append(board[g * size])

    for i in range(size):
        if (check_vertical_line(player_selection, board_line)):
            return True
    return False

if __name__ == "__main__":
    size = 9
    board = ['B' for x in range(size * size)]
    board[5:11] = [" " for x in range(6)]
    board[45:55] = [" " for x in range(10)]
    print(board)
    player_selection = "B"

    result = check_vertical(player_selection, size, board)

    print(result)