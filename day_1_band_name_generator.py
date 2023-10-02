#create a band name generator that gets a user's city and pet name, and returns a band name using the two

# greeting
print("Welcome to the band name generator.")

# ask user for city they grew up in
city = input("What city did you grow up in?\nCity: ")

# ask user for name of pet
pet = input("What's the name of your pet?\nPet name: ")

# combine name of city and pet, return band name
print(f"Your band name is: The {city} {pet}s.")