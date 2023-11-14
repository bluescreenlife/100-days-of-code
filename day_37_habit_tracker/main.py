'''Habit tracker input and editing via Pixela. This one was written for daily meditation habit.'''
import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = 'bluescreenlife91'
TOKEN = "d9hj37c5s0a"

today_date = datetime.now().strftime("%Y%m%d")

# authentication using HTTP header
headers = {
    "X-USER-TOKEN": TOKEN,
}

# ------ user creation ------ #
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ------ graph creation ------ #
graph_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id" : "graph1",
#     "name" : "Meditation Graph",
#     "unit" : "minute",
#     "type" : "int",
#     "color" : "sora"
# }

# requests.post(url=graph_creation_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ------ add/update/delete a pixel ------ #
meditation_graph = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

def add_pixel():
    add_pixel_data = {
        "date" : today_date,
        "quantity" : input("How many minutes did you meditate today? ")
    }

    response = requests.post(url=meditation_graph, json=add_pixel_data, headers=headers)
    print(response.text)
    
def update_pixel():
    update_pixel = input("Enter date of pixel to update (yyyyMMdd): ")

    update_pixel_data = {
        "quantity" : input("Enter updated number of minutes: ")
    }

    response = requests.put(url=f"{meditation_graph}/{update_pixel}", json=update_pixel_data, headers=headers)
    print(response.text)


def delete_pixel():
    delete_pixel = input("Enter date of pixel to delete (yyyyMMdd): ")

    response = requests.delete(url=f"{meditation_graph}/{delete_pixel}", headers=headers)
    print(response.text)

# ------ update graph ------ #

# graph_config = {
#     "unit" : "minutes"
# }
# response = requests.put(url=meditation_graph, json=graph_config, headers=headers)
# response.raise_for_status()
# print(response.text)

# ------ main menu ------ #
selection = int(input("What would you like to do?\n\n1. Add today's pixel\n2. Update a pixel\n3. Delete a pixel\n\nEnter a number: "))

if selection == 1:
    add_pixel()
elif selection == 2:
    update_pixel()
elif selection == 3:
    delete_pixel()