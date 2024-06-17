import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import os

# Function to load images safely
def load_image(file_path, size):
    try:
        image = Image.open(file_path)
        image = image.resize(size)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Error", f"Error loading image {file_path}: {e}")
        root.quit()

# Initialize the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("800x400")

# Ensure the script is running in the correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Load images for Rock, Paper, Scissors
rock_img = load_image("images/rock.jpg", (100, 100))
paper_img = load_image("images/paper.jpg", (100, 100))
scissors_img = load_image("images/scissors.jpg", (100, 100))

# Initialize scores
user_score = 0
computer_score = 0

# Title of the game
title = tk.Label(root, text='ROCK PAPER SCISSOR GAME', font=("Helvetica", 20, "bold"), bg="#ff9cce")
title.pack(pady=10)

# Buttons for Rock, Paper, Scissors
rock_button = tk.Button(root, image=rock_img, command=lambda: play("rock"))
rock_button.pack(side=tk.LEFT, padx=20, pady=20)

paper_button = tk.Button(root, image=paper_img, command=lambda: play("paper"))
paper_button.pack(side=tk.LEFT, padx=20, pady=20)

scissors_button = tk.Button(root, image=scissors_img, command=lambda: play("scissors"))
scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

# Labels for displaying choices and scores
user_choice_label = tk.Label(root, text="Your choice:", font=("Helvetica", 14))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer's choice:", font=("Helvetica", 14))
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Helvetica", 16))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14))
score_label.pack(pady=10)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

# Function to update the game state
def play(choice):
    user_choice = choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
    
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Result: {result}")
    
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

# Function to ask user if they want to play again
def play_again():
    response = messagebox.askyesno("Play Again", "Do you want to play again?")
    if response:
        global user_score, computer_score
        user_score = 0
        computer_score = 0
        score_label.config(text="Score - You: 0, Computer: 0")
        user_choice_label.config(text="Your choice:")
        computer_choice_label.config(text="Computer's choice:")
        result_label.config(text="Result: ")
    else:
        root.quit()

# Button to play again
play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
