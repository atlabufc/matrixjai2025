# Define ou altera o tópico (descrição) da sala
import requests

access_token = "SEU_TOKEN"
room_id = "!suaSala:matrix.org"
homeserver = "https://matrix.org"

url = f"{homeserver}/_matrix/client/v3/rooms/{room_id}/state/m.room.topic"
headers = {"Authorization": f"Bearer {access_token}"}
payload = {"topic": "Este é o novo tópico da sala."}

response = requests.put(url, json=payload, headers=headers)
print("Status:", response.status_code)
