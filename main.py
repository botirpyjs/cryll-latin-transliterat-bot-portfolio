from transliterate import to_cyrillic, to_latin
import telebot

token = 'token' #<<< QO'SHTIRNOQ ORASIGA BOT TOKENI KIRITILADI 
bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    javob = "Assalomu alaykum mening Pythonda ishlangan botimga hush kelibsiz!"
    javob += "\nBu botning vazifasi Krillcha so'zlarni Lotin alifbosidagi so'zlarga alishtiradi.\nAksincha Lotin alifbosidagi so'zlarni Krill so'zlariga alishtirib beradi."
    javob1 = "\n\nMatn kiriting:"
    bot.reply_to(message, javob + javob1)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    bot.reply_to(message, javob(msg))            
bot.polling()
