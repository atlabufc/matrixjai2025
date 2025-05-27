# Altera o nome visível de uma sala
import requests

access_token = "SEU_TOKEN"
room_id = "!suaSala:matrix.org"
homeserver = "https://matrix.org"

url = f"{homeserver}/_matrix/client/v3/rooms/{room_id}/state/m.room.name"
headers = {"Authorization": f"Bearer {access_token}"}
payload = {"name": "Sala renomeada via API"}

response = requests.put(url, json=payload, headers=headers)
print("Status:", response.status_code)
