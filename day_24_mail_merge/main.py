# Create a letter using starting_letter.txt 
# For each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
# Assemble list of names from invited_names.txt

with open('./Input/Names/invited_names.txt') as names_file:
    unedited_names = names_file.readlines()

names = []

for name in unedited_names:
    names.append(name.strip())

with open('./Input/Letters/starting_letter.txt') as template_file:
    template_lines = template_file.readlines()

for name in names:
    invite_content = template_lines.copy()
    invite_content[0] = invite_content[0].replace("[name]", f'{name}')

    with open(f'./Output/ReadyToSend/{name}.txt', mode='w') as new_invitation:
        for line in invite_content:
            new_invitation.write(line)