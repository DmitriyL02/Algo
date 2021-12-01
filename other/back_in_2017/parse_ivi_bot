import telebot
import requests
import textwrap
import time
from bs4 import BeautifulSoup
from flask import Flask, request


token = ""
host = "https://www.ivi.ru/search"
logo = "https://www.ivi.ru/images/social/ivi_1000x523.jpg"
secret = ""
url = "https://latsis.pythonanywhere.com/" + secret

bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url=url)

app = Flask(__name__)


@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


starter = """
Привет👋! Я @cinema_dslatsis_bot и вот, что я умею делать. Я умею находить:
- Фильмы 🎥🕷🕸
- Сериалы 📺👸🏻🤴🏻
- Трейлеры ⏱🏖🎢
- Мультфильмы 🔱🌊🧜🏼‍♀️
которые есть в сервисе <a href="https://www.ivi.ru">https://www.ivi.ru</a>
"""

helper = """
<b>Я помогатор</b>🚑 и подскажу, как пользоваться мной.\n
Для того чтобы начать работу, необходимо указать какое-нибудь название, например, название фильма.
И тогда я попытаюсь найти все возможные совпадения и показать их вам.
Максимально за запрос, я показываю 10 записей,чтобы не сильно нагружать чат. Если вы
что-то не нашли, попытайтесь уточнить запрос, например, не "Гарри", а
"Гарри Поттер и Кубок Огня. Пример вывода:\n
"""

test_film = """\n
<b>Название</b>: <a href="https://thumbs.dfs.ivi.ru/storage8/contents/f/d/2bf04fca61046a0fd0ccbe9adb2931.jpg/172x264/">
Гарри Поттер и Кубок огня</a>
<b>Ограничение</b>: 12+
<b>Ссылка</b>: <a href="https://www.ivi.ru/watch/64244">https://www.ivi.ru/watch/64244</a>
<b>Доступ</b>: Смотреть по подписке
"""

template_film = """
<b>Название</b>: <a href="https:{}">{}</a>
<b>Ограничение</b>: {}
<b>Ссылка</b>: {}
<b>Доступ</b>: {}
"""


def wrapper(text, width=400):
    wrp = textwrap.TextWrapper(width=width)
    return wrp.fill(text=text)


@bot.message_handler(commands=["start"])
def start_handler(message):
    add_starter = """Для того чтобы начать работу,
введите желаемое название и я попробую что-нибудь найти для Вас. Если возникнут проблемы,
то напишите команду /help и я подскажу, как пользоваться мной."""
    starter_info = starter + wrapper(add_starter)
    bot.send_photo(message.chat.id, logo)
    bot.send_message(message.chat.id, starter_info, parse_mode="HTML")


@bot.message_handler(commands=["help"])
def help_handler(message):
    help_info = wrapper(helper) + test_film
    bot.send_message(message.chat.id, help_info, parse_mode="HTML")


@bot.message_handler(content_types=["text"])
def text_handler(message):
    params = {"q": message.text}
    r = requests.get(host, params=params)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find_all(id="js-result-box-search")
    res = []
    for i in table:
        for j in i.find_all("li"):
            try:
                result = {
                    "name": j.find(class_="name").contents[0],
                    "age": j.find(class_="age-limit").get("data-value"),
                    "url": "https://www.ivi.ru" + j.a.get("href"),
                    "access": j.find(class_="image").get("data-caption"),
                    # "score": j.find(class_="video-assessment__ivi-score").contents[0].strip(),
                    "poster": j.img.get("src")
                }
                print(result)
                res.append(result)
            except AttributeError:
                pass

    if len(res) == 0:
        output = "К сожалению, мне не удалось ничего найти 😢"
        return bot.send_message(message.chat.id, output)

    for val in reversed(res):
        film = template_film.format(val["poster"], val["name"], val["age"], val["url"], val["access"])
        bot.send_message(message.chat.id, film, parse_mode="HTML")
