from telethon.sync import TelegramClient, events
import os
from dotenv import load_dotenv
load_dotenv()

client = TelegramClient('name', os.getenv('api_id'), os.getenv('api_hash'))

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    sender_name = sender.first_name if sender else "Unknown"
    print(f"[{event.date}] {sender_name}: {event.message.text}")

client.start()
client.run_until_disconnected()
