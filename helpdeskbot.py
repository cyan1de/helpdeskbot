from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

answers = { 
        "привет": "И тебе привет!Меня зовут Jack-IT Support Bot, меня создали в лаборатории компании Jack-IT для помощи людям у которых есть проблемы с компьютерами", 
        "шалом": "алейхем шалом!",
        "как дела?": "Нормально! А твои как?",
        "хорошо": "Ну и чудненько!Давай общаться?",
        "отлично": "Ну и чудненько!Давай общаться?",
        "пока": "До встречи!",
}

def main():
    updater = Updater("TOKEN")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("kb", kb))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()


def start(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

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
