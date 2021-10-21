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
    size = 9
    board = [" " for x in range(size * size)]

    a = 0
    board[13:18] = [" " for x  in range(5)]

    board[5*size+a] = "B"
    board[6*size+a] = "B"
    board[7*size+a] = "B"
    board[3*size+a] = "B"
    board[4*size+a] = "B"

    print(board)
    player_selection = "B"

    result = check_win(player_selection, size, board)

    print(result)
