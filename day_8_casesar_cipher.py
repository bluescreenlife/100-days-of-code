'''simple program to encrypt and decrypt plain text by shifting by a user-defined amount
    to a different letter in the alphabet, and back'''

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# main function to encrypt or decrypt string
def caesar(plain_text, shift_amount, shift_direction):

    # string to be built from new characters
    adjusted_text = ""

    # reverse the shift amount for decryption
    if shift_direction == "decrypt":
        shift_amount *= -1

    ignore_char = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    # loop to convert each character in string to new character via index in alphabet list above
    for char in plain_text:
        if char in ignore_char:
            adjusted_text += char
        else:
            index = alphabet.index(char)
            new_index = index + shift_amount

            # adjusting for overflow past 26th letter of alphabet or lower than 0
            if new_index >= 26:
                new_index -= 26
            elif new_index <= -1:
                new_index += 26

            # build conversion string
            adjusted_text += alphabet[new_index]

    # display result to user, pass back string for easy re-use/re-conversion
    print(f"Your adjusted text is: {adjusted_text}")
    return adjusted_text

# start with super cool artwork
print(logo)

# loop to offer repeating until user opts-out
while True:
    direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_amount=shift, shift_direction=direction)

    repeat = input("\nCipher again (Y/N)? ").lower()
    if repeat == 'n':
        break