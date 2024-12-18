import requests
import datetime
pixela_url = "https://pixe.la/v1/users"
profile_page = "https://pixe.la/@sampony"
USER_NAME = "sampony"
TOKEN = "hdidudhdhiddiddidi"

# Create account---------------------------------------------------------------------------
user_parameter = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}
# response = requests.post(url=pixela_url, json=user_parameter)
# print(response.text)

# Create a graph---------------------------------------------------------------------------
graph_endpoint = f"{pixela_url}/{USER_NAME}/graphs"

# Config a graph-----------------------------------
graph_config = {
    'id': "graph1",
    'name': "Studying English",
    'unit': "Horas",
    'type': "float",
    'color': "kuro"
}
header = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

# Posting a pixel quantity---------------------------------------------------------------------------
# Ex endpoint:/v1/users/<username>/graphs/<graphID>
post_pixel_endpoint = f"{pixela_url}/{USER_NAME}/graphs/{graph_config['id']}"
now = datetime.date.today()
today = now.strftime("%Y%m%d")

pixel_config = {
    'date': today,
    'quantity': "0.4",
}

response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=header)
print(response.text)