from asyncio import run
from random_haiku import rnd_haiku
from parser import photo_parser
from text_on_photo import write_on_photo
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from os import environ, remove
from random import randint

bot = AsyncTeleBot(environ['BOT_TOKEN'])


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Хокку'))
    await bot.send_message(message.from_user.id,
                           "Я бот, который генерирует Хокку.\nНажми на кнопку и получишь картинку и текст",
                           reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Хокку')
async def echo_message(message):
    try:
        haiku = await rnd_haiku()
        await photo_parser(f'Японская живопись {haiku[randint(0,2)]}')
        text = ''.join(haiku)
        await write_on_photo(text)
        photo = open('temp/img.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo, caption=text)
        photo.close()
        remove('temp/img.jpg')
    except Exception as e:
        print(e)
        await bot.send_message(message.from_user.id, 'Боту плохо, повторите запрос через какое-то время')


async def main():
    await bot.infinity_polling()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run(main())
