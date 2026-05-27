from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8875151704:AAEdjzghhJcn6AC1PiM6toka-NxcOgmZEVo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🚀 Başla", callback_data="start")]
    ]

    await update.message.reply_text(
        "👋 Salam!\n"
        "Veb app-dan pul qazanmaq istəyirsən?\n"
        "Düzgün yerdəsən 😎\n\n"
        "Başlamaq üçün bas 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start":
        await query.edit_message_text("🔥 Başladıq! Sistem işləyir...")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
