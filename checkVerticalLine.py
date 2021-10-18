def check_vertical_line(player_selection, board_line):
    count = len(board_line)
    for i in range(count - 4):
        win = 0
        for j in range(5):
            if board_line[i + j] == player_selection:
                win = win + 1
        if (win == 5):
            return True

    return False

if __name__ == "__main__":
    board = ['B' for x in range(81)]
    board[5:11] = [" " for x in range(6)]
    board[45:55] = [" " for x in range(10)]
    player_selection = "B"
    board_line = [(board[0]), (board[9]), (board[18]), (board[27]), (board[36]), (board[45]), (board[54]), (board[63]), (board[72])]
    print(board_line)

    result = check_vertical_line(player_selection, board_line)

    print(result)