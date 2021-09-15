import sys
import GuessingGame

default=100
if len(sys.argv)>1:
    GuessingGame.guessing_game(int(sys.argv[1]))
else:
    GuessingGame.guessing_game(default)