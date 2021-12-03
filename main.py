import markups as nav  # Подключения кнопак меню
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from config import TOKEN  # Подключения api токена

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать {0.first_name}!".format(message.from_user), reply_markup=nav.mainMenu)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Список команд ещё не готов!")


@dp.message_handler(Text(equals=['Номерной фонд', 'Наши рестораны', 'Экскурсии', 'Фитнес', 'Технические вопросы', 'Трансфер']))
async def process_menu(message: types.Message):
    await message.answer(f'Вы выбрали {message.text}!')


# @dp.message_handler()
# async def process_eco(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
