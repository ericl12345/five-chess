def check_horizontal_line(player_selection, board_line):
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
    player = "B"
    data = [' ' for x in range(3)]
    data.extend(['B' for x in range(5)])
    print(data)
    result = check_horizontal_line(player, data)
    print(result)