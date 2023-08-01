import requests
import json


import telebot
import config

TOKEN = config.TOKEN

bot = telebot.TeleBot(TOKEN)





class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        if base == quote:
            raise APIException("Вы ввели одинаковые валюты")

        try:
            base_ticker = base.upper()
            quote_ticker = quote.upper()
            url = f"https://api.exchangerate.host/latest?base={base_ticker}&symbols={quote_ticker}"
            response = requests.get(url)
            data = json.loads(response.text)
            price = data["rates"][quote_ticker]
            total = price * amount
            return total
        except:
            raise APIException("Ошибка при получении данных о валюте")


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    # Вывод инструкций
    instructions = "Привет! Я бот для конвертации валют.\n" \
                   "Для получения цены на определённое количество валюты " \
                   "отправьте мне сообщение в формате:\n" \
                   "<имя валюты, цену которой вы хотите узнать> " \
                   "<имя валюты, в которой надо узнать цену первой валюты> " \
                   "<количество первой валюты>\n" \
                   "Например: USD RUB 100\n\n" \
                   "Для просмотра списка доступных валют используйте команду /values"
    bot.send_message(message.chat.id, instructions)


@bot.message_handler(commands=['values'])
def handle_values(message):
    # Вывод списка доступных валют
    values = "Доступные валюты:\n" \
             "USD - Доллар США\n" \
             "EUR - Евро\n" \
             "RUB - Российский рубль"
    bot.send_message(message.chat.id, values)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        # Обработка текстового сообщения
        text = message.text.strip().split()
        if len(text) != 3:
            raise APIException("Неверный формат запроса. Пожалуйста, введите данные в правильном формате.")

        base_currency, quote_currency, amount = text
        amount = float(amount)

        result = CurrencyConverter.get_price(base_currency, quote_currency, amount)
        bot.send_message(message.chat.id, f"{amount} {base_currency} = {result} {quote_currency}")

    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {type(e).__name__}")


if __name__ == '__main__':
    bot.polling(none_stop=True)
