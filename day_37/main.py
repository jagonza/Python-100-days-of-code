import os
import requests
from dotenv import load_dotenv

load_dotenv()

USERNAME = "testusername20210522"
GRAPH_ID = "graph1"
TOKEN = os.getenv("PIXELA_TOKEN")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {"token": TOKEN,
               "username": USERNAME,
               "agreeTermsOfService": "yes",
               "notMinor": "yes"}

# YOU JUST NEED TO EXECUTE THIS ONCE TO CREATE THE USER
# https://pixe.la/@testusername20210522
# response = requests.post(url=pixela_endpoint", json=user_params)
# print(response.text)

graph_endpont = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_params = {"id": f"{GRAPH_ID}",
                "name": "Lecture Graph",
                "unit": "Pages",
                "type": "int",
                "color": "ichou"}
headers = {
    "X-USER-TOKEN": TOKEN
}

# YOU JUST NEED TO EXECUTE THIS ONCE TO CREATE THE GRAPH
# response = requests.post(url=graph_endpont, json=graph_params, headers=headers)
# print(response.text)


pixel_endpont = f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {"date": "20210521",
                "quantity": "20"}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=pixel_endpont, json=pixel_params, headers=headers)
# print(response.text)

update_endpont = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20210521"
update_params = {"quantity": "200"}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.put(
#     url=update_endpont, json=update_params, headers=headers)
# print(response.text)

delte_endpont = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20210521"

response = requests.delete(url=delte_endpont, headers=headers)
print(response.text)
