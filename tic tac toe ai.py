import tkinter as tk
from tkinter import messagebox

board = [['' for _ in range(3)] for _ in range(3)]
player = "X"  

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            return board[row][0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    # Check for a tie
    for row in board:
        if '' in row:
            return None  
    return 'Tie'

def minimax(board, depth, is_maximizing):
    result = check_winner()
    if result == 'X':
        return -1  # Player wins
    if result == 'O':
        return 1  # AI wins
    if result == 'Tie':
        return 0  # It's a tie

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)

    if move:
        board[move[0]][move[1]] = 'O'
        buttons[move[0]][move[1]].config(text='O')
        check_game_status()

def check_game_status():
    winner = check_winner()
    if winner == "X":
        messagebox.showinfo("Tic Tac Toe", "You win!")
        root.quit()
    elif winner == "O":
        messagebox.showinfo("Tic Tac Toe", "AI wins!")
        root.quit()
    elif winner == "Tie":
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        root.quit()

def player_move(row, col):
    if board[row][col] == '':
        board[row][col] = 'X'
        buttons[row][col].config(text='X')
        check_game_status()
        best_move()

# Tkinter setup for game UI
root = tk.Tk()
root.title("Tic Tac Toe - Minimax AI")

buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('normal', 40), width=5, height=2,
                                  command=lambda row=i, col=j: player_move(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
