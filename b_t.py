
import telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler


import smtplib
from email.mime.text import MIMEText
from email.header import Header

import logging

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
















logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


REG,CREATE,CHECK,PRIORITY=range(4)




def start(bot, update):
    print('Вызван /start')
    try:
        custom_keyboard = [['Начать']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,one_time_keyboard=True)
        update.message.reply_text('Добрый день! Вы только что запустили бота.', reply_markup=reply_markup,one_time_keyboard=True)

    except Exception as ex:
        print(ex)


    return REG

   

 

def user_reg(bot, update):
    print('Вызван /user_reg')
    #custom_keyboard = [['Авторизоваться']]
    #reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,one_time_keyboard=True)
    update.message.reply_text("Введите логин и пароль")#reply_markup=reply_markup,one_time_keyboard=True)
    return CHECK


    

def login_pas(bot,update):
    print('Вызван /login_pas')
    log_pas=update.message.text.strip().split()
    if log_pas[0]=='a' and log_pas[1]=='b':
        print('Вызван /1')
        update.message.reply_text('good')


        mail_sender='georgy.reznev@gmail.com'
        mail_receiver='gora.reznev@yandex.ru'
        user_name='georgy.reznev@gmail.com'
        password=''
        server = smtplib.SMTP('smtp.gmail.com:587')


        subject = u'Тестовый email от ' + mail_sender
        body = u'Это тестовое письмо отправлено '
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')

        server.starttls()
        server.ehlo()
        server.login(user_name, password)
        server.sendmail(mail_sender, mail_receiver, msg.as_string())
        server.quit()


        custom_keyboard = [['Создать заявку']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,one_time_keyboard=True)
        update.message.reply_text("Создание заявки",reply_markup=reply_markup)



        return CREATE
    else:
        print('Вызван /2')
        update.message.reply_text('not good')
        return CHECK
            

def create_ticket(bot, update):
    print('Вызван /create_ticket')
    custom_keyboard = [['Обычный','Срочный']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,one_time_keyboard=True)
    update.message.reply_text("Выберите приоритет заявки",reply_markup=reply_markup)

    return PRIORITY

#выяснить,надо ли добавить отправление приоритета заявки на почту/в бд к админу

def priority_choise(bot,update):
    print("Вызван/priority_choice")
    if update.message.text=="Обычный":
        update.message.reply_text("Usual")
        return ConversationHandler.END 

    elif update.message.text=="Срочный":
        update.message.reply_text("High")   
        return ConversationHandler.END  


    

def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Пока!')

    return ConversationHandler.END

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


"""def talk_to_me(bot,update):
    print('Получено сообщение: %s' % update.message.text)"""





def main():
    print("Bot started")
    updater = Updater("289791861:AAG1KzSUCc5XlZr4G6dd6Bdt9bPUnbRWE2E")
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],


        states={
        REG: [RegexHandler('^Начать$',user_reg)],

        CHECK: [MessageHandler([Filters.text],login_pas)],

        CREATE: [MessageHandler([Filters.text],create_ticket)],


        PRIORITY: [RegexHandler('^Обычный|Срочный$',priority_choise)]
        },

         fallbacks=[CommandHandler('cancel',cancel)]

    )  

    try:
        dp.add_handler(conv_handler)
    except Exception as e:
        print(e)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)





#[Filters.text],user_reg        
#MessageHandler([Filters.text],  