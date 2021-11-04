import printBoard
from printBoard import print_board
import gameMove
from gameMove import gameMove
import checkWin
from checkWin import check_win
import checkDraw
from checkDraw import check_draw
import gameMenu
from gameMenu import game_menu
import getPlayerNames
from getPlayerNames import get_player_names
import getPlayerChoice
from getPlayerChoice import getPlayerChoice
import askBoardLength
from askBoardLength import ask_board_length
import printScoreBoard
from printScoreBoard import print_scoreboard

def single_game(cur_player, player_selection, boardLength):

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_board(boardLength, values)

        move = gameMove(player_selection, values, boardLength)
        if move == "q":
            return "Q"
        elif move < 0:
            continue

        values[move-1] = player_selection
        player_pos[player_selection].append(move)
        
        checkWin = check_win(player_selection ,boardLength, values)
        checkDraw = check_draw(player_pos ,boardLength)
        if checkWin == True:
            print_board(boardLength, values)
            print("Player {} has won the game!!".format(cur_player))
            print("\n")
            return player_selection
        elif checkDraw == True:
            print_board(boardLength, values)
            print("\n")
            return "D"

        # Switch player moves
        if player_selection == 'B':
            player_selection = 'W'
        else:
            player_selection = 'B'

if __name__ == "__main__":
    players = get_player_names()
    boardLength = ask_board_length()
    cur_player = players[0]
    player_pos = {"B": [], "W": []}
    score_board = {players[0]: 0, players[1]: 0}
    values = [' ' for x in range(boardLength * boardLength)]

    while True:

        choice = game_menu(cur_player)

        if choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        player_choice = getPlayerChoice(choice, cur_player, players)

        # Stores the winner in a single game of wu zi qi
        if choice == 1:
            choice_1 = "B"
            winner = single_game(cur_player ,choice_1, boardLength)
        else:
            choice_1 = "W"
            winner = single_game(cur_player, choice_1, boardLength)

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