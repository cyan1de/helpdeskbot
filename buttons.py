import telegram

bot = telegram.Bot(token='141203240:AAEgIeBWoFcz_IW1qyNkR_pYy5GcXxERWTw')
updates = bot.getUpdates()
chat_id = bot.getUpdates()[-1].message.chat_id
custom_keyboard = [[ "Yes", "No"  ]]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
bot.sendMessage(chat_id=chat_id, text="Stay here, I'll be back.", reply_markup=reply_markup)