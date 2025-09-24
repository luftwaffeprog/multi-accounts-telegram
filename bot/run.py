import aiogram
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message
load_dotenv()


bot = Bot(os.getenv('token'))
dp = Dispatcher()
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("hello world")
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
