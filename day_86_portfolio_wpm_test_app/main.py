import tkinter as tk
from tkinter import IntVar, ttk
import threading
import time
import difflib

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.text_start = "Test your typing speed in 1 minute. Press enter at the end of each sentence. Enter \"start\" to begin."
        self.game_length = IntVar(value=60)

        self.display_idx = 0
        self.test_text_1m = ["The quick brown fox jumps over the lazy dog.", 
                            "This sentence includes every letter of the alphabet, making it a favorite among typists.", 
                            "Practicing with such a phrase can help improve your typing speed and accuracy.", 
                            "To become a proficient typist, it is essential to maintain proper posture and hand positioning.",
                            "Remember to keep your fingers on the home row keys and use all ten fingers while typing.",
                            "Regular practice and patience are key to mastering this valuable skill.",
                            "Keep challenging yourself with different texts to enhance your typing abilities."]
        
        self.completed_text_list = []
        self.user_entry_list = []
        self.game_on = False
        self.time_out = False

        # configure window
        self.title("FastFingers: A Typing Speed Test")
        self.geometry("700x300")

        # label
        self.display_label = ttk.Label(self, text=self.text_start)
        self.display_label.pack(side="top", padx=(10,10), expand=True)

        self.countdown_label = ttk.Label(self, text=float(self.game_length.get()))
        self.countdown_label.pack()

        # entry
        self.user_entry = ttk.Entry(self, width=400)
        self.user_entry.pack(side="bottom", padx=(10,10), expand=True)
        self.user_entry.bind('<Return>', self.user_return)
        self.user_entry.focus()

    def user_return(self, event: tk.Event):
        '''Logic flow for appending user's test text depending on game state.'''
        if not self.game_on and self.user_entry.get().lower().strip() == "start":
            self.game_on = True
            timer_thread = threading.Thread(target=self.run_timer)
            timer_thread.start()
            self.update_prompt()
        elif self.game_on and not self.time_out:
            self.user_entry_list.append(self.user_entry.get())
            self.completed_text_list.append(self.display_label["text"])
            self.update_prompt()
        elif not self.game_on and not self.time_out:
            self.display_label.config(text="Reminder: type \"start\" to begin.")
            self.user_entry.delete(0, "end")

        self.user_entry.delete(0, "end")
        self.user_entry.focus()

    def update_prompt(self):
        '''Update display label to the next string in the list.'''
        self.display_label.config(text=self.test_text_1m[self.display_idx])
        self.display_idx += 1

    def calculate_accuracy(self):
        '''Calculates accuracy ratio and WPM.'''
        original = " ".join(self.completed_text_list)
        typed = " ".join(self.user_entry_list)
        print(f"Comparing completed original text with typed:\nOriginal: {original}\nTyped: {typed}")

        matcher = difflib.SequenceMatcher(None, original, typed, False)
        ratio = matcher.ratio()

        num_orig_words = len(original.split(" "))
        num_typed_words = len(typed.split(" "))

        wpm = num_typed_words * ratio

        print(f"\nAccuracy ratio: {ratio}")
        return ratio, wpm

    def run_timer(self):
        # runs on own thread once game starts
        clock = self.game_length.get()
        while self.game_on and clock > 0:
            time.sleep(1)
            clock -= 1
            self.countdown_label.config(text=str(clock))

        # steps to end game
        self.game_on, self.time_out = False, True
        self.user_entry.config(state="disabled")
        ratio, wpm = self.calculate_accuracy()
        self.display_label.config(text=f"Time's Up! Accuracy: {ratio * 100:.2f}% | WPM: {wpm:.2f}")


if __name__ == "__main__":
    app = App()
    app.mainloop()