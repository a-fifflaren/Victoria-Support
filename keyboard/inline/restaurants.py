from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import info_callback

rest = InlineKeyboardMarkup(row_width=2)


infoVK = InlineKeyboardButton(text="Европейская", callback_data=info_callback.new(item_name="VK"))

rest.insert(infoVK)

infoMO = InlineKeyboardButton(text="Итальянская", callback_data=info_callback.new(item_name="MO"))

rest.insert(infoMO)
