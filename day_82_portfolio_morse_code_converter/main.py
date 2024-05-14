'''A text-based program to convert text into morse code.'''

mc_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', 
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', 
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-'
}

def eng_to_morse(eng_text:str):
    english = eng_text.upper()
    morse = ''
    for char in english:
        if char in mc_dict.keys():
            morse += (mc_dict[char] + ' ')
        elif char == ' ':
            morse += ' / '
        else:
            print(f'Received English character not represented in morse code: {char}. Please try again.')
            break
    
    return morse

if __name__ == '__main__':
    user_input_eng = input('Enter some text to convert to morse code, then press return:\n')

    morse_converted = eng_to_morse(user_input_eng)

    print(f'English: {user_input_eng}')
    print(f'Morse: {morse_converted}')