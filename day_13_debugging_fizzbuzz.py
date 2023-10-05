'''A debugging exercise'''

# # code to debug
# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# debugged code
target = int(input())
for number in range(1, (target + 1)): # placed target + 1 in parentheses
    if number % 3 == 0 and number % 5 == 0: # fixed indentation, changed or to and
        print("FizzBuzz") # fixed indentation
    elif number % 3 == 0: # made if into elif, fixed indentation
        print("Fizz") # fixed indentation
    elif number % 5 == 0: # made if into elif, fixed indentation
        print("Buzz") # fixed indenation
    else: # fixed indetnation
        print(number) # fixed indenatiion, removed unnecessary brackets