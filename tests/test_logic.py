import unittest
import sys
import os

# Add src to sys.path so we can import from it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tictactoe.logic import TicTacToeGame

class TestTicTacToeLogic(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()

    def test_initial_state(self):
        for row in range(3):
            for col in range(3):
                self.assertEqual(self.game.board[row][col], ' ')
        self.assertEqual(self.game.current_player, 'X')
        self.assertIsNone(self.game.winner)
        self.assertFalse(self.game.is_draw)

    def test_valid_move(self):
        success = self.game.make_move(0, 0)
        self.assertTrue(success)
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_player, 'O')

    def test_invalid_move_occupied(self):
        self.game.make_move(0, 0)
        success = self.game.make_move(0, 0)
        self.assertFalse(success)
        self.assertEqual(self.game.board[0][0], 'X') # Should not change to O
        self.assertEqual(self.game.current_player, 'O') # Turn should not switch again

    def test_invalid_move_out_of_bounds(self):
        success = self.game.make_move(3, 3)
        self.assertFalse(success)
        self.assertEqual(self.game.current_player, 'X')

    def test_win_row(self):
        self.game.make_move(0, 0) # X
        self.game.make_move(1, 0) # O
        self.game.make_move(0, 1) # X
        self.game.make_move(1, 1) # O
        self.game.make_move(0, 2) # X wins
        
        self.assertEqual(self.game.winner, 'X')
        self.assertFalse(self.game.is_draw)

    def test_win_col(self):
        self.game.make_move(0, 0) # X
        self.game.make_move(0, 1) # O
        self.game.make_move(1, 0) # X
        self.game.make_move(1, 1) # O
        self.game.make_move(2, 0) # X wins
        
        self.assertEqual(self.game.winner, 'X')
        self.assertFalse(self.game.is_draw)

    def test_win_diagonal(self):
        self.game.make_move(0, 0) # X
        self.game.make_move(0, 1) # O
        self.game.make_move(1, 1) # X
        self.game.make_move(0, 2) # O
        self.game.make_move(2, 2) # X wins
        
        self.assertEqual(self.game.winner, 'X')
        self.assertFalse(self.game.is_draw)

    def test_draw(self):
        moves = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2)
        ]
        # X O X
        # X O X
        # O X O -> Wait, let's trace this
        # X: (0,0), (0,2), (1,0), (2,1), (2,2)
        # O: (0,1), (1,1), (1,2), (2,0)
        
        for move in moves:
            self.game.make_move(move[0], move[1])

        self.assertIsNone(self.game.winner)
        self.assertTrue(self.game.is_draw)

if __name__ == '__main__':
    unittest.main()
