import json
from aiogram import Dispatcher, Bot, executor, types
from config import TOKEN
from aiogram.dispatcher.filters import Text
from main import collect_data
from aiogram.utils.markdown import hbold, hlink
import time
import requests

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
#второй параметр для лучшего оформления карточек
dp = Dispatcher(bot)  #для управления хэндлерами



@dp.message_handler(commands='start')
async def start(message: types.Message):  #функция ассинхронная,для ответа на команду старт
    num_buttoms = ['Give your number ☎️']
    start_buttoms = ['🔪knives', '🥊gloves', '🔫sniper rifles']  #создаю клавиатуру в боте и добавляю в нее сразу несколько обьектов
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)  #создаю обьект клавиатуры, параметр что бы кнопки были нормальных размеров
    keybord.add(*start_buttoms)
    keybord.add(*num_buttoms)
    await message.answer('Hi, please,choose category!', reply_markup=keybord)


@dp.message_handler(Text(equals='🥊gloves'))
async def get_discount_knives(message: types.Message):
    await message.answer('Please waiting...')

    collect_data()#импорт для подгрузки данных из json файла в main
    with open('result1.json') as file:
        data = json.load(file)
    for index, item in enumerate(data):#дает кроме обьекта индекс где он нахожуится enumerate
        card = f'{hlink(item.get("fullName"), item.get("3d"))}\n'\
               f'{hbold("Discount: ")}{item.get("overprice")}%\n'\
               f'{hbold("Price: ")}${item.get("price")}🔥'
        if index%20==0:#если индекс от деления на 20 будет 0 то засыпаем на 3 секунды что бы не было бана за флуд
            time.sleep(3)
        await message.answer(card)
@dp.message_handler(Text(equals='🔪knives'))
async def get_discount_gloves(message: types.Message):
    await message.answer('Please waiting...')

    collect_data()

    with open('result2.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("fullName"), item.get("3d"))}\n' \
               f'{hbold("Discount: ")}{item.get("overprice")}%\n' \
               f'{hbold("Price: ")}${item.get("price")}🔥'

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='🔫sniper rifles'))
async def get_discount_gloves(message: types.Message):
    await message.answer('Please waiting...')

    collect_data()

    with open('result3.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("fullName"), item.get("3d"))}\n' \
               f'{hbold("Discount: ")}{item.get("overprice")}%\n' \
               f'{hbold("Price: ")}${item.get("price")}🔥'

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)

def main():
    executor.start_polling(dp)#для запуска бота

if __name__ == '__main__':
    main()