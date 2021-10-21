import gameMenu
from gameMenu import game_menu
import getPlayerNames
from getPlayerNames import get_player_names

def getPlayerChoice(choice, cur_player, players):
    # Stores the choice of players
    player_choice = {'B' : "", 'W' : ""}
    # Conditions for player choice  
    if choice == 1:
        player_choice['B'] = cur_player
        if cur_player == players[0]:
            player_choice['W'] = players[1]
        else:
            player_choice['W'] = players[0]
    
    elif choice == 2:
        player_choice['W'] = cur_player
        if cur_player == players[0]:
            player_choice['B'] = players[1]
        else:
            player_choice['B'] = players[0]
    print(player_choice['B'])
    return player_choice

if __name__ == "__main__":
    player = get_player_names()
    choice = game_menu(player[0])
    cur_player = player[0]
    result = getPlayerChoice(choice[0], cur_player, player)

    print(result)