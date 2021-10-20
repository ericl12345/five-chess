def check_draw(player_pos, size):
    if len(player_pos["B"]) + len(player_pos["W"]) == (size * size):
        return True
    return False

if __name__ == "__main__":
    size = 6
    player_pos = {"B" : ["B" for x in range(18)], "W" : ["W" for x in range(18)]}

    result = check_draw(player_pos, size)
    print(result)
