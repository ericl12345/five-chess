def get_player_names():
    while True:
        global player1
        player1 = input("Enter the name of Player 1: ")
        print("\n")
        global player2
        player2 = input("Enter the name of Player 2: ")
        print("\n")
        
        if player1 != player2:
            return [player1, player2]
        else:
            print("Player names can't be the same.")
            continue

if __name__ == "__main__":
    result = get_player_names()
    print(result)