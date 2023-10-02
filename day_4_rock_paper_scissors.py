import random

class RPS_Game:
    def __init__(self):
        self.rps_dict = {"rock" : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
                    "paper" : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
                    "scissors" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''                 
                    }
        
        self.rock = self.rps_dict["rock"]
        self.paper = self.rps_dict["paper"]
        self.scissors = self.rps_dict["scissors"]

        self.pc_choice = random.choice(list(self.rps_dict.keys()))
        self.user_choice = self.get_user_choice()

        self.decide_winner()

    def get_user_choice(self):
        return input("Rock, paper, or scissors?\nChoose: ").lower()
    
    def decide_winner(self):
        if self.pc_choice == "rock":
            if self.user_choice == "rock":
                print(f"You chose:\n{self.rock}\nPC chose:\n{self.rock}\n")
                print("DRAW.")
            if self.user_choice == "paper":
                print(f"You chose:\n{self.paper}\nPC chose:\n{self.rock}\n")
                print("YOU WIN.")
            if self.user_choice == "scissors":
                print(f"You chose:\n{self.scissors}\nPC chose:\n{self.rock}\n")
                print("YOU LOSE.")
        elif self.pc_choice == "paper":
            if self.user_choice == "rock":
                print(f"You chose:\n{self.rock}\nPC chose:\n{self.paper}\n")
                print("YOU LOSE.")
            if self.user_choice == "paper":
                print(f"You chose:\n{self.paper}\nPC chose:\n{self.paper}\n")
                print("DRAW.")
            if self.user_choice == "scissors":
                print(f"You chose:\n{self.scissors}\nPC chose:\n{self.paper}\n")
                print("YOU WIN.")
        elif self.pc_choice == "scissors":
            if self.user_choice == "rock":
                print(f"You chose:\n{self.rock}\nPC chose:\n{self.scissors}\n")
                print("YOU WIN.")
            if self.user_choice == "paper":
                print(f"You chose:\n{self.paper}\nPC chose:\n{self.scissors}\n")
                print("YOU LOSE.")
            if self.user_choice == "scissors":
                print(f"You chose:\n{self.scissors}\nPC chose:\n{self.scissors}\n")
                print("DRAW.")
        else:
            print("Unknown error.")
        
if __name__ == "__main__":
    game = RPS_Game()