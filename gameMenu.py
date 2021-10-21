import askBoardLength
from askBoardLength import ask_board_length
import getPlayerNames
from getPlayerNames import get_player_names

def game_menu(player):
    while True:
        # Player choice Menu
        print("Turn to choose for {}" .format(player))
        print("Enter 1 for Black")
        print("Enter 2 for White")
        print("Enter 3 to Quit")
 
        # Try exception for CHOICE input
        try:
            global choice
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
        if (choice < 1 or choice > 3):
            print("Wrong Input!!! Try Again\n")
            continue
        elif choice == 1 or choice == 2:
            lengthOfBoard = ask_board_length()
        else:
            lengthOfBoard = "q"
        return [choice, lengthOfBoard]

if __name__ == "__main__":
    player = get_player_names()
    result = game_menu(player)

    print(result)