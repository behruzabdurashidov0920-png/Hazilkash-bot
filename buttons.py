from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

time_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⏳ Sekund", callback_data="seconds")],
    [InlineKeyboardButton(text="📅 Kun", callback_data="days")],
    [InlineKeyboardButton(text="🗓 Hafta", callback_data="weeks")],
    [InlineKeyboardButton(text="📆 Oy", callback_data="months")],
    [InlineKeyboardButton(text="🎂 Yil", callback_data="years")]
])
