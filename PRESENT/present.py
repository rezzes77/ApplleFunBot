import telebot
from telebot import types
import requests
import random
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


TOKEN = '7655944017:AAEBEgtLcXeWPRxklDF-32k_JqBMYSUlIV4'
bot = telebot.TeleBot(TOKEN)

reviews = []
user_photos = []
user_scores = {}

@bot.message_handler(commands=['start'])
def start(message):
    try:
        with open('appleim/81531-3840x2160-desktop-4k-apple-logo-wallpaper.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Продукты Apple🍏')
        btn2 = types.KeyboardButton('Новости Apple🗞')
        btn3 = types.KeyboardButton('Видео про Apple📹')
        btn4 = types.KeyboardButton('Поддержка🆘')

        keyboard.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, f"""{message.from_user.username}, Добро пожаловать в официальный бот Apple!
Здесь вы найдете все самое важное о продукции Apple: от последних новинок до подробных характеристик наших устройств. Мы рады помочь вам узнать больше о iPhone, MacBook, Apple Watch, и многих других продуктах.

🎬 Смотрите видео с презентациями и рекламой.
📰 Будьте в курсе последних новостей Apple и всех значимых событий.
💬 Получите поддержку по вопросам настройки, обслуживания и покупок.

Выберите одну из опций в меню и начните исследовать мир Apple прямо сейчас!""", reply_markup=keyboard)
        stic1 = 'CAACAgIAAxkBAAEM7D1nATnE7xIQJKeCaWSNrpSfPCWPNAACRhkAAnqiQUuZhN7FjveOyTYE'
        
        bot.send_sticker(message.chat.id, stic1)

    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")
        
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, """Команды, доступные в этом боте:
- /start - Начать взаимодействие с ботом
- /help - Получить список доступных команд
- /about - Узнать больше о боте
- /contact - Получить контактные данные для поддержки
- /latest_news - Узнать последние новости о продукции Apple
- /feedback - Оставить отзыв о работе бота
- /settings - Настроить предпочтения
- /reviews - Посмотреть все отзывы
- /website - Посмотреть другой веб-сайт
- /memes - Показать случайный мем про Apple
- /upload_photo - Загрузить фото продукта в галерею
- /view_gallery - Посмотреть загруженные фотографии пользователей
""")
    sticker_id = 'CAACAgIAAxkBAAEM7DtnATi0ygTC37YM3GGfxvRM0yTO1QACJT8AAt5DsEmSRUuwhckdCjYE'
    
    bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(commands=['about'])
def about_command(message):
    bot.send_message(message.chat.id, """Этот бот создан для предоставления информации о продуктах Apple и последних новостях компании. Мы рады помочь вам с любыми вопросами, связанными с продукцией Apple!""")

@bot.message_handler(commands=['contact'])
def contact_command(message):
    bot.send_message(message.chat.id, """Если у вас есть вопросы или нужна помощь, вы можете связаться с нашей службой поддержки по электронной почте: support@apple.com""")

@bot.message_handler(commands=['latest_news'])
def latest_news_command(message):
    bot.send_message(message.chat.id, "Вот последние новости о продукции Apple:\n- Новая версия iPhone\n- Обновление macOS\n- Запуск нового Apple Watch")

@bot.message_handler(commands=['feedback'])
def feedback_command(message):
    msg = bot.send_message(message.chat.id, "Мы ценим ваше мнение! Пожалуйста, напишите ваш отзыв:")
    bot.register_next_step_handler(msg, save_feedback)

def save_feedback(message):
    reviews.append(message.text)  
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв!")

@bot.message_handler(commands=['reviews'])
def reviews_command(message):
    if reviews:
        response = "Отзывы:\n" + "\n".join(reviews)
    else:
        response = "Пока нет отзывов."
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['settings'])
def settings_command(message):
    bot.send_message(message.chat.id, "Настройки еще не реализованы. Пожалуйста, ждите обновленийю")
    
@bot.message_handler(commands=['website'])
def website_command(message):
    try:
        with open('appleim/nft-trend-continuation-short-term-fashion-large-webp.webp', 'rb') as nft:
            bot.send_photo(message.chat.id, nft)
            
            bot.send_message(message.chat.id, 'Вы также можете рассмотреть сайт про NFT: https://calm-hamster-356f9c.netlify.app/')
            
            stic4 = 'CAACAgIAAxkBAAEM7EVnATxMGIrGgMoZmhi4f_v1wUcK3AACekMAAr5ysEmcFrzlK7nKQTYE'
            
            bot.send_sticker(message.chat.id, stic4)
    
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
        
@bot.message_handler(commands=['memes'])
def send_meme_button(message):

    markup = types.InlineKeyboardMarkup()
    meme_button = types.InlineKeyboardButton("Показать мем", callback_data='show_meme')
    markup.add(meme_button)
    
    bot.send_message(message.chat.id, "Нажми на кнопку, чтобы увидеть случайный мем про Apple!", reply_markup=markup)


    
    
@bot.message_handler(commands=['upload_photo'])
def ask_for_photo(message):
    bot.send_message(message.chat.id, "Отправь фотографию своего продукта, и она будет добавлена в галерею!")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        if not os.path.exists('user_photos'):
            os.makedirs('user_photos')
        
        photo_path = f'user_photos/{message.from_user.id}_{file_info.file_id}.jpg'
        
        with open(photo_path, 'wb') as photo_file:
            photo_file.write(downloaded_file)
        
        user_photos.append(photo_path)
        
        bot.send_message(message.chat.id, "Фотография успешно загружена в галерею!")
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при загрузке фотографии.")
        print(e)

@bot.message_handler(commands=['view_gallery'])
def show_gallery(message):
    bot.send_message(message.chat.id, 'Снизу вы можете увидеть галерею фото👇')
    if not user_photos:
        bot.send_message(message.chat.id, "Галерея пуста. Загрузите фотографии, используя команду /upload_photo.")
    else:
        for photo in user_photos:
            with open(photo, 'rb') as photo_file:
                bot.send_photo(message.chat.id, photo_file)
memes = [
    'memes/2024-09-10-mixnews-114.webp',
    'memes/AQAK1X8LYEAYH_QrcUlf1irRK2jvM-2p26UPJ61ORIOQNEDHH5mTOeIADOqZEFJl3fl1CgYzABNKimtMpzBiqyyGYIY.webp',
    'memes/AQAKApp0oppo7XSoeFs-7rpV2eUeCjrsQ4VCwY0StL2FNLP18yD9KDW6TBJFvucvczeng63v7JTZBNfNA-R9be5BgJA.webp',
    'memes/AQAKcA9uRfiP3uMxyrkK_Kw7sh0D4Wya_AovqE4bQAaHwIy1Fs3Em18oehxbPikZPy71eYPXUmdBZQ1RXkC5WDBofKU.webp',
    'memes/photo_2023-06-06_10-19-28-3-1024x576.jpeg',
    'memes/snimok-ekrana-2024-02-05-v-12.33.54-453x576.png'
]

@bot.callback_query_handler(func=lambda call: call.data == 'show_meme')
def show_random_meme(call):
    try:
        if call.message:
            random_meme = random.choice(memes)
            
            with open(random_meme, 'rb') as meme_file:
                bot.send_photo(call.message.chat.id, meme_file)
            
            bot.answer_callback_query(call.id, "Вот твой мем!")
    except Exception as e:
        print(e)





@bot.message_handler(func=lambda message: message.text == 'Продукты Apple🍏')
def send_product(message):
    markup = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton('Iphone📱', callback_data='iphone')
    btn6 = types.InlineKeyboardButton('MacBook💻', callback_data='macbook')
    btn7 = types.InlineKeyboardButton('Apple Watch⌚️', callback_data='apple_watch')
    btn8 = types.InlineKeyboardButton('Ipad📋', callback_data='ipad')
    btn9 = types.InlineKeyboardButton('Air Pods🎧', callback_data='air_pods')

    markup.add(btn5, btn6, btn7, btn8, btn9)


    bot.send_message(message.chat.id, 'Хорошо, теперь выбери продукцию, которую ты хочешь:', reply_markup=markup)
    
    
@bot.message_handler(func=lambda message: message.text == 'Видео про Apple📹')
def send_videos(message):
    markup = types.InlineKeyboardMarkup()
    
    btn13 = types.InlineKeyboardButton("📹 Презентации продуктов", callback_data="product_presentations")
    btn14 = types.InlineKeyboardButton("🎬 Обзоры", callback_data="reviews")
    btn15 = types.InlineKeyboardButton("📺 Рекламные ролики", callback_data="ads")
    btn16 = types.InlineKeyboardButton("📖 Учебные видео", callback_data="tutorials")
    
    markup.add(btn13, btn14, btn15, btn16)

    bot.send_message(message.chat.id, 'Выберите категорию видео:', reply_markup=markup)
    
    
@bot.message_handler(func=lambda message: message.text == 'Новости Apple🗞')
def send_news(message):
    markup = types.InlineKeyboardMarkup()
    
    btn10 = types.InlineKeyboardButton("📢 Последние новости", callback_data="latest_news")
    btn11 = types.InlineKeyboardButton("⚙️ Обновления ПО", callback_data="software_updates")
    btn12 = types.InlineKeyboardButton("🔔 Подписка на новости", callback_data="subscribe")
    
    markup.add(btn10, btn11, btn12)

    bot.send_message(message.chat.id, 'Хорошо, теперь выбери опцию, которую ты хочешь:', reply_markup=markup)
    
@bot.message_handler(func=lambda message: message.text == 'Поддержка🆘')
def send_support(message):
    markup = types.InlineKeyboardMarkup()
    
    btn1 = types.InlineKeyboardButton("📞 Контакты службы поддержки", callback_data="support_contacts")
    btn2 = types.InlineKeyboardButton("🛠 Статьи по устранению проблем", callback_data="support_articles")
    btn3 = types.InlineKeyboardButton("📋 Часто задаваемые вопросы (FAQ)", callback_data="support_faq")
    btn4 = types.InlineKeyboardButton('🌐Официальный сайт Apple', callback_data='official_site')
    
    
    markup.add(btn1, btn2, btn3)
    markup.add(btn4)

    bot.send_message(message.chat.id, "Выберите вариант поддержки, который вам нужен:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'iphone':
        bot.answer_callback_query(call.id, "Вы выбрали iPhone!")
        try:
            if call.message:
                with open('appleim/Apple-iPhone-16-Pro-hero-240909-lp.jpg.landing-big_2x.jpg', 'rb') as iphone:
                    bot.send_photo(call.message.chat.id, iphone)

                bot.send_message(call.message.chat.id, """iPhone 16 Pro Max — Последняя Линейка от Apple

📱 **iPhone 16 Pro Max** — это не просто телефон, это новый шаг в мобильных технологиях. Он сочетает в себе самые современные технологии, потрясающий дизайн и отличную производительность, создавая уникальное и незабываемое пользовательское впечатление.

### Технические характеристики:
- **Процессор**: Чип A17 Pro — революционная производительность для игр, приложений и многозадачности.
- **Дисплей**: 6.7-дюймовый Super Retina XDR дисплей с ProMotion и поддержкой частоты обновления 120 Гц для плавной прокрутки и невероятной четкости изображения.
- **Камера**: Тройная камера с улучшенным ночным режимом, 48 МП основная камера для потрясающих фотографий и 3x оптическим зумом.
- **Аккумулятор**: До 28 часов работы с видео — впечатляющая автономность для самого требовательного использования.
- **Память**: Доступные варианты с 128, 256, 512 ГБ и 1 ТБ хранилища, позволяющие хранить все данные, не переживая о нехватке места.
- **Дизайн**: Изысканная отделка из нержавеющей стали и матового стекла, доступен в нескольких элегантных цветах.
  
""")
                
            stic2 = 'CAACAgIAAxkBAAEM7D9nATpczzIIEWDFFrNcxN3iNaQO_QACqxQAAqfQ8UtQa9YTljxjoDYE'
        
            bot.send_sticker(call.message.chat.id, stic2)

            


        except Exception as e:
            bot.send_message(call.message.chat.id, f"Произошла ошибка: {e}")

    
    elif call.data == 'macbook':
        bot.answer_callback_query(call.id, 'Вы выбрали MacBook')
        try:
            if call.message:
                with open('appleim/macbook-pro-2023-m2-chip-600nw-2328203513.webp', 'rb') as mac:
                    bot.send_photo(call.message.chat.id, mac)
                    
                bot.send_message(call.message.chat.id, """MacBook — Легендарные Ноутбуки от Apple

💻 MacBook — это мощные ноутбуки, которые обеспечивают безупречную производительность, элегантный дизайн и исключительную автономность. С каждым новым поколением MacBook предлагает еще больше возможностей для работы, творчества и развлечений.

📊 **Технические характеристики MacBook**:
- **Процессор**: чип M2, который обеспечивает выдающуюся скорость и эффективность.
- **Дисплей**: Retina с разрешением 2560x1600 для невероятной четкости и цветопередачи.
- **Оперативная память**: до 16 ГБ, что позволяет работать с несколькими приложениями одновременно без потери производительности.
- **Хранение**: до 1 ТБ SSD, обеспечивающий молниеносную загрузку и быстрый доступ к файлам.

🎨 **Дизайн**: Стильный и ультратонкий корпус, который легко брать с собой в любую поездку.

🔋 **Автономность**: До 20 часов работы без подзарядки — идеальный выбор для работы на ходу.

С MacBook вы получите сочетание потрясающей мощности и бескомпромиссного качества. Он станет вашим идеальным помощником для работы и развлечений.

Выберите модель MacBook, которая подходит именно вам, и начните наслаждаться работой с Apple!""")
                
        except Exception as e:
            bot.send_message(call.message.chat.id, f"Произошла ошибка: {e}")
            
    elif call.data == 'apple_watch':
        bot.answer_callback_query(call.id, "Вы выбрали Apple watch!")
        try:
            if call.message:
                with open('appleim/pexels-tdcat-437037.jpg', 'rb') as watch:
                    bot.send_photo(call.message.chat.id, watch)

                bot.send_message(call.message.chat.id, """Apple Watch — Ваш Личный Помощник на Запястье

⌚ **Apple Watch** — это не просто смарт-часы, это полный набор функций для вашего здоровья, фитнеса и повседневной жизни. С каждым обновлением Apple Watch становится еще умнее, надежнее и красивее. 

### Технические характеристики:
- **Дисплей**: Retina Always-On Display с яркими и четкими цветами даже при ярком солнечном свете.
- **Здоровье и фитнес**: Современные датчики для мониторинга сердечного ритма, ЭКГ, измерения уровня кислорода в крови и даже температурный датчик для отслеживания здоровья в реальном времени.
- **Производительность**: Чип S9 с улучшенной производительностью, который позволяет эффективно работать с приложениями и функциями.
- **Аккумулятор**: До 18 часов работы без подзарядки — достаточно для всего дня активного использования.
- **Новый интерфейс**: Пользовательский интерфейс, который адаптируется к вашему стилю жизни, а также множество циферблатов на выбор.
  
""")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"Произошла ошибка: {e}")
            
    elif call.data == 'ipad':
        bot.answer_callback_query(call.id, "Вы выбрали iPad!")
        try:
            if call.message:
                with open('appleim/iPad-Air-5-wallpaper.webp', 'rb') as ipad:
                    bot.send_photo(call.message.chat.id, ipad)

                bot.send_message(call.message.chat.id, """iPad — Ваш Портативный Умный Партнер

📱 **iPad** — это невероятно мощный и универсальный планшет, который способен справиться с любыми задачами, от работы и учебы до творчества и развлечений. Он сочетает в себе простоту использования и удивительную производительность.

### Технические характеристики:
- **Дисплей**: Яркий и четкий Liquid Retina дисплей с ProMotion для максимально плавного отображения и естественного взаимодействия.
- **Процессор**: Чип M2 для мгновенной работы с любыми приложениями, включая графические и видеоредакторы, игры и многое другое.
- **Камеры**: 12 МП основная камера с автофокусом, которая идеально подходит для съемки фото и видео, а также 12 МП фронтальная камера с функцией Center Stage для отличных видеозвонков.
- **Аккумулятор**: До 10 часов автономной работы при активном использовании — отличный выбор для длительных рабочих сессий и путешествий.
- **Память**: От 64 ГБ до 1 ТБ, чтобы вместить все ваши документы, фото, видео и приложения.


iPad — это идеальный инструмент для работы, учебы и развлечений. От простых задач до сложных проектов, iPad помогает вам быть более продуктивным и креативным в любом месте и в любое время.

Откройте для себя новый уровень возможностей с iPad!""")

        except Exception as e:
            bot.send_message(call.message.chat.id, f"Произошла ошибка: {e}")
            
    elif call.data == 'air_pods':
        bot.answer_callback_query(call.id, "Вы выбрали Air Pods!")
        try:
            if call.message:
                with open('appleim/istockphoto-1430390678-612x612.jpg', 'rb') as watch:
                    bot.send_photo(call.message.chat.id, watch)

                bot.send_message(call.message.chat.id, """AirPods — Беспроводное Чудо Звука от Apple

🎧 **AirPods** — это идеальные наушники для тех, кто ценит свободу движения и исключительное качество звука. Благодаря инновационным технологиям и удобству использования, AirPods стали неотъемлемой частью экосистемы Apple.

### Технические характеристики:
- **Звук**: Чистый и сбалансированный звук с глубокими басами и кристально чистыми высокими частотами.
- **Активное шумоподавление**: В AirPods Pro и AirPods Max технология активного шумоподавления позволяет погружаться в музыку, блокируя внешние шумы.
- **Прозрачный режим**: Включите прозрачный режим, чтобы слышать окружающий мир, не снимая наушники.
- **Автономность**: До 5 часов прослушивания на одной зарядке и до 24 часов с зарядным футляром — наслаждайтесь музыкой целый день.
  

### Комфорт и дизайн:
- **Легкие и эргономичные**: AirPods удобно сидят в ушах даже при длительном использовании, а футляр для зарядки компактен и легко помещается в карман.
- **Управление касанием**: Пауза, перемотка и прием звонков возможны через простые прикосновения к наушникам.

Окунитесь в мир качественного звука без проводов и лишних сложностей с AirPods! Это ваш идеальный компаньон для музыки, общения и работы в пути.""")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"Произошла ошибка: {e}")

    elif call.data == 'latest_news':
        bot.send_message(call.message.chat.id, "Здесь отображаются последние новости Apple...")
        try:
            if call.message:
                with open('appleim/Apple-iOS-18-5628421.jpg', 'rb') as news:
                    bot.send_photo(call.message.chat.id, news)

            bot.send_message(call.message.chat.id, """📢 Последние новости Apple:

1️⃣ **Анонс iPhone 16 Pro Max**: Apple недавно выпустила новую линейку iPhone 16, которая включает в себя мощные функции, улучшенные камеры и чип M2.

2️⃣ **Обновление iOS 18**: Вышло долгожданное обновление iOS 18 с новыми возможностями, включая улучшенную безопасность и новые режимы работы с экосистемой Apple.

3️⃣ **Финансовый отчёт Q3 2024**: Apple сообщила о рекордной прибыли за третий квартал, главным драйвером стали продажи MacBook и аксессуаров.

4️⃣ **Предстоящая презентация**: Ожидается, что в октябре состоится новое мероприятие, на котором будет представлена обновленная линейка iPad и MacBook.""")

        except Exception as e:
            print(e)  
            bot.send_message(call.message.chat.id, "Произошла ошибка: не удалось загрузить изображение.")


    elif call.data == 'software_updates':
        bot.send_message(call.message.chat.id, 'Здесь отображаются обновление ПО...')
        try:
            if call.message:
                print("Отправка изображения...")
                with open('appleim/iphone_16_not_a17-1280x720.webp', 'rb') as cheap:
                    bot.send_photo(call.message.chat.id, cheap)

            # Отправка текста
            bot.send_message(call.message.chat.id, """🚀 Новые Чипы Apple: Мощь и Инновации! 💻

Apple всегда стремится к совершенству, и с новыми чипами M2 и A17 Pro мы видим, как это стремление воплощается в жизнь! 🌟

📈 Что нового?
- Производительность на уровне: Чипы M2 и A17 Pro обеспечивают невероятную скорость и эффективность работы, позволяя вам выполнять множество задач одновременно без задержек! ⚡
- Улучшенная графика: Новые графические процессоры делают игры и приложения более реалистичными и плавными. 🎮✨
- Энергоэффективность: Долгое время работы от батареи теперь доступно даже при выполнении самых требовательных задач. 🔋👍

🔄 Обновления ПО:
- Новая версия iOS 18: Она включает в себя улучшенные функции безопасности и новые возможности для пользователей. 🔒📱
- Поддержка новых функций: Новые чипы позволят использовать передовые технологии, такие как улучшенное распознавание лиц и инновационные возможности камеры. 📸👤

Apple продолжает задавать тренды в мире технологий, и с новыми чипами вы получите максимум от своих устройств! 🌍💪""")


           
           
           

        except Exception as e:
            print(f"Ошибка: {e}")  
            bot.send_message(call.message.chat.id, "Произошла ошибка: не удалось загрузить изображение или видео.")


    elif call.data == 'subscribe':
        bot.send_message(call.message.chat.id, 'Вы будете подписываться...')
    
        confirmation_link = "https://www.youtube.com/@Apple"
        bot.send_message(call.message.chat.id, f'Пожалуйста, перейдите по этой ссылке для подтверждения подписки: {confirmation_link}')
        
    elif call.data == 'product_presentations':
        bot.send_message(call.message.chat.id, 'Вы выбрали презентации продуктов Apple!')
        bot.send_message(call.message.chat.id, "Смотрите презентации на официальном канале YouTube: https://youtu.be/eDqfg_LexCQ")

    elif call.data == 'reviews':
        bot.send_message(call.message.chat.id, 'Вы выбрали обзоры продуктов!')
        bot.send_message(call.message.chat.id, "Ознакомьтесь с последними обзорами: https://youtu.be/aDqzDoJPkaA")
        
    elif call.data == 'ads':
        bot.send_message(call.message.chat.id, 'Вы выбрали рекламные ролики Apple!')
        bot.send_message(call.message.chat.id, "Смотрите рекламные ролики на официальном канале Apple: https://youtu.be/TPe8revsg3k")

    elif call.data == 'tutorials':
        bot.send_message(call.message.chat.id, 'Вы выбрали учебные видео!')
        bot.send_message(call.message.chat.id, "Изучайте учебные видео по продуктам Apple: https://youtu.be/PugKQZHPut8")
        
        
    elif call.data == 'support_contacts':
        bot.send_message(call.message.chat.id, "📞 Контакты службы поддержки:\n\nТелефон: +7 800 555 55 55\nEmail: support@apple.com")
    elif call.data == 'support_articles':
        bot.send_message(call.message.chat.id, "🛠 Статьи по устранению проблем доступны на нашем сайте:\nhttps://support.apple.com/")
    elif call.data == 'support_faq':
        bot.send_message(call.message.chat.id, "📋 Часто задаваемые вопросы (FAQ) можно найти здесь:\nhttps://support.apple.com/faq")
    elif call.data == 'official_site':
        bot.send_message(call.message.chat.id, '🌐 Вы можете перейти в официальный: \nhttps://apple.com')


bot.polling(non_stop=True)

