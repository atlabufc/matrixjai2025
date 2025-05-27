# Bot que registra mensagens recebidas em um arquivo local
from nio import AsyncClient, RoomMessageText, MatrixRoom
import asyncio

homeserver = "https://matrix.org"
user_id = "@seuusuario:matrix.org"
access_token = "SEU_TOKEN"

client = AsyncClient(homeserver, user_id)
client.access_token = access_token

async def registrar_mensagens(room: MatrixRoom, event: RoomMessageText):
    with open("log_mensagens.txt", "a", encoding="utf-8") as f:
        f.write(f"{event.sender}: {event.body}\n")

client.add_event_callback(registrar_mensagens, RoomMessageText)

async def main():
    await client.sync_forever(timeout=30000)

asyncio.run(main())
