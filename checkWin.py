import checkHorizontal
from checkHorizontal import check_horizontal
import checkVertical
from checkVertical import check_vertical

def check_win(player_selection, size, board):
    if check_horizontal(player_selection, size, board):
        return True
    if check_vertical(player_selection, size, board):
        return True
    return False

if __name__ == "__main__":
    size = 7
    board = [" " for x in range(size * size)]

    a = 0
    board[13:18] = [" " for x  in range(5)]

    board[1] = "B"
    board[2] = "B"
    board[3] = "B"
    board[0] = "B"
    board[4] = "B"

    print(board)
    player_selection = "B"

    result = check_win(player_selection, size, board)

    print(result)
