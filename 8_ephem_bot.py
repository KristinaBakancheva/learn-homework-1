"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename="bot.log")

import ephem
from datetime import date

TODAY = date.today().strftime("%Y/%m/%d")

PROXY = {
    "proxy_url": "socks5://t1.learn.python.ru:1080",
    "urllib3_proxy_kwargs": {
        "username": "learn",
        "password": "python"
    }
}

planets = {
    "mercury": ephem.Mercury,
    "venus": ephem.Venus,
    "mars": ephem.Mars,
    "jupiter": ephem.Jupiter,
    "saturn": ephem.Saturn,
    "uranus": ephem.Uranus,
    "neptune": ephem.Neptune,
    "pluto": ephem.Pluto
}

def greet_user(update, context):
    text = "Вызван /start"
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def find_constellation(update, context):
    user_text = update.message.text.split(" ")
    if len(user_text)==1 or planets.get(user_text[1].lower()) is None:
        update.message.reply_text("Планета не найдена. Вы должны написать название планеты на английском. ")
    else:
        planet = planets.get(user_text[1].lower())(TODAY)
        constellation = ephem.constellation(planet)
        planet = user_text[1].capitalize()
        update.message.reply_text(f"Сегодня планет {planet} в созвездии {constellation[1]}.")




def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
