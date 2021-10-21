import getPlayerNames
from getPlayerNames import get_player_names

def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t           SCOREBOARD       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   {}\t    {}".format(players[0], score_board[players[0]]))
    print("\t   {}\t    {}".format(players[1], score_board[players[1]]))

    print("\t--------------------------------\n")

if __name__ == "__main__":
    players = get_player_names()
    score_board = {players[0]: 0, players[1]: 0}

    result = print_scoreboard(score_board)