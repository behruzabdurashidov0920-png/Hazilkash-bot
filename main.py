import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from buttons import menu

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Diqqat! 🚨 {message.from_user.full_name} chatga qo‘shildi. Endi tinchlik yo‘q 😂",reply_markup=menu)


@dp.callback_query()
async def ans(callback: CallbackQuery):
    if callback.data == "bek1":
        await callback.answer()
        await callback.message.answer("Ma shaa Alloh! Shunaqa kayfiyat yuqumli bolsin")
    elif callback.data == "bek2":
        await callback.answer()
        await callback.message.answer("Hayoting ham 50/50 ekan-da 😅")
    elif callback.data == "bek3":
        await callback.answer()
        await callback.message.answer("Qora choymi yo “internet tezlashadigan” maxsus choymi? 📶😂")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
