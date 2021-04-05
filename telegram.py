import telebot
from man import Man
from config import token, stickerId
import databaseTeleg
from telebot import types

bot = telebot.TeleBot(token)
stickerLove = stickerId

man = Man("","",0,"")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Девушка', 'Парень')

# databaseTeleg.create_table()

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, "Да. Я тут! Напиши /help для информации обо мне.")

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == "/reg":
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Давай познакомимся! Напиши '/reg', для знакомства. Напиши love, если хочешь признаться в любви.")
    elif message.text.lower() == "love":
        bot.send_sticker(message.from_user.id, stickerId)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
def get_name(message):
    man.set_name(message.text)
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    man.set_surname(message.text)
    bot.send_message(message.from_user.id, "Сколько тебе лет?")
    bot.register_next_step_handler(message, get_age)

    
def get_age(message):
    while man.get_age() == 0:
        try:
            man.set_age(int(message.text))
        except Exception:
            bot.send_message(message.from_user.id, "Цифры, пожалуйста")
            break

    bot.send_message(message.from_user.id, "А теперь главное, кто ты?", reply_markup=keyboard1)
    bot.register_next_step_handler(message, get_sex)
    

def get_sex(message):
    man.set_sex(message.text)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Да", callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data='no')
    keyboard.add(key_no)
    question = "Тебе " + str(man.get_age()) + " лет, тебя зовут " + man.get_name() + " " + man.get_surname() + " и ты " + man.get_sex() + "?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    bot.register_next_step_handler(message, get_sex)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.from_user.id, "Хорошо, запомню!")
        databaseTeleg.add_data(man.get_name(), man.get_surname(), man.get_age(), man.get_sex())
    elif call.data == "no":
        bot.send_message(call.from_user.id, "Хорошо, Давай сначала! Введите '/reg'")

bot.polling(none_stop=True, interval=0)