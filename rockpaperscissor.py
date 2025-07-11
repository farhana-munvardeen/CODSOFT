import tkinter as tk
import random


user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Your Score: 0 | Computer Score: 0")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x350")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your move!", font=("Helvetica", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Helvetica", 12))
score_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=12, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=12, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=12, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(root, text="Play Again (Reset)", width=20, command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
