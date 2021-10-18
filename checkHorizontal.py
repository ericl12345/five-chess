import checkHorizontalLine
from checkHorizontalLine import check_horizontal_line

def check_horizontal(player_selection, size, board):
    for i in range(size):
        if (check_horizontal_line(player_selection, board[i * size: (i+1) * size])):
            return True
    return False

if __name__ == "__main__":
    player = "B"
    size = 10
    data = [' ' for x in range(size * size)]
    data[2:7] = ['B' for x in range(5)]
    print(data)
    result = check_horizontal(player, size, data)
    print(result)