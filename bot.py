from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# استبدل هذا بـ API token الذي حصلت عليه من BotFather
API_TOKEN = '7806230405:AAEvzNdvb8FWqX-PRmLG1_hsP8TgQ1MKjsk'

# دالة الرد على الأمر /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت تلغرام بسيط.')

# دالة الرد على الأمر /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('استخدم الأمر /start للبدء.')

def main():
    # إعداد Updater باستخدام API token
    updater = Updater(API_TOKEN)

    # الحصول على Dispathcer لتوصيل الأحداث
    dispatcher = updater.dispatcher

    # إضافة معالجات للأوامر
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # بدء البوت
    updater.start_polling()

    # البوت يعمل حتى يتم إيقافه
    updater.idle()

if __name__ == '__main__':
    main()
