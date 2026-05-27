import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Render ENV-dən token oxunur
TOKEN = os.getenv("TOKEN")


# /start komandası
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🚀 Başla", callback_data="start")]
    ]

    text = (
        "👋 Salam!\n"
        "Veb app-dan pul qazanmaq istəyirsən?\n"
        "Düzgün yerdəsən 😎\n\n"
        "Başlamaq üçün aşağıdakı düyməyə kliklə 👇"
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# Button click handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start":
        await query.edit_message_text(
            "🔥 Başladıq!\n"
            "İndi sistem işə düşdü 🚀"
        )


# bot setup
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot işləyir...")
    app.run_polling()


if __name__ == "__main__":
    main()
