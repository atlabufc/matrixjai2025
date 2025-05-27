# Lista salas públicas disponíveis no homeserver
import requests

homeserver = "https://matrix.org"
url = f"{homeserver}/_matrix/client/v3/publicRooms"

response = requests.get(url)
print(response.json())  # Exibe a lista de salas públicas
