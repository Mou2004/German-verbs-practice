import tkinter as tk
from tkinter import messagebox
import random
import time

class PrepositionGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Preposition Game")

        self.prepositions = [
            {"verb": "Achten", "correct_prep": "auf", "case": "a"},
            {"verb": "Sich ärgern", "correct_prep": "über", "case": "a"},
            {"verb": "sich vorbereiten", "correct_prep": "auf", "case": "a"},
            {"verb": "Sich entschüldigen", "correct_prep": "für", "case": "a"},
            {"verb": "teilnehmen", "correct_prep": "an", "case": "d"},
            {"verb": "warten", "correct_prep": "auf", "case": "a"},
            # Add more verbs and prepositions here
        ]

        self.score = 0
        self.current_verb_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.verb_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.verb_label.pack(pady=20)

        self.prep_entry = tk.Entry(self.master, font=("Arial", 14))
        self.prep_entry.pack(pady=20)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, font=("Arial", 14))
        self.submit_button.pack(pady=20)

        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(pady=20)

        self.update_verb()

    def check_answer(self):
        current_verb = self.prepositions[self.current_verb_index]
        user_input = self.prep_entry.get().lower()
        correct_prep = current_verb["correct_prep"]
        correct_case = current_verb["case"]

        if user_input == correct_prep:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is: {correct_prep}")

        self.prep_entry.delete(0, tk.END)
        self.current_verb_index += 1
        self.update_verb()

    def update_verb(self):
        if self.current_verb_index < len(self.prepositions):
            current_verb = self.prepositions[self.current_verb_index]
            self.verb_label.config(text=f"{current_verb['verb']} - Case: {current_verb['case']}")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            messagebox.showinfo("Congratulations!", f"You completed the game.\nYour score: {self.score}")
            self.master.destroy()

def main():
    root = tk.Tk()
    app = PrepositionGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
