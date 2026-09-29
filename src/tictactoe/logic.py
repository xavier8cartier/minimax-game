class TicTacToeGame:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.is_draw = False

    def reset(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.is_draw = False

    def make_move(self, row, col):
        if self.winner or self.is_draw:
            return False
            
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self._check_game_state()
            if not self.winner and not self.is_draw:
                self._switch_player()
            return True
        return False

    def _switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def _check_game_state(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.winner = self.board[i][0]
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.winner = self.board[0][i]
                return
                
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.board[0][0]
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.board[0][2]
            return

        # Check for draw
        if all(cell != ' ' for row in self.board for cell in row):
            self.is_draw = True

    def get_available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def evaluate_board(self):
        # Võit (O / AI): baasskoor +1
        if self.winner == 'O':
            return 1
        # Kaotus (X / Inimene): baasskoor -1
        elif self.winner == 'X':
            return -1
        # Viik: Skoor 0
        return 0

    def clone(self):
        new_game = TicTacToeGame()
        new_game.board = [row[:] for row in self.board]
        new_game.current_player = self.current_player
        new_game.winner = self.winner
        new_game.is_draw = self.is_draw
        return new_game
