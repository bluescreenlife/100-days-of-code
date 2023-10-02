# get info from user
total = float(input("What was the bill total? "))
num_people = float(input("How many people are splitting the bill? "))
tip_percentage = None

# get service level and assign tip percentage
while tip_percentage == None:
    service_level = input("How was the service?\nBad: 10% | OK: 15% | Good: 20%\nService level: ").lower()

    if service_level == "good":
        tip_percentage = 0.2
    elif service_level == "ok":
        tip_percentage = 0.15
    elif service_level == "bad":
        tip_percentage = 0.1
    else:
        print("Invalid input. Please enter \"good\", \"OK\", or \"bad\".")

# calculate tip
individual_total = (total / num_people)
tip_amount = individual_total * tip_percentage
grand_total = (individual_total + tip_amount)

# print tip and total with tip
print(f"Your total: {round(individual_total, 2)}\nTip: {round(tip_amount, 2)}\nTotal with tip: {round(grand_total, 2)}")