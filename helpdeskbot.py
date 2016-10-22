import telegram
import logging
from telegram import (ReplyKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

answers = { 
        "привет": "И тебе привет!Меня зовут Jack-IT Support Bot, меня создали в лаборатории компании Jack-IT для помощи людям у которых есть проблемы с компьютерами", 
        "как дела?": "Нормально! А твои как?",
        "хорошо": "Ну и чудненько!Давай общаться?",
        "отлично": "Ну и чудненько!Давай общаться?",
        "пока": "До встречи!",
}

#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
 #                   level=logging.INFO)

#logger = logging.getLogger(__name__)

REG, CREATE = range(2)

def start(bot, update):
    print('Вызван /start')
    try:
        custom_keyboard = [['Регистрация']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.sendMessage(update.message.chat_id, text ='Добрый день! Вы только что запустили бота который умеет создавать заявки в системе Intraservice.Для начала работы нужно авторизоваться используя логин и пароль.Логином является почтовый ящик в системе Intraservice.', reply_markup=reply_markup)
        
    except Exception as ex:
        print(ex)
    return REG

#    print('Вызван /start')
 #      try:
  #      custom_keyboard = [[ "Регистрация" ]]
   #     reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    #    bot.sendMessage(update.message.chat_id, text='Прежде чем создать заявку нужно зарегистрироваться!', reply_markup=reply_markup)
    #except Exception as ex:
     #   print(ex)


def user_reg(bot, update):
    print('Вызван /user_reg')
    reply_keyboard = [['Авторизоваться']]

    return CREATE

def create_ticket(bot, update):
    print('Вызван /create_ticket')
    reply_keyboard = [['Создать заявку']]

    return ConversationHandler.END

def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Пока!')

    return ConversationHandler.END

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

#def talk_to_me(bot, update):
 #   print('Пришло сообщение: %s' % update.message.text)

#    def get_answers(key, answers):
  #      return answers.get(key, 'Я не совсем понимаю что Вы пишите.Мои создатели еще дописывают мой функционал, поэтому прошу вас подождать.')
 #   user_input = update.message.text.lower().strip()
    #answer = get_answers(user_input, answers)
   # bot.sendMessage(update.message.chat_id, text = answer)
   # bot.sendMessage(update.message.chat_id, update.message.text.encode('utf-8'))

def main():
    updater = Updater("141203240:AAEgIeBWoFcz_IW1qyNkR_pYy5GcXxERWTw")
    dp = updater.dispatcher
    #dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("user_reg", user_reg))
    dp.add_handler(CommandHandler("create_ticket", create_ticket))
    dp.add_handler(CommandHandler("cancel", cancel))
   # dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            REG: [RegexHandler('^Регистрация$', user_reg)],

            CREATE: [RegexHandler('^(Создание заявки)$', create_ticket)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()