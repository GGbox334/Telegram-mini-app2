import asyncio
import logging
from aiogram import Bot, Dispatcher, types

TOKEN = "7949716168:AAGsvORpGGWtSAoSv6SJqGZWlAlqphP0-4s"  # Вставь сюда свой токен

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
