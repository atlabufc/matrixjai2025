# Envia convite para um usuário ingressar em uma sala
import requests

access_token = "SEU_TOKEN"
room_id = "!suaSala:matrix.org"
homeserver = "https://matrix.org"
invitee = "@usuario:matrix.org"

url = f"{homeserver}/_matrix/client/v3/rooms/{room_id}/invite"
headers = {"Authorization": f"Bearer {access_token}"}
payload = {"user_id": invitee}

response = requests.post(url, json=payload, headers=headers)
print(response.json())  # Resposta do servidor sobre o convite
