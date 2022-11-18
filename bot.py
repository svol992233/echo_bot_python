from config import token
import telebot

bot = telebot.TeleBot(token)  # класс TeleBot внес в bot свои параметры (возможности)


@bot.message_handler(content_types=['animation']) # + # мы обратились к набору возможностей бот применив фунцию отcлеживания соообщений
# с типом анимация
def echo(message):  # если пришла анимация - выполняется эта функция
    if message.document.mime_type == "video/mp4":
        bot.send_animation(message.chat.id, message.document.file_id)   # эта фунция возвращает нам наше сообщение
        # (сенд мессендж функция играющая роль команды) по указанным параметрам, которые мы достаем из полученного сообщения
        # (что бы посмотреть полученное сообщение нужно вывести на принт мессендж)


@bot.message_handler(content_types=['audio']) # +
def repeat_audio(message):
    if message.audio.mime_type == 'audio/mpeg':
        bot.send_audio(message.chat.id, message.audio.file_id)


@bot.message_handler(content_types=['text']) # +
def repeat_text(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['voice']) # +
def repeat_voice(message):
    bot.send_voice(message.chat.id, message.voice.file_id)


@bot.message_handler(content_types=['video'])  # + # это не кружок телеги
def repeat_all_video(message):
    bot.send_video(message.chat.id, message.video.file_id)


@bot.message_handler(content_types=['sticker']) # +
def repeat_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)


@bot.message_handler(content_types=["photo"]) # + !!!!!!!!!!!!!!!!!!!!
def repeat_photo(message):
    bot.send_photo(message.chat.id, message.photo[0].file_id)

# спросить у темы че я сделал ^ (почему работает обращение к первому ключу в списке, и почему их там так много почти одинаковых)

@bot.message_handler(content_types=['location'])   # +
def repeat_location(message):
    bot.send_location(message.chat.id, message.location.latitude, message.location.longitude)


@bot.message_handler(content_types=['video_note'])  # +
def repeat_video_note(message):
    bot.send_video_note(message.chat.id, message.video_note.file_id)


@bot.message_handler(content_types=['contact'])  # + как указать много номеров на вывод
def repeat_contact(message):
    bot.send_contact(message.chat.id, message.contact.phone_number, message.contact.first_name)


if __name__ == "__main__":
    print("Hello1")
    bot.infinity_polling()
    print("By")