'''Automated birthday greeting emailer. Birthdays from birthdays.csv 
are checked, and any on the current date have an email sent to the
address listed with the person's name replaced in the template.'''
import smtplib
import pandas
import datetime as dt
from random import choice

# set values accordingly for sender
SENDER_EMAIL_ADDR ='youremail@gmail.com'
SENDER_PW ='yourkey'
SENDER_SERVER = 'smtp.gmail.com'
SENDER_PORT = 587
SENDER_NAME = 'yourname' # to be written as from in email

def get_birthdays():
    '''Checks list of birthdays, and if it is someone's birthday, returns their name and email address, otherwise returns False.'''
    birthdays_df = pandas.read_csv('./birthdays.csv')
    birthdays_dict = birthdays_df.to_dict(orient='records')
    today_month = dt.datetime.now().month
    today_day = dt.datetime.now().day
    today_birthdays = []

    for person in birthdays_dict:
        if person['month'] == today_month and person['day'] == today_day:
            today_birthdays.append(person)
        
    for birthday in today_birthdays:
        print(f"Birthday today: {birthday['name']}: {birthday['email']}\n")
    return today_birthdays

def get_birthday_message(recipient_name):
    '''Takes a name, returns one of 3 birthday messages, addressed to name.'''
    templates = ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt']
    random_template = choice(templates)

    with open(random_template, 'r') as birthday_letter:
        birthday_letter_list = birthday_letter.readlines()
        birthday_letter_list[0] = birthday_letter_list[0].replace("[NAME]", recipient_name.title())
        birthday_letter_list[6] = birthday_letter_list[6].replace("[SENDER]", SENDER_NAME)
        letter_to_send = "".join(birthday_letter_list)
        print(f"Message to be sent:\n{letter_to_send}\n")
        return letter_to_send

def send_email(recipient_address, message):
    '''Takes an email address and a message to send, and sends it.
    Requires sender email and password to be specified within function first.'''

    with smtplib.SMTP(SENDER_SERVER, port=SENDER_PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL_ADDR, password=SENDER_PW)
        connection.sendmail(
            from_addr=SENDER_EMAIL_ADDR, 
            to_addrs=recipient_address, 
            msg=f"Subject:Happy Birthday!\n\n{message}")
    
    print(f"\nBirthday wishes to {recipient_address} successfully sent.")

if __name__ == "__main__":
    birthdays = get_birthdays() # list containing dict for each birthday (name and email)

    if get_birthdays():
        for birthday in birthdays:
            birthday_message = get_birthday_message(birthday['name'])
            send_email(birthday['email'], birthday_message)