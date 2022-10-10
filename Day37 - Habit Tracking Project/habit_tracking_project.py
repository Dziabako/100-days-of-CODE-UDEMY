import requests
from datetime import datetime as dt

USERNAME = "dawidio"
TOKEN = "sjdfhjkbvkuyrkzhf7893bb"
GRAPH_ID = "graph2"
headers = {
    "X-USER-TOKEN": TOKEN,
}

# Wykorzystanie pixela na stronie pixe.la
pixela_endpoint = "https://pixe.la/v1/users"

# STEP 1 - Tworzenie konta na pixela / przy post uzywamy json poniewaz przesylamy dane w takiej formie (str: str)
# Wedlug dokumentacji TOKEN tworzymy sami
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# # Zwraca nam informacje czy wszystko poszlo ok w formie tekstu
# print(response.text)

# STEP 2 - Tworzenie grafu na pixela / zmienia sie tutaj endpoint wedlug dokumentacji
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Learning Graph",
#     "unit": "h",
#     "type": "float",
#     "color": "kuro",
# }
#
# # Do poprawnego dzialania wymagany jest header zawierajacy dane konta ktore zalozylismy
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# STEP 3 - Wyswietalanie grafu
# https://pixe.la/v1/users/dawidio/graphs/graph2.html

# STEP 4 - Dodawanie pixeli do grafu
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = dt.now()
date_formatted = date.strftime("%Y%m%d")

new_pixel_data = {
    "date": date_formatted,
    "quantity": input("Time: "),
}

response = requests.post(url=add_pixel_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# STEP 5 - Aktualizowanie pixeli
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_formatted}"
update_data = {
    "quantity": "7",
}
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# STEP 6 - Usuwanie pixeli
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_formatted}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
