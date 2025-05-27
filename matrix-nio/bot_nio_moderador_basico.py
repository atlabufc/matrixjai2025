# Bot que apaga mensagens com palavras ofensivas
from nio import AsyncClient, RoomMessageText, MatrixRoom
import asyncio

homeserver = "https://matrix.org"
user_id = "@seuusuario:matrix.org"
access_token = "SEU_TOKEN"

client = AsyncClient(homeserver, user_id)
client.access_token = access_token

palavras_proibidas = ["spam", "banido"]

async def moderar(room: MatrixRoom, event: RoomMessageText):
    if any(p in event.body.lower() for p in palavras_proibidas):
        await client.redact(room.room_id, event.event_id, reason="Conteúdo inadequado")

client.add_event_callback(moderar, RoomMessageText)

async def main():
    await client.sync_forever(timeout=30000)

asyncio.run(main())
