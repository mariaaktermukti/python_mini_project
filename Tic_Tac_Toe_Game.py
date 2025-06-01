import tkinter as tk
from tkinter import messagebox

def check_winner():
    # All possible winning combinations
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in combos:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != ""):
            # Highlight winning buttons
            for index in combo:
                buttons[index].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
            return

    # If all buttons are filled and no winner, it's a draw
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        root.quit()

def button_click(index):
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player.get()
        check_winner()
        toggle_player()

def toggle_player():
    if current_player.get() == "X":
        current_player.set("O")
    else:
        current_player.set("X")
    label.config(text=f"Player {current_player.get()}'s turn")

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Track current player
current_player = tk.StringVar(value="X")

# Create 3x3 grid of buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Label to show whose turn it is
label = tk.Label(root, text=f"Player {current_player.get()}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the GUI loop
root.mainloop()
