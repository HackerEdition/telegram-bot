import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

DIRECT_LINK = "https://t.me/ADSRBX_bot/ADSRBX"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Başla",
                url=DIRECT_LINK
            )
        ]
    ]

    await update.message.reply_text(
        "👋 Salam!\n\nBaşlamaq üçün düyməyə bas 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot işləyir...")
    app.run_polling()


if __name__ == "__main__":
    main()
