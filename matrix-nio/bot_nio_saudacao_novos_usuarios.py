# Bot que envia mensagem de boas-vindas quando alguém entra na sala
from nio import AsyncClient, RoomMemberEvent
import asyncio

homeserver = "https://matrix.org"
user_id = "@seuusuario:matrix.org"
access_token = "SEU_TOKEN"

client = AsyncClient(homeserver, user_id)
client.access_token = access_token

async def saudacao(room, event: RoomMemberEvent):
    if event.membership == "join" and event.state_key != user_id:
        await client.room_send(
            room.room_id, "m.room.message",
            {"msgtype": "m.text", "body": f"👋 Bem-vindo(a), {event.state_key}!"}
        )

client.add_event_callback(saudacao, RoomMemberEvent)

async def main():
    await client.sync_forever(timeout=30000)

asyncio.run(main())
