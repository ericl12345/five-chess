import askBoardLength
from askBoardLength import ask_board_length

def gameMove(cur_player, values):
    # Try exception block for MOVE input
    while True:
        try:
            #print("Player ", cur_player, " turn. Which box? : ", sep='', end="")
            print("Player {} turn. Which box? : ".format(cur_player))
            inputValue = input()
            if inputValue == 'q' :
                return 'q'
            move = int(inputValue)
        except ValueError:
            print("Wrong Input!!! Try Again")
            return -1

        # Sanity check for MOVE inout
        if move < 1 or move > (boardLength * boardLength):
            print("Wrong Input!!! Try Again")
            return -2

        # Check if the box is not occupied already

        if values[move-1] != " ":
            print("Place already filled. Try again!!")
            return -3
        return move

if __name__ == "__main__":
    boardLength = ask_board_length()
    cur_player = "B"
    values = [" " for x in range(boardLength * boardLength)]

    result = gameMove(cur_player, values)
    print(result)