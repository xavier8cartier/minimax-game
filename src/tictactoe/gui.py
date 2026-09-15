import tkinter as tk
from tkinter import messagebox
import threading
from tkinter import messagebox
from .logic import TicTacToeGame
from .ai import get_best_move
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game = TicTacToeGame()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self._create_widgets()

    def _create_widgets(self):
        # Create a frame for the board
        self.board_frame = tk.Frame(self.root, padx=10, pady=10)
        self.board_frame.pack()

        # Create buttons
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.board_frame, text=" ", font=('Arial', 40), width=4, height=2,
                    command=lambda r=row, c=col: self._on_button_click(r, c)
                )
                button.grid(row=row, column=col, padx=2, pady=2)
                self.buttons[row][col] = button

        # Create reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self._reset_game, font=('Arial', 14))
        self.reset_button.pack(pady=10)

    def _on_button_click(self, row, col):
        if self.game.current_player != 'X' or self.game.winner or self.game.is_draw:
            return

        if self.game.make_move(row, col):
            # Update the button text
            self.buttons[row][col].config(text=self.game.board[row][col])
            
            if self._check_game_over():
                return
            
            # Trigger AI move
            self.root.after(100, self._ai_turn)

    def _ai_turn(self):
        # Run AI move calculation in a background thread
        threading.Thread(target=self._ai_worker).start()

    def _ai_worker(self):
        best_move = get_best_move(self.game)
        if best_move:
            r, c = best_move
            # Update the game and UI safely on the main thread
            self.root.after(0, self._apply_ai_move, r, c)

    def _apply_ai_move(self, r, c):
        self.game.make_move(r, c)
        self.buttons[r][c].config(text=self.game.board[r][c])
        self._check_game_over()

    def _check_game_over(self):
        if self.game.winner:
            messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
            return True
        elif self.game.is_draw:
            messagebox.showinfo("Game Over", "It's a draw!")
            return True
        return False

    def _reset_game(self):
        self.game.reset()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")
