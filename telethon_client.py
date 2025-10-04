from telethon import TelegramClient, errors
import os
from dotenv import load_dotenv
load_dotenv()

SESSIONS_DIR = "sessions"
clients = {}

async def create_client(user_id: int) -> TelegramClient:
    session_path = os.path.join(SESSIONS_DIR, f"user_{user_id}")
    client = TelegramClient(session_path, os.getenv('api_id'), os.getenv('api_hash'))
    clients[user_id] = client
    await client.connect()
    return client

async def send_code(user_id: int, phone: str):
    client = await create_client(user_id)
    try:
        await client.send_code_request(phone)
        return True
    except errors.PhoneNumberInvalidError:
        await client.disconnect()
        clients.pop(user_id, None)
        return False
