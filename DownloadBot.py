import telebot
import requests
import urllib
import os


TOKEN = '962000825:AAE6dH4zVgjf7AnSQ0DgA4CL8CgtSKXZFIY'

bot = telebot.TeleBot(TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
bt1 = telebot.types.KeyboardButton('Поменять директорию')
bt2 = telebot.types.KeyboardButton('Посмотреть результаты')
bt3 = telebot.types.KeyboardButton('Посмотреть баланс')
keyboard1.add(bt1, bt2)





@bot.message_handler(commands=['start'])
def start_message(message):
    nm = message.from_user.first_name
    bot.send_message(message.chat.id, 'Здравствуйте, ' +str(nm)+ ' , проверим Ваши навыки!', reply_markup=keyboard1);


@bot.message_handler(content_types=['text'])
def send_text(message):


    if message.text.lower() == 'поменять директорию':
        print(os.getcwd())
        bot.send_message(message.from_user.id,'Чуть позже доделаю) ', reply_markup=keyboard1)

    elif message.text.lower() == 'посмотреть результаты':
        bot.send_message(message.from_user.id, 'В разработке))', reply_markup=keyboard1);
    else:
        handle_docs_audio(message)






def handle_docs_audio(message):
    file_id = message.text
    i = 0
    a = len(file_id)
    res = file_id.split('\n')
    x= len(res)
    #file_id.find('jpeg', [0], [int(a)])
    #file_info = bot.get_file(file_id)
    #urllib.request.urlretrieve(f'https://api.telegram.org/file/bot{TOKEN}/{file_info}',
                                      # file_info.file_path)
    while i< x:
        url = res[i]

        bot.send_photo(message.chat.id, url)
        i= i+1



bot.polling(none_stop=True, interval=0)