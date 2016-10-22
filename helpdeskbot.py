from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

answers = { 
        "привет": "И тебе привет!Меня зовут Jack-IT Support Bot, меня создали в лаборатории компании Jack-IT для помощи людям у которых есть проблемы с компьютерами", 
        "как дела?": "Нормально! А твои как?",
        "хорошо": "Ну и чудненько!Давай общаться?",
        "отлично": "Ну и чудненько!Давай общаться?",
        "пока": "До встречи!",
}

def main():
    updater = Updater("141203240:AAEgIeBWoFcz_IW1qyNkR_pYy5GcXxERWTw")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()


def start(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
#    bot = telegram.Bot(token='141203240:AAEgIeBWoFcz_IW1qyNkR_pYy5GcXxERWTw')
    updates = bot.getUpdates()
    chat_id = bot.getUpdates()[-1].message.chat_id
    custom_keyboard = [[ "Yes", "No"  ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id=chat_id, text="Stay here, I'll be back.", reply_markup=reply_markup)

def talk_to_me(bot, update):
    print('Пришло сообщение: %s' % update.message.text)

    def get_answers(key, answers):
        return answers.get(key, 'Я не совсем понимаю что Вы пишите.Мои создатели еще дописывают мой функционал, поэтому прошу вас подождать.')
    user_input = update.message.text.lower().strip()
    answer = get_answers(user_input, answers)
    bot.sendMessage(update.message.chat_id, text = answer)
    bot.sendMessage(update.message.chat_id, update.message.text.encode('utf-8'))

if __name__ == '__main__':
    main()