import getPlayerNames
from getPlayerNames import get_player_names
import askBoardLength
from askBoardLength import ask_board_length
import gameMenu
from gameMenu import game_menu
import printScoreBoard
from printScoreBoard import print_scoreboard
import getPlayerChoice
from getPlayerChoice import getPlayerChoice
import singleGame
from singleGame import single_game
import printBoard
from printBoard import print_board

if __name__ == "__main__":
    players = get_player_names()
    boardLength = ask_board_length()
    cur_player = players[0]
    score_board = {players[0]: 0, players[1]: 0}

    while True:
        player_pos = {"B": [], "W": []}
        values = [' ' for x in range(boardLength * boardLength)]
        choice = game_menu(cur_player)

        if choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        player_choice = getPlayerChoice(choice, cur_player, players)

        # Stores the winner in a single game of wu zi qi
        if choice == 1:
            choice_1 = "B"
            winner = single_game(cur_player ,choice_1, boardLength, values, player_pos)
        else:
            choice_1 = "W"
            winner = single_game(cur_player, choice_1, boardLength, values, player_pos)

        # Edits the scoreboard according to the winner
        if winner == 'D':
            print("Draw!")
        elif winner == 'Q':
            print("Quited!")
        else:
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
        
        print("Final board:")
        print_board(boardLength, values)
        print_scoreboard(score_board)
        # Switch player who chooses B or W
        if cur_player == players[0]:
            cur_player = players[1]
        else:
            cur_player = players[0]