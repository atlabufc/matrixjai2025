# Bot que responde a comandos iniciados com "!"
from nio import AsyncClient, RoomMessageText, MatrixRoom
import asyncio

homeserver = "https://matrix.org"
user_id = "@seuusuario:matrix.org"
access_token = "SEU_TOKEN"

client = AsyncClient(homeserver, user_id)
client.access_token = access_token

async def message_callback(room: MatrixRoom, event: RoomMessageText):
    if event.body.startswith("!ajuda"):
        await client.room_send(
            room.room_id, "m.room.message",
            {"msgtype": "m.text", "body": "📘 Comandos disponíveis: !ajuda, !info"}
        )

client.add_event_callback(message_callback, RoomMessageText)

async def main():
    await client.sync_forever(timeout=30000)

asyncio.run(main())
