from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttonMain = KeyboardButton('Главное меню')

# ---MAIN MENU---
buttonRoom = KeyboardButton('Номерной фонд')
buttonRestaurant = KeyboardButton('Наши рестораны')
buttonExcursions = KeyboardButton('Экскурсии')
buttonFitness = KeyboardButton('Фитнес')
buttonTechnique = KeyboardButton('Технические вопросы')
buttonTransfer = KeyboardButton('Трансфер')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonRoom, buttonRestaurant, buttonExcursions, buttonTechnique, buttonFitness, buttonTransfer)

# ---ROOM MENU---
roomMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonMain)
# ---RESTAURANT MENU---
restaurantMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonMain)
# ---Fitness MENU---
fitnessMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonMain)
# ---Excursions MENU---
excursionsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonMain)
buttonVSpace = KeyboardButton('Музей Выборг Космический')
# ---Transfer MENU---
techniqueMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonMain)
buttonWifi = KeyboardButton('Инструкция подключения Wi-Fi')
buttonTV = KeyboardButton('Инструкция по Телевизору')
