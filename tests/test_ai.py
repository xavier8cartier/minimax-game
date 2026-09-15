import unittest
import sys
import os

# Add src to sys.path so we can import from it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tictactoe.logic import TicTacToeGame
from tictactoe.ai import get_best_move

class TestTicTacToeAI(unittest.TestCase):
    def test_ai_blocks_win(self):
        game = TicTacToeGame()
        # X is about to win on top row
        game.make_move(0, 0) # X
        game.make_move(1, 0) # O
        game.make_move(0, 1) # X
        
        # AI's turn (O)
        best_move = get_best_move(game)
        self.assertEqual(best_move, (0, 2)) # O should block X



    def test_ai_takes_win_properly(self):
        game = TicTacToeGame()
        game.make_move(0, 1) # X
        game.make_move(0, 0) # O
        game.make_move(1, 1) # X
        game.make_move(1, 0) # O
        game.make_move(0, 2) # X
        
        # O is at 0,0 and 1,0. Needs 2,0 to win.
        # Let's just set the board manually for testing
        game = TicTacToeGame()
        game.board = [
            ['X', 'X', ' '],
            ['O', 'O', ' '],
            [' ', ' ', ' ']
        ]
        game.current_player = 'O'
        best_move = get_best_move(game)
        self.assertEqual(best_move, (1, 2)) # O takes the win

if __name__ == '__main__':
    unittest.main()
