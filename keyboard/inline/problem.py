from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import info_callback

pblm = InlineKeyboardMarkup(row_width=2)

TV = InlineKeyboardButton(text="Проблема с TV", callback_data=info_callback.new(item_name="TV"))
WiFi = InlineKeyboardButton(text="Не подключиться к Wi-Fi", callback_data=info_callback.new(item_name="WIFI"))

pblm.insert(TV)
pblm.insert(WiFi)