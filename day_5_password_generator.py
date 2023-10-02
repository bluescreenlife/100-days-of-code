import random

# lists of characters from which to generate password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# greet user
print("Welcome to the PyPassword Generator!")

# ask user how many letters they want in PW
pw_letters = int(input("\nHow many letters would you like in the password?\n"
                    "Enter a number: "))

# ask user how many numbers they want in PW
pw_numbers = int(input("\nHow many numbers would you like in the password?\n"
                    "Enter a number: "))

# ask user how many symbols they want in PW
pw_symbols = int(input("\nHow many symbols would you like in the password?\n"
                    "Enter a number: "))

# create an empty list for the password
password_in_progress = []

# loops to append random selections to the in-progress password

for number in range(pw_letters):
    password_in_progress.append(random.choice(letters))

for number in range(pw_numbers):
    password_in_progress.append(random.choice(numbers))

for number in range(pw_symbols):
    password_in_progress.append(random.choice(symbols))

# shuffle the passowrd character list
shuffled_password = random.sample(password_in_progress, len(password_in_progress))

# join the passowrd list into one string
password = "".join(shuffled_password)

# print the final password
print(f"\nYour password is: {password}")