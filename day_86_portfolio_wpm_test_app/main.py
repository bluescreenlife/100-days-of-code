import tkinter as tk
from tkinter import IntVar, ttk
# from typing import Callable, Any

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.text_start = "Test your typing speed in 1 minute. Press enter at the end of each sentence. Enter \"start\" to begin."
        self.countdown = IntVar(value=60)

        self.display_idx = 0
        self.text_list_1m = ["The quick brown fox jumps over the lazy dog.", 
                            "This sentence includes every letter of the alphabet, making it a favorite among typists.", 
                            "Practicing with such a phrase can help improve your typing speed and accuracy.", 
                            "To become a proficient typist, it is essential to maintain proper posture and hand positioning.",
                            "Remember to keep your fingers on the home row keys and use all ten fingers while typing.",
                            "Regular practice and patience are key to mastering this valuable skill.",
                            "Keep challenging yourself with different texts to enhance your typing abilities."]
        
        self.user_entry_list = []

        # configure window
        self.title("FastFingers: A Typing Speed Test")
        self.geometry("700x300")

        # label
        self.display_label = ttk.Label(self, text=self.text_start)
        self.display_label.pack(side="top", padx=(10,10), expand=True)

        self.countdown_label = ttk.Label(self, text=float(self.countdown.get()))
        self.countdown_label.pack()

        # entry
        self.user_entry = ttk.Entry(self, width=400)
        self.user_entry.pack(side="bottom", padx=(10,10), expand=True)
        self.user_entry.bind('<Return>', self.user_return)
        self.user_entry.focus()

    def user_return(self, event: tk.Event):
        '''Add entry contents to list of user-entered strings.'''
        self.user_entry_list.append(self.user_entry.get())
        self.user_entry.delete(0, "end")
        self.user_entry.focus()

        self.update_prompt()


    def update_prompt(self):
        '''Update display label to the next string in the list.'''
        self.display_label.config(text=self.text_list_1m[self.display_idx])
        self.display_idx += 1

    def calculate_accuracy(self):
        pass
    


if __name__ == "__main__":
    app = App()
    app.mainloop()