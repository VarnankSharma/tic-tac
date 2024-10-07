import tkinter as tk
from tkinter import messagebox
# Function to check if any player has won
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

# Function to handle button clicks
def button_click(row, col):
    global current_player, board

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(board[row][col] != "" for row in range(3) for col in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "❁" if current_player == "❌" else "❌"

# Function to reset the game
def reset_game():
    global current_player, board

    current_player = "❌"
    board = [["" for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title(5*" "+"𝓣𝓲𝓬 𝓣𝓪𝓬 𝓣𝓸𝓮")


# Create the game board
board = [["" for _ in range(3)] for _ in range(3)]

# Create the buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(
            window,
            text="",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda
              row=row, col=col: button_click(row, col)
        )
        button.grid(row=row, column=col, sticky="nsew") # use for arranging buttons simply use to arrange buttons acc to their relative positions
        button_row.append(button)
        button.configure(background="darkslategray2")
    buttons.append(button_row)

# Create a reset button
reset_button = tk.Button(
    window,
    text="Reset",
    font=("TIMES NEW ROMAN", 14),
    width=10,
    command=reset_game
)
reset_button.grid(row=3, columnspan=3, sticky="nsew")

# Set the initial player
current_player = "❌"

# Start the main loop
window.mainloop()