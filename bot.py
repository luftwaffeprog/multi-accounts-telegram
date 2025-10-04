import aiogram
import os
from dotenv import load_dotenv
import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message
import logging
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
import telethon_client as tg

load_dotenv()


bot = Bot(os.getenv('token'))
dp = Dispatcher(storage=MemoryStorage())

class LoginState(StatesGroup):
    waiting_for_phone = State()
    waiting_for_code = State()
    waiting_for_password = State()

client = {}

@dp.message(Command("login"))
async def login_start(message: types.Message, state: FSMContext):
    await message.answer("Phone number (example: +79999999999)")
    await state.set_state(LoginState.waiting_for_phone)

@dp.message(LoginState.waiting_for_phone)
async def process_phone(message:types.Message, state: FSMContext):
    phone = message.text.strip()
    ok = await tg.send_code(message.from_user.id, phone)
    if not ok:
        await message.answer("please, try again")
        await state.finish()
        return
    await state.update_data(phone=phone)
    await message.answer("code is send")






async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
