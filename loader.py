from aiogram import Bot, Dispatcher, types
import config
import logging

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig()
