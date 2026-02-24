import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from datetime import datetime
from buttons import time_menu

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

# 🔥 foydalanuvchi tug‘ilgan sanasini saqlaymiz
users_birthdays = {}


# 1️⃣ START
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🎂 Tug‘ilgan sanangizni kiriting:\n\nFormat: DD/MM/YYYY\nMasalan: 21/03/2005"
    )


# 2️⃣ Sana qabul qilish
@dp.message()
async def get_birthday(message: Message):
    try:
        birth_date = datetime.strptime(message.text, "%d/%m/%Y")
        users_birthdays[message.from_user.id] = birth_date

        await message.answer(
            "✅ Sana qabul qilindi!\nEndi hisoblash turini tanlang 👇",
            reply_markup=time_menu
        )

    except:
        await message.answer("❌ Noto‘g‘ri format! Iltimos DD/MM/YYYY formatda kiriting.")


# 3️⃣ Hisoblash qismi
@dp.callback_query()
async def calculate(callback: CallbackQuery):
    await callback.answer()

    user_id = callback.from_user.id

    if user_id not in users_birthdays:
        await callback.message.answer("Avval /start bosing.")
        return

    birth_date = users_birthdays[user_id]
    now = datetime.now()
    diff = now - birth_date

    if callback.data == "seconds":
        result = int(diff.total_seconds())
        text = f"⏳ Siz {result:,} sekund yashagansiz."

    elif callback.data == "days":
        result = diff.days
        text = f"📅 Siz {result:,} kun yashagansiz."

    elif callback.data == "weeks":
        result = diff.days // 7
        text = f"🗓 Siz {result:,} hafta yashagansiz."

    elif callback.data == "months":
        result = diff.days // 30
        text = f"📆 Siz taxminan {result:,} oy yashagansiz."

    elif callback.data == "years":
        result = diff.days // 365
        text = f"🎂 Siz taxminan {result:,} yil yashagansiz."

    await callback.message.answer(text)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
