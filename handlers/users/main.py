from loader import dp
from aiogram.types import Message

from keyboard.inline.problem import pblm
from keyboard.inline.restaurants import rest


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: Message):
    await message.answer(text="Добро пожаловать {0.first_name}!\nМеня зовут Виктория!\n\nКак на счет перекусить? В гостинице"
                           " есть рестораны с видом на набережную на 1 этаже и с видом на Выборгский замок"
                           "и старый город на 7 этаже! Если вы голодны и не хотите никуда идти напишите /eat.\n\n"
                           "Я так же могу помочь в решений технических проблем! Если не работает телевизор или "
                           "Wi-Fi, то напишите /problem.")


@dp.message_handler(commands=['eat'])
async def command_eat(message: Message):
    await message.answer(text="У нас есть два ресторана с Европейской и Итальянской кухней!\n\n Какую предпочитаете вы?", reply_markup=rest)


@dp.message_handler(commands=['problem'])
async def command_problems(message: Message):
    await message.answer(text="Выберете с чем именно у вас проблема и я покажу самые частые варианты их решения!", reply_markup=pblm)
