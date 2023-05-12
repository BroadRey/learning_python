import csv
import datetime
from time import time

import telebot
from telebot import types
from decouple import config

bot = telebot.TeleBot(config("TOKEN"))


@bot.message_handler(commands=["start", "начать"])
def get_start_command(message):
    text = "Привет {0} {1} я бот с буткемпа, который записывает расходы".format(message.chat.first_name,
                                                                                message.chat.last_name, )
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["calculate"])
def calculate(message):
    total_expenses = 0
    medications = 0
    utilities = 0
    food = 0
    with open(f"{message.from_user.id}.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            if i[0] == 'комм услуги':
                utilities += float(i[1])
            if i[0] == 'Аптека':
                medications += float(i[1])
            if i[0] == 'Еда':
                food += float(i[1])
            total_expenses += float(i[1])
    bot.send_message(message.chat.id,
                     f'еда: {food}с\n'
                     f'аптека: {medications}с\n'
                     f'комм услуги: {utilities}с\n'
                     f'итого: {total_expenses}с')


@bot.message_handler(commands=["categories"])
def get_category_command(message):
    text = "Выберите категории"
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("еда", callback_data="food")
    btn2 = types.InlineKeyboardButton("+", callback_data="apteka")
    btn3 = types.InlineKeyboardButton("комм услуги", callback_data="service")
    markup.add(btn3, btn2, btn1)
    bot.reply_to(message, text, reply_markup=markup)


@bot.message_handler(commands=["dates"])
def get_dates_command(message):
    text = "Выберите время, за которое хотите узнать расходы:"
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn_day = types.InlineKeyboardButton("за сегодня", callback_data="day")
    btn_week = types.InlineKeyboardButton("за неделю", callback_data="week")
    btn_month = types.InlineKeyboardButton("за месяц", callback_data="month")
    btn_year = types.InlineKeyboardButton("за год", callback_data="year")
    markup.add(btn_day, btn_week, btn_month, btn_year)
    bot.reply_to(message, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ("day",  "week", "month", "year"))
def get_dates_call_data(call: types.CallbackQuery):
    days_ago = None
    if call.data == "day":
        days_ago = datetime.timedelta(1)
    if call.data == "week":
        print('week')
        days_ago = datetime.timedelta(7)
    if call.data == "month":
        days_ago = datetime.timedelta(30)
    if call.data == "year":
        days_ago = datetime.timedelta(365)
    if days_ago == None:
        return

    total_expenses = 0
    with open(f"{call.from_user.id}.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            current_time = datetime.datetime.now()
            if current_time - datetime.datetime.strptime(i[2], '%Y-%m-%d %H:%M:%S.%f') <= days_ago:
                total_expenses += float(i[1])

    bot.send_message(call.message.chat.id,
                     f'Общие расходы за выбранный период: {total_expenses}')


empty = {}


@bot.callback_query_handler(func=lambda call: call.data in ("food", "apteka", "service"))
def get_call_data(call):
    category = None
    if call.data == "food":
        category = "Еда"
        print('еда')
    if call.data == "apteka":
        category = "Аптека"
    if call.data == "service":
        category = "комм услуги"
    empty.update({
        call.from_user.id: {"category": category}

    })
    text = "Теперь введите сумму: "
    bot.send_message(call.message.chat.id,
                     text)


@bot.message_handler(commands=["createfile"])
def create_csv_file(message):
    name_csv = message.from_user.id
    with open(f"{name_csv}.csv", "w") as file:
        expenses = csv.writer(file, delimiter=',')
        titles = ["Категория", "Цена", "Дата"]
        expenses.writerow(titles)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("food")
    btn2 = types.KeyboardButton("transport")
    btn3 = types.KeyboardButton("clothes")
    btn4 = types.KeyboardButton("+")
    btn5 = types.KeyboardButton("com.services")
    markup.add(btn4, btn5, btn3, btn2, btn1)
    bot.reply_to(message, "Успешно создана ;-), сделайте запись выберите категорию: ",
                 reply_markup=markup)


@bot.message_handler(content_types=["text", ])
def eho_bot(message):
    text = "Расход успешно сохранен"
    if message.text.isdigit():
        datetime_now = datetime.datetime.now()
        with open(f"{message.from_user.id}.csv", "a") as file:
            expenses = csv.writer(file, delimiter=',')
            expenses.writerow([empty.get(message.from_user.id)[
                              'category'], message.text, datetime_now])
    else:
        text = "введите числовое значение я не понимаю!!!"
    bot.send_message(message.chat.id, text)


bot.polling()
