''' a game of blackjack, with the exception that cards have equal probability
to be drawn as the game goes on (card is not removed from the deck/pool of possible cards)'''
import random

# game artwork
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# function to calculate a player's current score
def calculate_score(person: list):
    return sum(person)

# function to begin game and deal the first hand, 2 cards per person
def deal():
    print(logo)
    input("Welcome to Blackjack! Good luck!\nPress enter to deal and begin: ")
    draw_card(dealer)
    print(f"\nDealer hand: {dealer} , [hidden card]\nDealer total: {calculate_score(dealer)} + ?")
    draw_card(dealer)
    for _ in range(2):
        draw_card(player)
    print(f"\nPlayer hand: {player}\nPlayer total: {calculate_score(player)}")
    print("----------------------------------------------------------")

# function to draw a single card
def draw_card(person: list):
    draw = random.choice(cards)
    if draw == 11:
        if calculate_score(person) + draw > 21:
            draw = 1
    person.append(draw)

# function to report the current score for user, dealer, or both, by passing appropriate string
def report_score(person = None):
    if person == "player":
        print(f"\nPlayer hand: {player}\nPlayer total: {calculate_score(player)}")
    elif person == "dealer":
        print(f"Dealer hand: {dealer}\nDealer total: {calculate_score(dealer)}")
    elif person == None:
        print("\nFINAL SCORES:")
        print(f"Player hand: {player}\nPlayer total: {calculate_score(player)}")
        print(f"Dealer hand: {dealer}\nDealer total: {calculate_score(dealer)}\n")

# function to compare scores if the user or dealer does not bust (hit over 21) during game
def compare_score():
    if final_report == True:
        if calculate_score(player) <= 21 and calculate_score(dealer) <= 21:
            if calculate_score(player) > calculate_score(dealer):
                report_score()
                print("\nYOU WIN!")
            elif calculate_score(player) < calculate_score(dealer):
                print("\nYOU LOSE!")
            elif calculate_score(player) == calculate_score(dealer):
                print("\nTIE!")
        report_score()
    else:
        pass

# function for standard player turn sequence after cards have been dealt
def player_move():

    hit_or_stand = input("\nHit or stand? ").lower()

    if hit_or_stand == "hit":
        draw_card(player)
        print(f"\nNew card: {player[-1]}")
        report_score("player")
        if calculate_score(player) > 21:
            print("\nBUST! You lose.")
            final_report = False
        elif calculate_score(player) <= 21:
            player_move()
    elif hit_or_stand == "stand":
        print("\nPlayer stands.")
        input("\nPress enter to continue... ")
        print(f"\nDealer reveals: {dealer[-1]}")
        report_score("dealer")
        input("\nPress enter to continue... ")

        while calculate_score(dealer) < 17:
            draw_card(dealer)
            print(f"\nDealer draws: {dealer[-1]}")
            report_score("dealer")

        if calculate_score(dealer) > 21:
            print("\nDealer BUSTS! You win!")
            final_report = False

# main while loop to run game and offer repeat
while True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer = []
    player = []
    final_report = True

    deal()
    player_move()
    compare_score()
    print("----------------------------------------------------------")
    repeat = input(f"Would you like to play again?\nY/N: ").lower()
    if repeat == "y":
        pass
    elif repeat == "n":
        break