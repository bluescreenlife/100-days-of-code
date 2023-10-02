''' simple program to simulate a silent auction'''
from replit import clear

# empty dict to store bidder name and bid
bids = {}

# gavel artwork
art = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# print art and greet user
print(art)
print("Welcome to the silent auction!")

# loop to allow bid entry
while True:
    name = input("Enter your name: ").title()
    bid = input("Enter your bid: ")

    bids[name] = bid

    repeat = input("Thank you for your bid. Is there another bidder? ").upper()
    if repeat == "Y" or repeat == "YES":
        clear()
    elif repeat == "N" or repeat == "NO":
        break

# get value of highest bid
high_bidder = max(bids.values())

# determine name of highest bidder and announce
for key, value in bids.items():
    if value == high_bidder:
        print(f"\nThe winning bidder is {key}!")