#!/bin/bash

# CONFIGURAÇÃO DO USUÁRIO
USERNAME=""              # ex: bot-teste
PASSWORD=""              # ex: minhasenhasecreta
HOMESERVER=""            # ex:matrix.org

# LOGIN
echo "🔐 Fazendo login no Matrix..."
LOGIN_RESPONSE=$(curl -s -X POST "$HOMESERVER/_matrix/client/v3/login" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "m.login.password",
    "user": "'"$USERNAME"'",
    "password": "'"$PASSWORD"'"
  }')

ACCESS_TOKEN=$(echo "$LOGIN_RESPONSE" | jq -r '.access_token')
USER_ID=$(echo "$LOGIN_RESPONSE" | jq -r '.user_id')

if [[ "$ACCESS_TOKEN" == "null" ]]; then
  echo "❌ Erro no login: $LOGIN_RESPONSE"
  exit 1
fi

echo "✅ Login bem-sucedido como $USER_ID"
echo

# CRIAR SALA
echo "🏠 Criando nova sala..."
CREATE_ROOM_RESPONSE=$(curl -s -X POST "$HOMESERVER/_matrix/client/v3/createRoom" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}')

ROOM_ID=$(echo "$CREATE_ROOM_RESPONSE" | jq -r '.room_id')

if [[ "$ROOM_ID" == "null" ]]; then
  echo "❌ Erro ao criar sala: $CREATE_ROOM_RESPONSE"
  exit 1
fi

echo "✅ Sala criada: $ROOM_ID"
echo

# ENTRAR NA SALA (garante entrada)
echo "🚪 Entrando na sala $ROOM_ID..."
JOIN_RESPONSE=$(curl -s -X POST "$HOMESERVER/_matrix/client/v3/join/$(echo $ROOM_ID | jq -s -R -r @uri)" \
  -H "Authorization: Bearer $ACCESS_TOKEN")

if echo "$JOIN_RESPONSE" | grep -q 'room_id'; then
  echo "✅ Entrada na sala realizada com sucesso."
else
  echo "⚠️ Aviso: talvez já esteja na sala. Resposta do servidor:"
  echo "$JOIN_RESPONSE"
fi
echo

# ENVIAR MENSAGEM
echo "💬 Enviando mensagem para a sala..."
EVENT_ID=$(date +%s%N)  # timestamp único

SEND_MESSAGE_RESPONSE=$(curl -s -X PUT "$HOMESERVER/_matrix/client/v3/rooms/${ROOM_ID}/send/m.room.message/${EVENT_ID}" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "msgtype": "m.text",
    "body": "Olá, Matrix! Esta é uma mensagem automatizada via curl/script Bash."
  }')

if echo "$SEND_MESSAGE_RESPONSE" | grep -q 'event_id'; then
  echo "✅ Mensagem enviada com sucesso."
else
  echo "❌ Erro ao enviar mensagem: $SEND_MESSAGE_RESPONSE"
  exit 1
fi

echo

# LISTAR MENSAGENS
echo "📥 Buscando últimas mensagens da sala..."
MESSAGES=$(curl -s -X GET "$HOMESERVER/_matrix/client/v3/rooms/${ROOM_ID}/messages?dir=b&limit=5" \
  -H "Authorization: Bearer $ACCESS_TOKEN")

echo "$MESSAGES" | jq '.chunk[] | {sender, body: .content.body}' || echo "$MESSAGES"
