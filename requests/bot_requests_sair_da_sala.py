# Sai de uma sala (como o próprio usuário autenticado)
import requests

access_token = "SEU_TOKEN"
room_id = "!suaSala:matrix.org"
homeserver = "https://matrix.org"

url = f"{homeserver}/_matrix/client/v3/rooms/{room_id}/leave"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.post(url, headers=headers)
print("Você saiu da sala:", response.status_code)
