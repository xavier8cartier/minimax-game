import tkinter as tk
from tictactoe.gui import TicTacToeGUI

def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
