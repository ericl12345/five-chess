def ask_board_length():
    while True:
        try:
            global boardLength
            boardLength = int(input("How big do you want the side of the board to be?"))
        except ValueError:
            print("Has to be a integer")
            boardLength = -1
        if boardLength < 5 or boardLength > 17:
            print("Has to be bigger or equal to 5 and smaller or equal to 17.")
            boardLength = -2
        if boardLength < 0:
            continue
        else:
            break
    return boardLength

if __name__ == "__main__":
    result = ask_board_length()
    print(result)