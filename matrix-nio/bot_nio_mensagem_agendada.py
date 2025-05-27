# Bot que envia mensagem automática a cada 60 segundos
from nio import AsyncClient
import asyncio

homeserver = "https://matrix.org"
user_id = "@seuusuario:matrix.org"
access_token = "SEU_TOKEN"
room_id = "!sala:matrix.org"

client = AsyncClient(homeserver, user_id)
client.access_token = access_token

async def post_periodico():
    while True:
        await client.room_send(
            room_id, "m.room.message",
            {"msgtype": "m.text", "body": "⏰ Esta é uma mensagem agendada."}
        )
        await asyncio.sleep(60)

async def main():
    await client.sync_forever(timeout=30000, full_state=True)
asyncio.get_event_loop().create_task(post_periodico())
asyncio.get_event_loop().run_forever()
