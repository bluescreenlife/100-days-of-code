'''program to translate any word into NATO phonetic spelling, using csv data'''
import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_alpha_df = pandas.read_csv('./nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for (index, row) in nato_alpha_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Enter a word to convert to NATO phonetic spelling: ")
translation = [phonetic_dict[char] for char in input_word.upper()]
print(f"Translation: {' '.join(translation)}")