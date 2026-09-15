import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from tictactoe.logic import TicTacToeGame
from tictactoe.ai import get_best_move

if __name__ == '__main__':
    print("Benchmarking Minimax on an empty board (first move)...")
    game = TicTacToeGame()
    # The get_best_move function already prints the profile output
    # But let's trigger it for the empty board where current player is 'X', wait AI is 'O'.
    # Actually, AI is maximizing. In the empty board, it will just explore all branches.
    get_best_move(game)
