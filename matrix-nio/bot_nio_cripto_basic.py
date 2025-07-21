#!/usr/bin/env python3
import asyncio
import os
from nio import (
    AsyncClient,
    AsyncClientConfig,
    LoginResponse,
    RoomMessageText,
    MatrixRoom,
)

# === CONFIGURAÇÃO ===
HOMESERVER = ""
USERNAME = ""
PASSWORD = ""
ROOM_ALIAS = ""
STORE_PATH = "./bot-store"

# === CALLBACK PARA MENSAGENS RECEBIDAS ===
async def message_callback(room: MatrixRoom, event: RoomMessageText):
    if event.sender != client.user:
        print(f"📨 [{event.sender}] {event.body}")

# === PROGRAMA PRINCIPAL ===
async def main():
    global client

    config = AsyncClientConfig(encryption_enabled=True)
    client = AsyncClient(HOMESERVER, USERNAME, config=config, store_path=STORE_PATH)

    # Tenta carregar sessão anterior (se existir)
    if os.path.exists(os.path.join(STORE_PATH, "e2e.sqlite")):
        print("🔄 Restaurando sessão anterior...")
        await client.load_store()
        await client.sync_forever(timeout=30000)
        return

    # Faz login e armazena sessão
    print("🔐 Fazendo login...")
    response = await client.login(PASSWORD)
    if not isinstance(response, LoginResponse):
        print("❌ Erro no login:", response)
        return

    print(f"✅ Login como {USERNAME}")

    # Entra na sala
    print("🚪 Entrando na sala...")
    join = await client.join(ROOM_ALIAS)
    if hasattr(join, "room_id"):
        print(f"✅ Sala: {join.room_id}")
    else:
        print("❌ Falha ao entrar:", join)
        return

    # Habilita recebimento de mensagens criptografadas
    client.add_event_callback(message_callback, RoomMessageText)

    print("🤖 Escutando mensagens criptografadas (E2EE)...")
    await client.sync_forever(timeout=30000)

if __name__ == "__main__":
    asyncio.run(main())
