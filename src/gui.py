import tkinter as tk
from tkinter import messagebox
from .game_logic import check_winner, switch_player, best_move
from .model import load_trained_model, predict_best_move

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        # self.model = load_trained_model()
        self.board = [' '] * 9
        self.current_player = 'X'
        
        self.buttons = [tk.Button(self.window, text=" ", font='Arial 20', width=5, height=2, command=lambda i=i: self.make_move(i)) for i in range(9)]
        for idx, btn in enumerate(self.buttons):
            row = idx // 3
            col = idx % 3
            btn.grid(row=row, column=col)

    def make_move(self, idx):
        if self.board[idx] == ' ':
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            
            winner = check_winner(self.board)
            if winner:
                messagebox.showinfo("Ganador", f"¡El jugador {winner} ha ganado!")
                self.reset_game()
                return
            
            if ' ' not in self.board:
                messagebox.showinfo("Empate", "¡Es un empate!")
                self.reset_game()
                return
            
            self.current_player = switch_player(self.current_player)
            if self.current_player == 'O':  # Asumiendo que 'O' es la IA
                idx = best_move(self.board)
                if self.board[idx] == ' ':
                    self.make_move(idx)

    def reset_game(self):
        for i in range(9):
            self.board[i] = ' '
            self.buttons[i].config(text=' ')
        self.current_player = 'X'
        
    def run(self):
        self.window.mainloop()