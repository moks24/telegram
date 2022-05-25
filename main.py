import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot('5338205847:AAFYNddrGLJ6cM1Q41NDdODumNO_zsmKNr0')  # token

def mainmenu():
    keyboard = types.InlineKeyboardMarkup()
    keyboard = types.InlineKeyboardMarkup(row_width=2)  # выбираем тип клавиатуры
    about_hotel = types.InlineKeyboardButton(text='Об отеле\U0001F4AB', callback_data='btn1')
    contacts = types.InlineKeyboardButton(text='Контакты\U0001F514', callback_data='btn4')
    keyboard.add(about_hotel, contacts)
    restoran = types.InlineKeyboardButton(text='Ресторан\U0001F371', callback_data='btn3')
    uslugi = types.InlineKeyboardButton(text='Удобства и услуги\U0001F440', callback_data='btn6')
    keyboard.add(restoran, uslugi)
    weather = types.InlineKeyboardButton(text='Погода\U0001F31E', callback_data='btn2')
    time = types.InlineKeyboardButton(text='Местное время\U0001F552', callback_data='btn5')
    keyboard.add(time, weather)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    keyboard_1 = mainmenu()
    bot.send_message(message.chat.id, 'Отель <b>"Gratia"</b>', reply_markup=keyboard_1, parse_mode='HTML')

@bot.callback_query_handler(func=lambda callback: callback.data)
def answer_callback(callback):
    if callback.data == 'btn4':
        photo = open('reception.png', 'rb')  # фото отеля
        bot.send_photo(callback.message.chat.id, photo)  # ответное сообщение с фото
        kb = types.InlineKeyboardMarkup(row_width=2)
        gps_yandex = types.InlineKeyboardButton(text='Посмотреть на Yandex карте',
                                                url='https://yandex.ru/maps/-/CCUJANhP8D')
        gps_google = types.InlineKeyboardButton(text='Посмотреть на Google карте',
                                                url='https://goo.gl/maps/qVLNCqnEZ3tDRbWd9')
        kb.add(gps_yandex, gps_google)
        bot.send_message(callback.message.chat.id, """
<b>Наши контакты:</b>
Адрес: г. Асирис, ул. Одиссея д.1
Ресепшн: +79168697207
Отдел бронирования: +79878878756
email: fedorov_ns@mail.ru
""", reply_markup=kb, parse_mode='HTML')

    elif callback.data == 'btn5':  # возвращает сообщение с датой и временем в режиже реального времени
        bot.send_message(callback.message.chat.id,
                         '<b>Местное время:</b>\n' + str(datetime.now().strftime("%d.%m.%Y, %H:%M")), parse_mode='HTML')

    elif callback.data == 'btn2':  # возвращает сообщение с текущей погодой
        kb = types.InlineKeyboardMarkup(row_width=1)
        weather_ = types.InlineKeyboardButton(text='необходимо спарсить сайт с погодой', callback_data='btn_weather')
        kb.add(weather_)
        bot.send_message(callback.message.chat.id, 'Прогноз погоды на сегодня', reply_markup=kb)

    elif callback.data == 'btn3':  # информация о ресторане или кафе, также возможен лобибар и буфет
        bot.send_message(callback.message.chat.id, """
Бар расположен на 1-ом этаже
Ресторан находится на территории отеля в 1-м корпусе
Завтрак в номер, для заказа свяжитесь с администратором по номеру тел. +79878878756
""")

    elif callback.data == 'btn1':
        photo_hotel = open('HOTEL.png', 'rb')
        bot.send_photo(callback.message.chat.id, photo_hotel)
        bot.send_message(callback.message.chat.id, """
Отель Gratia расположен в уютном районе Гротеска, в нескольких шагах от дизайнерских магазинов.
К услугам гостей номера и люксы с бесплатным Wi-Fi. При отеле работает бар-ресторан, где подают блюда средиземноморской кухни.
До исторического центра Гротеска несколько минут ходьбы.

Все номера в мягких тонах обставлены специально подобранной мебелью и оформлены в современном стиле.
В распоряжении гостей кондиционер, телевизор с плоским экраном и спутниковыми каналами.
В некоторых номерах обустроена гостиная зона. В большинстве номеров есть балкон.
Ванная комната с ванной или душем укомплектована тапочками, бесплатными туалетно-косметическими принадлежностями и феном.

Стойка регистрации открыта круглосуточно. По запросу и за дополнительную плату организуется трансфер от/до аэропорта.

В отеле можно взять напрокат велосипеды. От отеля Gratia до Национального сада — 400 метров, а до центральной площади — 500 метров.
Расстояние до аэропорта имени Циклопа одноглазого составляет 38 км.
Расстояние до железнодорожного вокзала составляет 8 км.

Это любимая часть города Гротеска среди наших гостей согласно независимым отзывам.
""", parse_mode='HTML')

    elif callback.data == 'btn6':
        uslugimenu = types.InlineKeyboardMarkup(row_width=2)
        himchistka = types.InlineKeyboardButton(text='Прачечная', callback_data='btn_himchistka')
        sauna = types.InlineKeyboardButton(text='Сауна', callback_data='btn_sauna')
        back = types.InlineKeyboardButton(text='Главное меню', callback_data='btn_back')
        uslugimenu.add(himchistka, sauna, back)
        bot.send_message(callback.message.chat.id, 'Наши услуги',
                         reply_markup=uslugimenu)
        # Todo лучше разделить услуги на платные и бесплатные

    elif callback.data == 'btn_himchistka':
        bot.send_message(callback.message.chat.id, """
<b>Услиги праченой:</b>
Стирка-500р
Погладить белье-100р
Подшить одежду-250р
""", parse_mode='HTML')

    elif callback.data == 'btn_sauna':
        bot.send_message(callback.message.chat.id, 'Сауна на 8 челове, 1час-500р')

    elif callback.data == 'btn_back':
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              text='вы вернулись в главное меню', reply_markup=mainmenu())


bot.infinity_polling()